import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

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
    scatter = ax_scatter.scatter(x, y, 
                                 alpha=0.7, 
                                 c=y,  # Color by y-value
                                 cmap='viridis', 
                                 edgecolors='black', 
                                 linewidth=0.5)
    ax_scatter.set_xlabel(x_label)
    ax_scatter.set_ylabel(y_label)
    
    # Add colorbar
    fig.colorbar(scatter, ax=ax_scatter, shrink=0.8, aspect=20)
    
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

def main():
    # Simulate student data: study hours vs. exam scores
    np.random.seed(42)
    
    # Generate correlated data
    study_hours = np.random.normal(5, 2, 200)  # Mean 5 hours, std dev 2
    exam_scores = 50 + 5 * study_hours + np.random.normal(0, 10, 200)
    
    # Create a DataFrame for better data handling
    df = pd.DataFrame({
        'Study Hours': study_hours,
        'Exam Scores': exam_scores
    })
    
    # Calculate correlation
    correlation = df['Study Hours'].corr(df['Exam Scores'])
    
    # Create the plot
    fig = scatter_with_marginals(
        df['Study Hours'], 
        df['Exam Scores'], 
        x_label='Study Hours', 
        y_label='Exam Scores', 
        title=f'Study Hours vs. Exam Scores (Correlation: {correlation:.2f})'
    )
    
    # Print some basic statistics
    print(df.describe())
    print(f"\nCorrelation between Study Hours and Exam Scores: {correlation:.2f}")
    
    # Display the plot
    plt.show()

if __name__ == '__main__':
    main() 