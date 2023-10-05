import seaborn as sns
import matplotlib.pyplot as plt

def plot_corr_matrix(data, title="Correlation Matrix", cmap="coolwarm", annot=True, figsize=(10, 8)):
    """
    Plot a correlation matrix heatmap.
    
    Parameters:
        data (pd.DataFrame): The data frame containing the data.
        title (str): The title for the plot. Default is "Correlation Matrix".
        cmap (str): The color map to use for the heatmap. Default is "coolwarm".
        annot (bool): Whether to annotate cells with their values. Default is True.
        figsize (tuple): The size of the figure. Default is (10, 8).
    """
    # Compute the correlation matrix
    corr = data.corr()

    # Create a heatmap
    plt.figure(figsize=figsize)
    sns.heatmap(corr, cmap=cmap, annot=annot, fmt=".2f", linewidths=.5, cbar_kws={"shrink": .5})
    
    # Add title and show the plot
    plt.title(title, fontsize=18)
    plt.show()

# # Example usage:
# import pandas as pd

# # Sample data
# data = {
#     'A': [45, 37, 42, 35, 39],
#     'B': [38, 31, 26, 28, 33],
#     'C': [10, 15, 17, 21, 12]
# }

# df = pd.DataFrame(data)

# # Usage
# plot_corr_matrix(df, title="Sample Correlation Matrix")
