import matplotlib.pyplot as plt
import pandas as pd


def plot_target_distribution(
    y: pd.Series, title: str = "Customer Churn Distribution") -> None:
    """Plots and displays the distribution of the target variable."""
    ax = y.value_counts().plot(kind="bar", color=["#2b5c8f", "#d95f02"], edgecolor="black")
    plt.title(title, fontsize=12, fontweight="bold")
    plt.xlabel("Churn (0 = Retained, 1 = Churned)", fontsize=10)
    plt.ylabel("Number of Customers", fontsize=10)
    plt.xticks(rotation=0)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    
    # Add count labels on top of the bars
    for p in ax.patches:
        ax.annotate(
            str(p.get_height()),
            (p.get_x() + p.get_width() / 2.0, p.get_height()),
            ha="center",
            va="bottom",
        )

    plt.tight_layout()
    plt.show()