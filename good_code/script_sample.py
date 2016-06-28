#!/usr/bin/env python

from code_sample import *

import argparse


def complicated_function():

    pass


# Execute this only if we are executed from the command line

if __name__=="__main__":

    this_command = argparse.ArgumentParser("script_sample")

    this_command.add_argument("first",help="This is the first argument", type=float)
    this_command.add_argument("second", help="This is the second argument")
    this_command.add_argument("--param1", help="This is an optional argument",required=True)
    this_command.add_argument("--param2", help="This is an optional argument",required=True)

    args = this_command.parse_args()

    print(args.first)
    print(args.second)
    print(args.param1)
    print(args.param2)



