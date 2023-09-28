import seaborn as sns
import matplotlib.pyplot as plt

def plot_facet_grid(data, row_variable, col_variable, plot_type, title="Facet Grid Plot", **kwargs):
    """
    Plots a facet grid for the given data.

    Parameters:
    - data (DataFrame): Data to be plotted.
    - row_variable (str): Variable in data for rows of the grid.
    - col_variable (str): Variable in data for columns of the grid.
    - plot_type (function): Seaborn plotting function (e.g., sns.scatterplot).
    - title (str): Title for the entire grid.
    - **kwargs: Additional keyword arguments to be passed to the plotting function.

    Returns:
    - seaborn.FacetGrid: The FacetGrid object.
    """

    g = sns.FacetGrid(data, row=row_variable, col=col_variable, margin_titles=True)
    g = g.map_dataframe(plot_type, **kwargs)
    g.fig.suptitle(title, y=1.03)

    return g

# # Example usage:
# if __name__ == "__main__":
#     import pandas as pd

#     # Sample data
#     data_sample = pd.DataFrame({
#         'A': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'],
#         'B': ['one', 'one', 'two', 'two', 'one', 'one'],
#         'X': [1, 2, 3, 4, 5, 6],
#         'Y': [2, 3, 4, 5, 6, 7]
#     })

#     plot_facet_grid(data_sample, 'A', 'B', sns.scatterplot, x='X', y='Y')
#     plt.show()