import sys


def ft_filter(filter_func, iterable):
    """
    Filters elements from an iterable based on a filter function.

    Args:
    filter_func (function):
    A function that takes an element and returns True or False.
    iterable (iterable):
    An iterable (e.g., list, tuple, etc.) to filter.

    Returns:
    list: A list containing elements from the iterable
    for which the filter function returned True.
    """
    if filter_func is None:
        return [item for item in iterable if item]
    return [item for item in iterable if filter_func(item)]


def main():
    """
    Main function to demonstrate the usage of ft_filter with different
    filter functions and iterables.
    """

    sys.tracebacklimit = 0

    def is_not_a(c) -> bool:
        """
        Check if a character is the letter 'a'.
        """
        return c != 'a'

    name = "Catalina"
    filtered_name = ft_filter(is_not_a, name)
    print(f"Filtered name (only non-'a's): {''.join(filtered_name)}")

    test_list = [0, 1, 2, 3, 4, 5, None, '', [], {},
                 False, True, 'Hello', 'World', '', 69.98]
    filtered_list = ft_filter(None, test_list)
    print(f"Filtered list (only truthy values): {filtered_list}")


if __name__ == "__main__":
    main()
