from publisher import pub
from subscriber import func
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def pub_sub():
    pub()
    print("done with publishing")
    func()
    print("done with subscriber")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pub_sub()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
