def solution(s):
    newstring = ''

    for letter in s:
        if letter.isupper():
            newstring += ' '
        newstring += letter

    return newstring