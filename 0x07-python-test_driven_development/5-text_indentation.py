#!/usr/bin/python3

"""prints a text with 2 new lines"""

def text_indentation(text):
    """a function that prints 2 new lines"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # remove leading and trailing whitespace
    text = text.strip()

    # iterate over the characters in the text
    for i, char in enumerate(text):
        # print the current character
        print(char, end="")

        # if the current character is a period, question mark, or colon, print 2 newlines
        if char in [".", "?", ":"]:
            print("\n\n", end="")

        # if the current character is a space, check the next character
        elif char == " ":
            # if the next character is a period, question mark, or colon, skip the space
            if i < len(text) - 1 and text[i+1] in [".", "?", ":"]:
                continue

            # otherwise, print the space
            print(" ", end="")

    # print a newline at the end of the text
    print()
