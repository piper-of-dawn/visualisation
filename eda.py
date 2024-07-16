import plotly.graph_objects as go
import numpy as np

def plot_with_regression(x, y, slope, intercept, title=None, x_label=None, y_label=None, figsize=(800, 600), footnote=None):
    # Calculate the regression line based on provided slope and intercept
    regression_line = slope * x + intercept
    
    # Create the scatter plot
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=x, y=y,
        mode='markers',
        name='Data Points',
        marker=dict(color='grey')
    ))
    
    # Add the regression line
    fig.add_trace(go.Scatter(
        x=x, y=regression_line,
        mode='lines',
        name='Regression Line',
        line=dict(color='black')
    ))
    
    # Update the layout to remove spines, add dashed gridlines, and use neutral colors
    fig.update_layout(
        title=title,
        xaxis_title=x_label,
        yaxis_title=y_label,
        font=dict(family="SF Mono", color='black'),
        xaxis=dict(
            showline=False,
            showgrid=True,
            gridcolor='lightgrey',
            gridwidth=1,
            zeroline=False,
            showticklabels=True
        ),
        yaxis=dict(
            showline=False,
            showgrid=True,
            gridcolor='lightgrey',
            gridwidth=1,
            zeroline=False,
            showticklabels=True
        ),
        plot_bgcolor='white',
        width=figsize[0],
        height=figsize[1],
        margin=dict(l=50, r=50, t=50, b=100)  # Adjust margins to make space for the footnote
    )
    
    # Update the gridlines to be dashed
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey', griddash='dash')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey', griddash='dash')
    
    # Add footnote if provided
    if footnote:
        fig.add_annotation(
            text=footnote,
            xref="paper", yref="paper",
            x=0, y=-0.15,  # Position the footnote inside the visible area
            showarrow=False,
            font=dict(family="SF Mono", size=12, color="black"),
            align="left"
        )
    
    # Show the plot
    fig.show()


