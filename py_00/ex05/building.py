import sys


def is_punt(c) -> bool:
    """
    Check if a character is a punctuation mark.
    """
    return c in ['.', ',', ';', ':', '!', '?']


def text_analyzer(text: str) -> dict:
    """
    Analyze the given text and return a dictionary with counts of various elements.
    """
    result = {
        'characters': len(text),
        'words': len(text.split()),
        'lines': text.count('\n') + 1,
        'punctuation': sum(1 for c in text if is_punt(c)),
        'uppercase': sum(1 for c in text if c.isupper()),
        'lowercase': sum(1 for c in text if c.islower())
    }
    return result
