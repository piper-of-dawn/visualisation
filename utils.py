def hex_to_rgba(hex_color, alpha):
    """
    Convert a HEX color to an RGBA color string.

    Parameters:
    hex_color (str): The HEX color string (e.g., '#RRGGBB' or '#RRGGBBAA').
    alpha (float): The alpha (opacity) value (0.0 to 1.0). Default is 1.0.

    Returns:
    str: The RGBA color string (e.g., 'rgba(255, 0, 0, 0.5)').
    """
    # Remove the hash symbol if present
    hex_color = hex_color.lstrip('#')

    # Convert hex to RGB
    if len(hex_color) == 6:
        r, g, b = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
    elif len(hex_color) == 8:
        r, g, b, a = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16), int(hex_color[6:8], 16)
        # alpha = a / 255.0
    else:
        raise ValueError("HEX color must be in the format '#RRGGBB' or '#RRGGBBAA'.")

    # Return RGBA string
    return f'rgba({r}, {g}, {b}, {alpha})'
