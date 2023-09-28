import matplotlib.pyplot as plt

def plot_bubble(x, y, size, labels=None, title="Bubble Plot", xlabel="X", ylabel="Y", size_scale=100, color="blue", alpha=0.6, show=True, save_path=None):
    """
    Plots a bubble plot for the given data.
    
    Parameters:
    - x (list or array-like): Data for the x-axis.
    - y (list or array-like): Data for the y-axis.
    - size (list or array-like): Determines the size of bubbles.
    - labels (list of str, optional): Labels for each data point.
    - title (str): Title of the plot.
    - xlabel (str): X-axis label.
    - ylabel (str): Y-axis label.
    - size_scale (int or float): Scaling factor for the bubble sizes.
    - color (str): Color of the bubbles.
    - alpha (float): Opacity of the bubbles.
    - show (bool): Whether to display the plot.
    - save_path (str): If provided, save the plot to this path.

    Returns:
    - matplotlib.axes.Axes: Axes object with the bubble plot.
    """

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(x, y, s=[i*size_scale for i in size], color=color, alpha=alpha)
    
    if labels:
        for i, label in enumerate(labels):
            ax.annotate(label, (x[i], y[i]))

    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)  # Adding the grid

    if save_path:
        plt.savefig(save_path, format='png', dpi=300)
    
    if show:
        plt.show()

    return ax

# # Example usage:
# if __name__ == "__main__":
#     x_sample = [1, 2, 3, 4, 5]
#     y_sample = [2, 4, 1, 3, 5]
#     size_sample = [0.1, 0.2, 0.6, 0.4, 0.5]
#     labels_sample = ["A", "B", "C", "D", "E"]

#     plot_bubble(x_sample, y_sample, size_sample, labels=labels_sample, title="Sample Bubble Plot", xlabel="X Values", ylabel="Y Values")