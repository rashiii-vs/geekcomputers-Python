
import pyttsx3
import os


def friday(x):
    """
    Check whether a command asks to open or run Notepad.

    Worked example 1: Smallest matching input

    >>> command = "runnotepad"
    >>> has_notepad = ("notepad" in command) or ("Notepad" in command)
    >>> has_action = ("open" in command) or ("run" in command) or ("Open" in command) or ("Run" in command)
    >>> (has_notepad, has_action, friday(command))
    (True, True, True)

    Worked example 2: Ordinary input

    >>> command = "please run Notepad"
    >>> has_notepad = ("notepad" in command) or ("Notepad" in command)
    >>> has_action = ("open" in command) or ("run" in command) or ("Open" in command) or ("Run" in command)
    >>> (has_notepad, has_action, friday(command))
    (True, True, True)

    Worked example 3: Non-matching input

    >>> friday("open calculator")
    False
    """
    has_notepad = ("notepad" in x) or ("Notepad" in x)
    has_action = ("open" in x) or ("run" in x) or ("Open" in x) or ("Run" in x)

    return has_notepad and has_action


def main():
    var = 1

    while var > 0:
        pyttsx3.speak("How can I help you Sir")
        print("How can I help you Sir : ", end="")
        x = input()

        if friday(x):
            pyttsx3.speak("Here it is , sir")
            os.system("notepad")

        print("anything more")


if __name__ == "__main__":
    main()

