import matplotlib.pyplot as plt


def update_training_curve_plot(
    fig, ax1, ax2, train_losses, test_losses, train_accuracies, test_accuracies, steps
):
    # Plot loss
    ax1.clear()
    ax1.plot(
        range(len(train_losses)),
        train_losses,
        "b-",
        alpha=0.7,
        label=f"Train Loss: {train_losses[-1]:.3f}",
    )
    ax1.plot(
        steps, test_losses, "r-", marker="o", label=f"Test Loss: {test_losses[-1]:.3f}"
    )
    ax1.set_title("Loss")
    ax1.set_xlabel("Step")
    ax1.set_ylabel("Loss")
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # Plot accuracy
    ax2.clear()
    ax2.plot(
        range(len(train_accuracies)),
        train_accuracies,
        "b-",
        alpha=0.7,
        label=f"Train Accuracy: {train_accuracies[-1]:.3f}",
    )
    ax2.plot(
        steps,
        test_accuracies,
        "r-",
        marker="o",
        label=f"Test Accuracy: {test_accuracies[-1]:.3f}",
    )
    ax2.set_title("Accuracy")
    ax2.set_xlabel("Step")
    ax2.set_ylabel("Accuracy")
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()

    return fig
