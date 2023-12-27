def rgb(r, g, b):
    # Ensure that values are within the valid range (0 - 255)
    r = max(0, min(255, round(r)))
    g = max(0, min(255, round(g)))
    b = max(0, min(255, round(b)))

    # Convert decimal values to hexadecimal and format the result
    hex_value = '{:02X}{:02X}{:02X}'.format(r, g, b)

    return hex_value