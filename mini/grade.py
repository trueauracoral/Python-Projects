#!/usr/bin/env python
import argparse
import sys

wrong = 0
questions = 0

def parse_arguments():
    parser = argparse.ArgumentParser(description='pass.py')
    parser.add_argument('-q', '--questions', type=int, metavar='NUMBER', help='Number of questions')
    parser.add_argument('-w', '--wrong', type=int, metavar='NUMBER', help='Number of missed questions')
    parser.add_argument('-d', '--decimal', action="store_true", default=False, help='Output decimal')
    parser.add_argument('-c', '--chart', action="store_true", default=False, help='Output chart')
    args = parser.parse_args()
 
    return args

def calculate(wrong, questions, args):
    correct = questions - wrong
    result = round((correct / questions) * 100, 2)
    if not args.decimal:
        result = round(result)
    return result

def main():
    args = parse_arguments()
    if args.questions:
        print(f"{args.questions - args.wrong}/{args.questions} = {calculate(args.wrong, args.questions, args)}%")
        if args.chart:
            print("Wrong:\tGrade:")
            for i in list(range(1, args.questions+1)):
                #print(f"{i}\t{round(((questions - i) / questions) * 100)}")
                print(f"{i}\t{calculate(i, args.questions, args)}")
    else:
        sys.exit("Enter -q/-questions for the amount of questions. Please read the -h/--help.")

if __name__ == "__main__":
    main()