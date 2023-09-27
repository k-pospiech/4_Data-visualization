import matplotlib.pyplot as plt
import seaborn as sns

def plot_violin(data, x_labels, title="Violin Plot", ylabel="Values", show=True, save_path=None):
    """
    Plots a violin plot for the given data.

    Parameters:
    - data (list of lists or 2D array-like): Data to be plotted. Each inner list is one "violin"
    - x_labels (list of str): Labels for the x-axis (corresponding to each inner list of data)
    - title (str): Title of the plot
    - ylabel (str): Y-axis label
    - show (bool): Whether to display the plot
    - save_path (str): If provided, save the plot to this path

    Returns:
    - matplotlib.axes.Axes: Axes object with the violin plot
    """

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.violinplot(data=data, ax=ax, palette="muted")

    ax.set_title(title)
    ax.set_xticklabels(x_labels)
    ax.set_ylabel(ylabel)

    if save_path:
        plt.savefig(save_path, format="png", dpi=300)

    if show:
        plt.show()

    return ax

# # Example usage:
# if __name__ == "__main__":
#     data_sample = [
#         [5, 6, 6, 7, 8, 8, 9, 10, 11],
#         [1, 2, 2, 3, 3, 4, 5, 5, 6],
#         [7, 7, 8, 8, 9, 10, 11, 12, 13]
#     ]
#     labels_sample = ["Group A", "Group B", "Group C"]
#     plot_violin(data_sample, labels_sample, title="Sample Violin Plot", ylabel="Value Range")