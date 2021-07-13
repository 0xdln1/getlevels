#!/usr/bin/python3

import sys
import os
import argparse

def parser_error(self):
    print("\nUsage: python " + sys.argv[0] + " [Options] use -h for help\n")
    print("         	Coded With <3 by @0xdln\n")
    sys.exit()

def parse_args():
    parser = argparse.ArgumentParser(epilog='\tExample: \r\npython ' + sys.argv[0] + " -f [FILE] -l [LEVEL]")
    parser.error = parser_error
    parser._optionals.title = "OPTIONS"
    parser.add_argument('-f', '--file', required=True)
    parser.add_argument('-l', '--level', required=True)
    args = parser.parse_args()
    return args

str1 = '\w+'
str2 = '\.+'

def concat_():
    str_main = str1+str2
    return str_main

def main():
    args = parse_args()
    num = int(args.level)
    f = args.file
    i=0
    str_main = ''
    while i < num:
        str_main += concat_()
        i+=1

    grep_word = "grep -Po \"("+str_main+"\w+)$\""
    os.system("cat "+f+" | "+grep_word+" | sort -u ")

if __name__ == '__main__':
    main()