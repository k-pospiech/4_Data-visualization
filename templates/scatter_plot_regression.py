import matplotlib.pyplot as plt
import numpy as np

def plot_scatter_with_regression(x, y, title="Scatter Plot with Regression", xlabel="X", ylabel="Y", color="blue", show=True, save_path=None):
    """
    Plots a scatter plot with a regression line for the given data.

    Parameters:
    - x (list or array-like): X-axis data
    - y (list or array-like): Y-axis data
    - title (str): Title of the plot
    - xlabel (str): X-axis label
    - ylabel (str): Y-axis label
    - color (str): Color of the scatter points
    - show (bool): Whether to display the plot
    - save_path (str): If provided, save the plot to this path

    Returns:
    - matplotlib.axes.Axes: Axes object with the scatter plot and regression line
    """

    fig, ax = plt.subplots()
    ax.scatter(x, y, color=color, label="Data Points")

    # Calculate regression coefficients (slope and intercept)
    m, b = np.polyfit(x, y, 1)

    # Generate regression line
    ax.plot(x, m*np.array(x) + b, color="red", label=f"Regression line (y={m:.2f}x + {b:.2f})")
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(color="gainsboro")
    ax.legend()

    if save_path:
        plt.savefig(save_path, format='png', dpi=300)

    if show:
        plt.show()

    return ax

# # Example usage:
# if __name__ == "__main__":
#     x = [1, 2, 3, 4, 5]
#     y = [2, 4.1, 5.9, 8.3, 9.8]
#     plot_scatter_with_regression(x, y, title="Sample Scatter Plot with Regression", xlabel="X Values", ylabel="Y Values")