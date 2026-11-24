# Count the number of digits in an integer.

def totaldigits(N):
    """
    Return the number of decimal digits in an integer.
    The minus sign is not counted.

    Let d be the number of decimal digits.
    len() takes O(1) time after string creation.
    Integer-to-decimal conversion may take superlinear time,
    depending on the Python implementation.
    The temporary string requires O(d) space.
    """
    return len(str(abs(N)))


if __name__ == "__main__":
    N = int(input("Enter The number: "))
    print(totaldigits(N))
