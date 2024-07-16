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
