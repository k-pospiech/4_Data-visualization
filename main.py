import sys
from utilities.data_loader import load_data
from utilities.normalizer import normalize_data
from utilities.missing_value_handler import handle_missing_values
from utilities.categorical_to_numerical import convert_categorical_to_numerical
from templates.histogram_plotter import plot_histogram
from templates.scatter_plot_regression import plot_scatter_with_regression
# Import other visualization templates as needed

def main():
    # 1. Data Input
    data_filepath = input("Enter the path to your data file: ")
    data = load_data(data_filepath)

    # Example: Normalize data
    columns_to_normalize = input("Enter columns to normalize (comma-separated), or press enter to skip: ")
    if columns_to_normalize:
        columns_to_normalize = columns_to_normalize.split(',')
        data = normalize_data(data, columns=columns_to_normalize)

    # More data manipulation options can be added there

    # 2. Visualization Selection
    print("Select a visualization type:")
    print("1. Histogram")
    print("2. Scatter Plot")
    # Ad more options as per templates
    viz_type = input()

    if viz_type == "1":
        # User inputs for histogram
        column = input("Enter the column name for the histogram: ")
        title = input("Enter the title for the histogram: ")
        xlabel = input("Enter the xlabel for the histogram: ")
        ylabel = input("Enter the ylabel for the histogram: ")
        plot_histogram(data, column, title=title, xlabel=xlabel, ylabel=ylabel)
    elif viz_type == "2":
        # User inputs for scatter plot
        x_column = input("Enter the x column name for the scatter plot: ")
        y_column = input("Enter the y column name for the scatter plot: ")
        title = input("Enter the title for the scatter plot: ")
        xlabel = input("Enter the xlabel for the scatter plot: ")
        ylabel = input("Enter the ylabel for the scatter plot: ")
        plot_scatter(data, x_column, y_column, title=title, xlabel=xlabel, ylabel=ylabel)
    # Additional visualization options should be added similarly

    # 3. Display/Export Visualization
    # (The plots might already be displayed by the visualization functions, or you might want to save/export them)

if __name__ == "__main__":
    main()