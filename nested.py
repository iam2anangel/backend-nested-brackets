#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = "__iam2anangel__"  # Jen Browning

import sys


def check_nested_brackets(filename):
    """setting up the file"""
    with open(filename, 'r+') as f:
        exp_list = f.read().split('\n')
    result = []

    for expressions in exp_list:
        result.append(check_brackets(expressions))
    return result


def check_brackets(expressions):
    """checking to see both brackets are in input"""
    stack = []
    brackets = {'(': ')', '[': ']', '{': '}', '<': '>', '(*': '*)'}
    count = 0

    for index, item in enumerate(expressions):
        count = index + 1
        if item in brackets:
            stack.append(item)
        elif item in brackets.values():
            open_bracket = (new_index for new_index,
                            new_item in brackets.items() if new_item == item)
            if open_bracket and stack[-1] != open_bracket:
                return "no" + str(index)
            else:
                brackets.pop()
        if len(stack) > 0:
            return "no" + str(count+1)
        return "Yes"

# lines = ["(*a++(*)", "(*a{+}*)"]
# openers = ['(*', '(', '{', '[', '<']
# closers =

# # tokenizing a string means splitting it us and compare things within in python


# def main(line):
#     stack = []
#     while line:
#         token = line[0]
#         if line.startswith('(*')
#         token = '(*'
#         elif line.startswith('*)'):
#             token = '*)'

#     if stack:
#         # something not right
#     else:
#         # yay. all openers got matched to closers

#         # do business logic matching openers and closers, push onto stack i fopener found, pop off stack if closer found.
#         #  will need counter to tell us where things went badly and push onto stack if opener found
#         # incrememnt m position index. ex: index +=1

#         # use while loop, should not have any leftovers


#         # how to begin reducing the size of the line
# line = line[len(token):]

# if token in openers:
#     stack.append(token)


def main(args):
    if len(sys.argv) != 2:
        sys.exit(1)
    print(check_nested_brackets(sys.argv[1]))


if __name__ == '__main__':
    main(sys.argv)
