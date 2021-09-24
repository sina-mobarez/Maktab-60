#! /usr/bin/python3.8

import argparse

parser = argparse.ArgumentParser(description='This script is a simple calculator')
parser.add_argument('num1', help='just a number, first', type=float)
parser.add_argument('num2', help='just a number, second', type=float)
parser.add_argument('-o', '--operation', action='store_true', help='operator for numbers')
parser.add_argument('operator', help='"+", "-", "/", "x" >>> just enter one of them', type=str)
args = parser.parse_args()
try:
    if args.operator == "+":
        print(float(args.num1) + float(args.num2))
    elif args.operator == "-":
        print(float(args.num1) - float(args.num2))
    elif args.operator == "/":
        print(float(args.num1) / float(args.num2))
    elif args.operator == "x":
        print(float(args.num1) * float(args.num2))
except ValueError:
    print(" You don't enter enough inputs ")
