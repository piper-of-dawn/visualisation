def plot_acf_pacf_side_by_side(data, lags=None, padding=0.1, title='Autocorrelation and Partial Autocorrelation Functions'):
    from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
    from statsmodels.stats.stattools import durbin_watson
    fig, ax = plt.subplots(1, 2, figsize=(12, 4))

    # ACF plot
    plot_acf(data, lags=lags, ax=ax[0], color='gray')
    ax[0].set_title('Autocorrelation Function (ACF)')

    # PACF plot
    plot_pacf(data, lags=lags, ax=ax[1], color='gray')
    ax[1].set_title('Partial Autocorrelation Function (PACF)')
    if lags is not None:
        ax[0].set_xlim(0, lags)
        ax[1].set_xlim(0, lags)
    else:
        ax[0].set_xlim(0, len(data) // 2)
        ax[1].set_xlim(0, len(data) // 2)
    # Remove spines from both x and y axes
    sns.despine(ax=ax[0], left=True, right=True, top=True, bottom=True)
    sns.despine(ax=ax[1], left=True, right=True, top=True, bottom=True)

    # Adjust layout with padding
    plt.subplots_adjust(wspace=padding)
    # Perform Durbin-Watson test
    dw_stat = durbin_watson(data)
    dw_conclusion = f"Durbin-Watson Test: statistic = {dw_stat:.4f}."

    # Perform ADF test
    adf_result = adf_test(data, 0.05)
    # Add footnote
    fig.text(0.5, -0.05, f"{adf_result}\n{dw_conclusion}", ha='center', fontsize=10, color='gray')

    plt.suptitle(title, y=1.02, fontsize=14, color='black',fontweight= 'bold')
    # Show the plots
    return fig

def adf_test(series, alpha=0.05):
    from statsmodels.tsa.stattools import adfuller
    """
    Perform Augmented Dickey-Fuller (ADF) test for stationarity.

    Parameters:
    - series (pd.Series): Time series data.
    - alpha (float): Significance level for the test.

    Returns:
    - ADF test results and conclusion.
    """
    mask = np.logical_not(np.isnan(series))
# Use this mask to select non-NaN values
    series = series[mask]
    result = adfuller(series, autolag='AIC')
    p_value = result[1]

    if p_value <= alpha:
        return f"Result: Reject the null hypothesis at {alpha} significance level (p-value: {round(p_value,2)}). The time series is likely stationary."

    else:
        return f"Result: Fail to reject the null hypothesis at {alpha} significance level (p-value: {round(p_value,2)}). The time series is likely non-stationary."





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

# Example usage:
x = np.random.rand(50)
y = 2 * x + np.random.randn(50) * 0.1

# Provided slope and intercept
slope = 2
intercept = 0

plot_with_regression(
    x, y, slope, intercept,
    title='Sample Plot',
    x_label='X Axis',
    y_label='Y Axis',
    figsize=(1200, 800),
    footnote='This is a sample footnote.'
)

