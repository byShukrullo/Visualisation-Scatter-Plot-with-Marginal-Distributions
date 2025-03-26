# Scatter Plot with Marginal Distributions

## Overview
A Python implementation of a scatter plot with marginal distributions using Matplotlib. This visualization provides additional context about the distribution of data along x and y axes.

# Example output
![Visualization-Scatter-Plot-with-Marginal-Distributions](/output124.png)

## Requirements
- Python 3.7+
- Matplotlib
- NumPy
- SciPy

## Installation
```bash
pip install matplotlib numpy scipy
```

## Usage

### Basic Example
```python
import numpy as np
from scatter_with_marginals import scatter_with_marginals

# Generate sample data
x = np.random.normal(0, 1, 500)
y = x * 0.5 + np.random.normal(0, 0.5, 500)

# Create the plot
fig = scatter_with_marginals(x, y, 
    x_label='X Variable', 
    y_label='Y Variable', 
    title='Sample Scatter Plot'
)

# Save or show the plot
plt.savefig('scatter_plot.png')
plt.show()
```

## Features
- Scatter plot with main data points
- Marginal distributions for x and y axes
- Customizable labels and title
- Easy to use with NumPy arrays

## Parameters
- `x`: X-axis data
- `y`: Y-axis data
- `x_label`: Label for x-axis
- `y_label`: Label for y-axis
- `title`: Plot title
- `figsize`: Figure size tuple

## Contributing
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

