def split_camel_case(s):
    result = []
    current_word = ""

    for char in s:
        if char.isupper() and current_word:
            result.append(current_word)
            current_word = char
        else:
            current_word += char

    if current_word:
        result.append(current_word)

    return " ".join(result)