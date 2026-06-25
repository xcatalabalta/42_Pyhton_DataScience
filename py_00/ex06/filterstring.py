import sys
from ft_filter import ft_filter
# Add the path to the ex05 directory to import building.py
sys.path.append("../ex05")
from building import is_punt  # noqa: E402
"""
# noqa: E402
skip the E402 check on this line to remove the warning about
module level import not at top of file
"""


def is_good(c) -> bool:
    """
    Check a character is not a punctuation mark
    but is printable.
    """
    return not is_punt(c) and c.isprintable()


def main():
    """Filter words from a string by minimum length, removing punctuation."""
    sys.tracebacklimit = 0
    assert len(sys.argv) == 3, "the arguments are bad"
    assert sys.argv[2].isdigit(), "the arguments are bad"
    filtered_string = ft_filter(is_good, sys.argv[1])
    filtered_string = ''.join(filtered_string)
    filtered_string = filtered_string.split()
    filtered_string = ft_filter(lambda word: len(word) >= int(sys.argv[2]),
                                filtered_string)
    print(filtered_string)


if __name__ == "__main__":
    main()
