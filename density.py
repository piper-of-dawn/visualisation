def plot_kde_with_shapiro(arrays, title=None, x_label=None, y_label=None, figsize=(800, 600)):
    # Create the Plotly figure
    fig = go.Figure()
    
    # Define a color map with muted tones
    colormap = cm.get_cmap('tab20c', len(arrays))
    
    for i, array in enumerate(arrays):
        # Perform Shapiro-Wilk test
        shapiro_stat, shapiro_p_value = stats.shapiro(array)
        shapiro_outcome = 'normal' if shapiro_p_value > 0.05 else 'not normal'
        
        # Generate kernel density estimate using scipy
        kde = stats.gaussian_kde(array)
        x_values = np.linspace(min(array), max(array), 1000)
        y_values = kde(x_values)
        
        # Convert color from colormap to rgba with transparency
        rgba_color = mcolors.to_rgba(colormap(i), alpha=0.5)
        rgba_color_str = f'rgba({int(rgba_color[0]*255)}, {int(rgba_color[1]*255)}, {int(rgba_color[2]*255)}, {rgba_color[3]})'
        
        # Add the KDE plot with translucent fill
        fig.add_trace(go.Scatter(
            x=x_values, y=y_values,
            mode='lines',
            fill='tozeroy',
            fillcolor=rgba_color_str,
            line=dict(color=rgba_color_str),
            name=f'Dataset {i+1}'
        ))
        
        # Calculate statistics
        mean_val = np.mean(array)
        std_val = np.std(array)
        skewness_val = stats.skew(array)
        kurtosis_val = stats.kurtosis(array)
        
        # Format footnote text with statistics
        footnote_text = f'Dataset {i+1}: Shapiro-Wilk test p-value: {shapiro_p_value:.4f} ({shapiro_outcome})<br>' + \
                        f'Mean: {mean_val:.4f}, Std: {std_val:.4f}, Skewness: {skewness_val:.4f}, Kurtosis: {kurtosis_val:.4f}'
        
        # Add footnote with Shapiro-Wilk test results and statistics
        fig.add_annotation(
            text=footnote_text,
            xref="paper", yref="paper",
            x=0, y=-0.1 - i*0.05,  # Position the footnote inside the visible area
            showarrow=False,
            font=dict(family="SF Mono, monospace", size=12, color="black"),
            align="left"
        )
    
    # Update the layout to remove spines, add dashed gridlines, and use neutral colors
    fig.update_layout(
        title=title,
        xaxis_title=x_label,
        yaxis_title=y_label,
        font=dict(family="SF Mono, monospace", color='black'),
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
        margin=dict(l=50, r=50, t=50, b=100 + len(arrays)*20)  # Adjust margins to make space for the footnote
    )
    
    # Update the gridlines to be dashed
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey', griddash='dash')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey', griddash='dash')
    
    # Show the plot
    fig.show()

