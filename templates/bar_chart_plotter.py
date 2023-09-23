import matplotlib.pyplot as plt

def plot_bar_chart(categories, values, title="Bar Chart", xlabel="Categories", ylabel="Values", color="blue", show=True, save_path=None):
    """
    Plots a vertical bar chart for the given data.

    Parameters:
    - categories (list of str): Category names.
    - value (list of numbers): Values corresponding to each category.
    - title (str): Title of the bar
    - xlabel (str): X-axis label.
    - ylabel (str): Y-axis label.
    - color (str): Color of the bars.
    - show (bool): Whether to display the chart.
    - save_path (str): If provided, save the chart to this path.

    Returns:
    - matplotlib.axes.Axes: Axes object with the bar chart.
    """

    fig, ax = plt.subplots()
    ax.bar(categories, values, color=color)

    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    if save_path:
        plt.savefig(save_path, format='png', dpi=300)

    if show:
        plt.show()

    return ax

# Example usage:
if __name__ == "__main__":
    categories = ["A", "B", "C", "D"]
    values = [5, 7, 3, 8]
    plot_bar_chart(categories, values, title="Sample Bar Chart", xlabel="Categories", ylabel="Values")