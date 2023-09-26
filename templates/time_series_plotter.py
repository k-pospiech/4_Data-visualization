import matplotlib.pyplot as plt

def plot_time_series(dates, values, title="Time Series Plot", xlabel="Date", ylabel="Value", color="blue", show=True, save_path=None):
    """
    Plots a time series for the given data.

    Parameters:
    - dates (list of dates): Dates for the x-axis
    - values (list of numbers): Values for the y-axis
    - title (str): Title of the plot
    - xlabel (str): X-axis label
    - ylabel (str): Y-axis label
    - color (str): Color of the time series line
    - show (bool): Whether to display the plot
    - save_path (str): If provided, save the plot to this path

    Returns:
    - matplotlib.axes.Axes: Axes object with the time series plot
    """

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(dates, values, color=color, label=ylabel)

    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.legend(loc='upper left')

    fig.autofmt_xdate() # Rotate and align the x labels for better display 

    if save_path:
        plt.savefig(save_path, format="png", dpi=300)

    if show:
        plt.show()

    return ax

# # Example usage:
# if __name__ == "__main__":
#     from datetime import date, timedelta

#     # Generating some sample dates and values
#     start_date = date.today() - timedelta(days=10)
#     dates = [start_date + timedelta(days=i) for i in range(10)]
#     values = [i + (i * 0.1) for i in range(10)]

#     plot_time_series(dates, values, title="Sample Time Series Plot", xlabel="Date", ylabel="Value")