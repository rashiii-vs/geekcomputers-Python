
def check_condition(user):
    if user == 1:
        print("in first if")
    elif user == 2:
        print("in second if")
    elif user == 3:
        print("in third if")
    else:
        print("Enter numbers b/w the range of 1-3")


def main():
    while True:
        try:
            user = int(input("enter any number b/w 1-3\n"))
            check_condition(user)
        except ValueError:
            print("enter only digits")


if __name__ == "__main__":
    main()
