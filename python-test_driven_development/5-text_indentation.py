#!/usr/bin/python3

"""
Contain a function that prints a text with 2 new lines after a symbol
"""

def text_indentation(text):
    
    """
    prints a text with 2 new lines after one of these characters: ., ? or :

    Args:
    text (str): a long text with symbol.

    Raises:
    TypeError: if text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    symbols = {'.', '?', ':'}
    new_text = ""
    i = 0
    while i < len(text):
        new_text += text[i]
        if text[i] in symbols:
            new_text += "\n\n"
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
    print(new_text, end="")
    