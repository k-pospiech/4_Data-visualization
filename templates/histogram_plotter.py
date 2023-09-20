import matplotlib.pyplot as plt

def plot_histogram(data, bins=10, title="Histogram", xlabel="Value", ylabel="Frequency", color="blue", show=True, save_path=None):
    """
    Plots a histogram for the given data.

    Parameters:
    - data (list or array-like): Data to be plotted
    - bins (int or sequence): Number of histogram bins or a sequence defining bins edges
    - title (str): Title of the histogram
    - xlabel (str): X-axis label
    - ylabel (str): Y-axis label
    - color (str): Color of the histogram bars
    - show (bool): Whether to display the plot
    - save_path (str): If provided, save the plot to this path

    Returns:
    - matplotlib.axes.Axes: Axes object with the histogram
    """

    fig, ax = plt.subplots()
    ax.hist(data, bins=bins, color=color)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    if save_path:
        plt.savefig(save_path, format='png', dpi=300)

    if show:
        plt.show()

    return ax

# # Example usage:
# if __name__ == "__main__":
#     data = [1, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5]
#     plot_histogram(data, bins=5, title="Sample Histogram", xlabel="Number", ylabel="Count")