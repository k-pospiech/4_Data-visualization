import matplotlib.pyplot as plt
import seaborn as sns

def plot_heatmap(data, xlabels, ylabels, title="Heatmap", cmap="viridis", show=True, save_path=None):
    """
    Plots a heatmap for the given data.

    Parameters:
    - data (2D list or array-like): Data to be plotted
    - xlabels (list of str): Labels for the x-axis (typically columns of the data)
    - ylabels (list of str): Labels for the y-axis (trpically rows of the data)
    - title (str): Title of the heatmap
    - cmap (str): Colormap to use
    - show (bool): Whether to display the heatmap
    - save_path (str): If provided, save the heatmap to this path

    Returns:
    - matplotlib.axes.Axes: Axes object with the heatmap
    """

    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(data, annot=True, ax=ax, cmap=cmap, xticklabels=xlabels, yticklabels=ylabels)

    ax.set_title(title)

    if save_path:
        plt.savefig(save_path, format='png', dpi=300)

    if show:
        plt.show()

    return ax

# # Example usage:
# if __name__ == "__main__":
#     data = [
#         [0.1, 0.3, 0.5],
#         [0.5, 0.2, 0.4],
#         [0.6, 0.8, 1.0]
#     ]
#     xlabels = ["X1", "X2", "X3"]
#     ylabels = ["Y1", "Y2", "Y3"]
#     plot_heatmap(data, xlabels, ylabels, title="Sample Heatmap")