import matplotlib.pyplot as plt

def plot_pie_chart(labels, sizes, title="Pie Chart", colors=None, explode=None, show=True, save_path=None):
    """
    Plots a pie chart for the given data.

    Parameters:
    - labels (list of str): Labels for each segment
    - sizes (list of numbers): Sizes for each segment
    - title (str): Title of the pie chart
    - colors (list of str, optional): Colors for each segment
    - explode (list of numbers, optional): Fraction to "explode" each segment. If used, should be same length as labels
    - show (bool): Whether to display the chart
    - save_path (str): If provided, save the chart to this path

    Returns:
    - matplotlib.axes.Axes: Axes object with the pie chart
    """

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, colors=colors, explode=explode, autopct='%1.1f%%', startangle=90)
    ax.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle
    ax.set_title(title)

    if save_path:
        plt.savefig(save_path, format='png', dpi=300)

    if show:
        plt.show()

    return ax

# # Example usage:
# if __name__ == "__main__":
#     labels = ["A", "B", "C", "D"]
#     sizes = [15, 30, 45, 10]
#     colors = ["red", "yellow", "blue", "green"]
#     explode = (0.1, 0, 0, 0)  # "explode" the 1st slice (i.e., 'A')
#     plot_pie_chart(labels, sizes, title="Sample Pie Chart", colors=colors, explode=explode)