def split_string_into_pairs(input_string):
    # If the length is odd, add an underscore to make it even
    if len(input_string) % 2 != 0:
        input_string += '_'
    
    # Use list comprehension to create pairs
    return [input_string[i:i + 2] for i in range(0, len(input_string), 2)]