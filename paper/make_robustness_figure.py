from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


OUT = Path(__file__).parent / "figures"
OUT.mkdir(exist_ok=True)

protocols = [
    "Shuffled\n10 seeds",
    "Source-order\n5-fold",
    "Normalized\nquery groups",
    "Template\ngroups",
    "Leave-one-domain\nout",
]
accuracy = np.array([0.952103, 0.845477, 0.945257, 0.943574, 0.640611])
macro_f1 = np.array([0.947794, 0.844831, 0.941325, 0.939318, 0.672924])
paper_accuracy = 0.932
paper_macro_f1 = 0.928

x = np.arange(len(protocols))
fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.5), sharey=True)

for ax, values, reference, ylabel in [
    (axes[0], accuracy, paper_accuracy, "Accuracy"),
    (axes[1], macro_f1, paper_macro_f1, "Macro-F1"),
]:
    bars = ax.bar(x, values, width=0.68, color="0.82", edgecolor="black", linewidth=0.8)
    for bar, hatch in zip(bars, ["", "//", "\\\\", "..", "xx"]):
        bar.set_hatch(hatch)
    ax.axhline(reference, color="black", linestyle="--", linewidth=1.0,
               label=f"Paper reference ({reference:.3f})")
    ax.set_ylim(0.55, 1.0)
    ax.set_ylabel(ylabel)
    ax.set_xticks(x, protocols, rotation=0, ha="center")
    ax.tick_params(axis="x", labelsize=8.5, pad=5)
    ax.grid(axis="y", color="0.86", linewidth=0.7)
    ax.set_axisbelow(True)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    for i, value in enumerate(values):
        ax.text(i, value + 0.012, f"{value:.3f}", ha="center", va="bottom", fontsize=8)

axes[0].set_title("Performance")
axes[1].set_title("Robustness across evaluation protocols")
axes[1].legend(frameon=False, loc="lower left", fontsize=8)
fig.suptitle("Classical router performance and robustness", fontsize=13, weight="bold")
fig.tight_layout(rect=(0, 0, 1, 0.94), pad=0.7)
fig.savefig(OUT / "robustness_performance.png", dpi=400, bbox_inches="tight", facecolor="white")
fig.savefig(OUT / "robustness_performance.pdf", bbox_inches="tight", facecolor="white")
plt.close(fig)
