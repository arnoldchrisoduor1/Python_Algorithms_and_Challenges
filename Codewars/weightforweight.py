def order_weight(strng):
    # Split the input string into a list of weights
    weights = strng.split()

    # Define a custom sorting function based on weight calculation
    def custom_sort(weight):
        weight_sum = sum(int(digit) for digit in weight)
        return (weight_sum, weight)

    # Sort the weights using the custom sorting function
    sorted_weights = sorted(weights, key=custom_sort)

    # Join the sorted weights into a string
    result = " ".join(sorted_weights)
    
    return result
