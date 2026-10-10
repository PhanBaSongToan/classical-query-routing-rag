from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


OUT = Path(__file__).parent / "figures"
OUT.mkdir(exist_ok=True)

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Times New Roman", "DejaVu Serif", "Liberation Serif"],
    "font.size": 9,
    "axes.titlesize": 11,
    "axes.labelsize": 9,
})

protocols = [
    "Shuffled\n10 seeds",
    "Source-order\n5-fold",
    "Normalized-query\ngroups",
    "Template\ngroups",
    "Leave-one-domain\nout",
]
accuracy = np.array([0.952103, 0.845477, 0.945257, 0.943574, 0.640611])
macro_f1 = np.array([0.947794, 0.844831, 0.941325, 0.939318, 0.672924])

x = np.arange(len(protocols))
width = 0.35
fig, ax = plt.subplots(figsize=(7.4, 4.3), dpi=300)

bars_accuracy = ax.bar(
    x - width / 2, accuracy, width, label="Accuracy",
    color="0.28", edgecolor="black", linewidth=0.8, hatch="//",
)
bars_f1 = ax.bar(
    x + width / 2, macro_f1, width, label="Macro-F1",
    color="0.82", edgecolor="black", linewidth=0.8, hatch="..",
)

ax.axhline(0.932, color="0.25", linestyle="--", linewidth=1.0,
           label="Paper accuracy reference (0.932)")
ax.axhline(0.928, color="0.05", linestyle=":", linewidth=1.0,
           label="Paper macro-F1 reference (0.928)")

ax.set_title("Classical router performance and robustness", fontweight="bold", pad=10)
ax.set_ylabel("Score")
ax.set_ylim(0.55, 1.0)
ax.set_xticks(x, protocols)
ax.tick_params(axis="x", labelsize=8, pad=5)
ax.grid(axis="y", linestyle=":", linewidth=0.7, color="0.70", alpha=0.8)
ax.set_axisbelow(True)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

for bars in (bars_accuracy, bars_f1):
    for bar in bars:
        ax.annotate(
            f"{bar.get_height():.3f}",
            xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
            xytext=(0, 3), textcoords="offset points",
            ha="center", va="bottom", fontsize=7.5,
        )

ax.legend(loc="lower left", frameon=True, framealpha=0.95,
          edgecolor="0.55", fontsize=7.5)
fig.tight_layout(pad=0.7)
fig.savefig(OUT / "classical_router_performance.png", dpi=400,
            bbox_inches="tight", facecolor="white")
fig.savefig(OUT / "classical_router_performance.pdf",
            bbox_inches="tight", facecolor="white")
plt.close(fig)
