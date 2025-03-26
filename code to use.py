import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def scatter_with_marginals(x, y, 
                            x_label='X Axis', 
                            y_label='Y Axis', 
                            title='Scatter Plot with Marginal Distributions',
                            figsize=(10, 8)):
    """
    Create a scatter plot with marginal distributions using Matplotlib.
    
    Parameters:
    -----------
    x : array-like
        Data for x-axis
    y : array-like
        Data for y-axis
    x_label : str, optional
        Label for x-axis
    y_label : str, optional
        Label for y-axis
    title : str, optional
        Title of the plot
    figsize : tuple, optional
        Figure size (width, height)
    
    Returns:
    --------
    fig : matplotlib.figure.Figure
        The created figure object
    """
    # Create the figure and grid
    fig = plt.figure(figsize=figsize)
    
    # Create grid specification
    gs = fig.add_gridspec(2, 2, 
        width_ratios=[3, 1], 
        height_ratios=[1, 3],
        hspace=0.1, 
        wspace=0.1
    )
    
    # Main scatter plot
    ax_scatter = fig.add_subplot(gs[1, 0])
    ax_scatter.scatter(x, y, alpha=0.7, edgecolors='black', linewidth=0.5)
    ax_scatter.set_xlabel(x_label)
    ax_scatter.set_ylabel(y_label)
    
    # Top marginal (x distribution)
    ax_marginal_x = fig.add_subplot(gs[0, 0], sharex=ax_scatter)
    ax_marginal_x.hist(x, bins=20, alpha=0.7, color='skyblue', edgecolor='black')
    ax_marginal_x.set_title(title)
    plt.setp(ax_marginal_x.get_xticklabels(), visible=False)
    ax_marginal_x.yaxis.tick_right()
    
    # Right marginal (y distribution)
    ax_marginal_y = fig.add_subplot(gs[1, 1], sharey=ax_scatter)
    ax_marginal_y.hist(y, bins=20, orientation='horizontal', 
                       alpha=0.7, color='lightgreen', edgecolor='black')
    plt.setp(ax_marginal_y.get_yticklabels(), visible=False)
    ax_marginal_y.xaxis.tick_top()
    
    return fig

# Example usage
def main():
    # Generate sample data
    np.random.seed(42)
    x = np.random.normal(0, 1, 500)
    y = x * 0.5 + np.random.normal(0, 0.5, 500)
    
    # Create the plot
    fig = scatter_with_marginals(
        x, y, 
        x_label='X Variable', 
        y_label='Y Variable', 
        title='Sample Scatter Plot with Marginal Distributions'
    )
    
    # Save the plot
    plt.savefig('scatter_with_marginals.png', dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == '__main__':
    main()

# Additional customization options
def advanced_scatter_with_marginals(x, y, 
                                    x_label='X Axis', 
                                    y_label='Y Axis', 
                                    title='Advanced Scatter Plot',
                                    color_scatter='blue',
                                    color_x_marginal='skyblue',
                                    color_y_marginal='lightgreen',
                                    figsize=(10, 8)):
    """
    Advanced version with more customization options.
    
    Additional parameters allow for more detailed plot customization.
    """
    # (Same implementation as previous function with added color parameters)
    # ... (code would be similar to the previous function)
    pass