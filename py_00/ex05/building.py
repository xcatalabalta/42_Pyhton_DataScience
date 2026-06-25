import sys


def is_punt(c) -> bool:
    """
    Check if a character is a punctuation mark.
    """
    return c in ['.', ',', ';', ':', '!', '?']


def text_analyzer(text: str) -> dict:
    """
    Analyze a text and return a dictionary with counts of various elements.
    """
    result = {
        'characters': len(text),
        'words': len(text.split()),
        'lines': text.count('\n') + 1,
        'punctuation': sum(1 for c in text if is_punt(c)),
        'uppercase': sum(1 for c in text if c.isupper()),
        'lowercase': sum(1 for c in text if c.islower()),
        'spaces': sum(1 for c in text if c.isspace()),
        'digits': sum(1 for c in text if c.isdigit())
    }
    return result


def main():
    """
    Main function to handle command-line input and output the analysis.
    """

    sys.tracebacklimit = 0
    argc = len(sys.argv)

    if argc > 2:
        raise AssertionError("Too many arguments") from None

    if argc == 1 or len(sys.argv[1]) == 0:
        print("Enter text to analyze: (Press ctrl+d to submit)")
        text = sys.stdin.read()
    else:
        text = sys.argv[1]

    analysis = text_analyzer(text)

    a = len(text) - 1
    if a >= 0 and text[a] != '\n':
        print()

    print(f"The text contains {analysis['characters']} characters:")
    print(f"{analysis['uppercase']} uppercase letters")
    print(f"{analysis['lowercase']} lowercase letters")
    print(f"{analysis['punctuation']} punctuation marks")
    print(f"{analysis['spaces']} spaces")
    print(f"{analysis['digits']} digits")


if __name__ == "__main__":
    main()
