#!/bin/python3

import math
import os
import random
import re
import sys


def python_if_else(n):
    if n % 2 == 1:
        return "Weird"
    if n % 2 == 0 and 2 <= n <= 5:
        return "Not Weird"
    if n % 2 == 0 and 6 <= n <= 20:
        return "Weird"
    if n % 2 == 0 and n > 20:
        return "Not Weird"
    return "Weird"

if __name__ == '__main__':
    n = int(input().strip())
    print(python_if_else(n))
