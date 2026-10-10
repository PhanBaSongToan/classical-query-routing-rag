from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch


OUT = Path(__file__).parent / "figures"
OUT.mkdir(exist_ok=True)

fig, ax = plt.subplots(figsize=(6.6, 8.0))
ax.set_xlim(0, 10)
ax.set_ylim(0, 14)
ax.axis("off")


def box(x, y, w, h, title, subtitle="", fontsize=11):
    patch = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.04,rounding_size=0.08",
                           linewidth=1.2, edgecolor="black", facecolor="0.93")
    ax.add_patch(patch)
    ax.text(x + w / 2, y + h * 0.62, title, ha="center", va="center", fontsize=fontsize, weight="bold")
    if subtitle:
        ax.text(x + w / 2, y + h * 0.30, subtitle, ha="center", va="center", fontsize=9)


def arrow(x1, y1, x2, y2):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>", mutation_scale=12,
                                 linewidth=1.1, color="black"))


box(3.55, 12.3, 2.9, 0.75, "User query")
box(1.55, 9.85, 6.9, 1.2, "Feature extraction", "TF-IDF / character / structural features", fontsize=10)
box(3.25, 7.55, 3.5, 0.85, "Classical router")
arrow(5.0, 12.3, 5.0, 11.05)
arrow(5.0, 9.85, 5.0, 8.4)

centers = [1.55, 5.0, 8.45]
labels = [("Single-hop", "NaiveRAG"), ("Multi-hop", "HybridRAG"), ("Summary", "IterativeRAG")]
for x, (query_type, rag) in zip(centers, labels):
    box(x - 1.2, 4.45, 2.4, 0.8, query_type, fontsize=10)
    box(x - 1.25, 1.55, 2.5, 0.8, rag, fontsize=10)
    arrow(5.0, 7.55, x, 5.25)
    arrow(x, 4.45, x, 2.35)

fig.tight_layout(pad=0.2)
fig.savefig(OUT / "query_routing_pipeline.png", dpi=400, bbox_inches="tight", facecolor="white")
fig.savefig(OUT / "query_routing_pipeline.pdf", bbox_inches="tight", facecolor="white")
plt.close(fig)

