import matplotlib.pyplot as plt
from format import format_chart
import numpy as np
from math import e
import matplotlib.ticker as ticker

@format_chart
def multiline_plot(data, figsize=(10, 6), title="Multiline Plot", xlabel="Index", ylabel="Value", grid=True):
    fig, ax = plt.subplots(figsize=figsize)
    for name, x, y in data:
        ax.plot(x,y, label=name)
    ax.legend()
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(grid, linestyle="--", alpha=0.6)
    ax.xaxis.set_major_locator(ticker.LinearLocator(10))
    ax.xaxis.set_minor_locator(ticker.LinearLocator(min(len(x),999)))
    plt.tight_layout()
    return ax




def plot_line_and_bar(line_data, bar_data, line_label, bar_label, title, xlabel, line_color='black', bar_color='orange', figsize=(10, 6)):
    x = np.arange(len(line_data))  # Create x-coordinates
    # Create a figure and primary axis
    fig, ax1 = plt.subplots(figsize=figsize)

    # Plot the line chart
    ax1.plot(x, line_data, label=line_label, color=line_color, linewidth=2)
    ax1.set_ylabel(line_label, color=line_color)
    ax1.tick_params(axis='y', labelcolor=line_color)
    ax1.set_xlabel(xlabel)

    # Create a secondary axis for the bar chart
    ax2 = ax1.twinx()
    ax2.bar(x, bar_data, label=bar_label, color=bar_color, alpha=0.6, width=0.4)
    ax2.set_ylabel(bar_label, color=bar_color)
    ax2.tick_params(axis='y', labelcolor=bar_color)

    # Add title and grid
    ax1.set_title(title.upper(), pad=20)
    ax1.grid(True, linestyle='--', alpha=0.5)

    # Combine legends from both axes
    lines, labels = ax1.get_legend_handles_labels()
    bars, bar_labels = ax2.get_legend_handles_labels()
    ax1.legend(lines + bars, labels + bar_labels, loc='upper left')

    # Adjust layout and show plot
    plt.tight_layout()
    plt.show()

# Example usage:
# line_data = [1, 2, 3, 4, 5]
# bar_data = [5, 4, 3, 2, 1]
# plot_line_and_bar(line_data, bar_data, "Line Chart", "Bar Chart", "Line and Bar Chart Example", "X-axis Label")

