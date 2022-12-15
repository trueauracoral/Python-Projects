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

def main():
    args = parse_arguments()
    if args.questions:
        questions = args.questions
        wrong = args.wrong
        correct = questions - wrong
        result = round((correct / questions) * 100, 2)
        if not args.decimal:
            result = round(result)
        print(f"{correct}/{questions} = {result}%")
        if args.chart:
            print("Wrong:\tGrade:")
            for i in list(range(1, questions+1)):
                print(f"{i}\t{round(((questions - i) / questions) * 100)}")
    else:
        sys.exit("Enter -q/-questions for the amount of questions. Please read the -h/--help.")

if __name__ == "__main__":
    main()