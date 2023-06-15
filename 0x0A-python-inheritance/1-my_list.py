#!/usr/bin/python3
''' Module: 1-my_list
'''


class MyList(list):
    ''' Represents a MyList
    '''

    def print_sorted(self):
        '''
        prints the list, but sorted
        '''
        sorted_list = sorted(self)
        for element in sorted_list:
            print(element)
