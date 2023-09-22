import matplotlib.pyplot as plt

def plot_box(data, labels=None, title="Box Plot", ylabel="Values", show=True, save_path=None):
    """
    Plots a box plot for the given data.

    Parameters:
    - data (list of lists or array-like): Data to be plotted. Each inner list is a separate box plot.
    - labels (list of str): Labels for each dataset. Should be the same length as data.
    - title (str): Title of the box plot.
    - ylabel (str): Y-axis label.
    - show (bool): Whether to display the plot.
    - save_path (str): If provided, save the plot to this path.
    
    Returns:
    - matplotlib.axes.Axes: Axes object with the box plot.
    """

    fig, ax = plt.subplots()
    ax.boxplot(data, labels=labels, vert=True, patch_artist=True) # vert=True makes the plot vertical. patch_artist=True helps in setting custom colors.

    ax.set_title(title)
    ax.set_ylabel(ylabel)

    if save_path:
        plt.savefig(save_path, format="png", dpi=300)

    if show:
        plt.show()

    return ax

# # Example usage:
# if __name__ == "__main__":
#     data1 = [1, 2, 2.5, 3, 3.5, 4, 5]
#     data2 = [2, 3, 3.5, 4, 4.5, 5, 6]
#     data = [data1, data2]
#     labels = ["Dataset 1", "Dataset 2"]
#     plot_box(data, labels=labels, title="Sample Box Plot", ylabel="Value Range")