"""Export a static risk/return plot without assigning a weighted score."""

from pathlib import Path

from .comparison import StrategySummary, frontier_names
from .scoring import ScoreBounds


def plot_frontier(
    summaries: tuple[StrategySummary, ...], bounds: ScoreBounds, output: Path
) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    if not summaries:
        raise ValueError("no strategy results to plot")
    frontier = frontier_names(summaries)
    fig, ax = plt.subplots(figsize=(9, 6))
    fig.subplots_adjust(left=0.12, right=0.96, bottom=0.21, top=0.89)
    risk_midpoint = (min(item.downside_risk for item in summaries)
                     + max(item.downside_risk for item in summaries)) / 2
    for item in summaries:
        selected = item.name in frontier
        ax.scatter(
            item.downside_risk, item.average_normalized_score,
            color="#087e8b" if selected else "#969da5",
            marker="D" if selected else "o", s=65,
        )
        right_side = item.downside_risk > risk_midpoint
        ax.annotate(item.name, (item.downside_risk, item.average_normalized_score),
                    xytext=(-6 if right_side else 6, 6), textcoords="offset points",
                    ha="right" if right_side else "left")
    ax.axhline(0, color="#b55b43", linestyle="--", linewidth=1, label="C = G analytical anchor")
    ax.axhline(100, color="#68778a", linestyle=":", linewidth=1, label="Zero-price grid ideal")
    ax.set(xlabel="Downside risk (lower semideviation, normalized points)",
           ylabel="Average normalized campaign score Q (%)",
           title=f"Risk–return frontier · {bounds.capacity_per_submission_mw:g} MW per submission")
    ax.grid(alpha=0.2)
    ax.margins(x=0.15)
    ax.legend(loc="best")
    fig.text(0.5, 0.035, "Diamonds: nondominated strategies. Scenarios equally weighted.\nUpper anchor assumes full allocation and zero grid-energy prices.",
             ha="center", fontsize=8)
    try:
        fig.savefig(output, dpi=160, bbox_inches="tight")
    finally:
        plt.close(fig)
