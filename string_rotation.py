# This program rotates a given string letters by letters
# for example:
# input: "Tie"
# Output: ["ieT", "eTi"]

def _rotate_left_once(characters):
    return [
        characters[(index + 1) % len(characters)]
        for index in range(len(characters))
    ]


def rotate(n):
    a = list(n)
    if len(a) == 0:
        return print([])
    l = []
    for i in range(1, len(a) + 1):
        a = _rotate_left_once(a)
        l += ["".join(a)]
    print(l)


string = str(input())
print("Your input is :", string)
print("The rotation is :")
rotate(string)


# Input : Python
# output :
# The rotation is :
# ['ythonp', 'thonpy', 'honpyt', 'onpyth', 'npytho', 'python']
