#!/usr/bin/env python3
import sys


def sum(tall1=0, tall2=0, tall3=0):
    print("Summen er:", tall1 + tall2 + tall3)


def main():
    if len(sys.argv) == 2:
        sum(sys.argv[1])
    elif len(sys.argv) == 3:
        sum(int(sys.argv[1]), int(sys.argv[2]))
    elif len(sys.argv) == 4:
        sum(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
    else:
        sum()


if __name__ == '__main__':
    main()
