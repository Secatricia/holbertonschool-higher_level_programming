#!/usr/bin/python3

"""class MyList that inherits from list"""


class MyList(list):
    """MyList that inherits from list"""
    def __init__(self, list_va=[]):
        """Init"""
        self.list = list_va

    """Create function that print"""
    def print_sorted(self):
        """print list"""
        print("{}".format(sorted(self)))
