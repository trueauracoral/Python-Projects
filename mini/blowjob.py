import sys
import random

def main():
    if len(sys.argv) < 2:
        sys.exit("Please input an argument")
    try:
        num = int(sys.argv[1])
    except:
        sys.exit("Please input your argument as an integer")
    
    first = random.randint(0, 100)
    second = random.randint(0, 10)
    arithmetic = random.choice(["+", "-"])
    if arithmetic == "+":
        answer = first + second
        text = f"Lmaoo can't even add {first} and {second} together"
    elif arithmetic == "-":
        answer = first - second
        text = f"Lmaoo can't even subtract {first} from {second}"
    question = input(f"What is {first} {arithmetic} {second}: ")
    try:
        question = int(question)
    except:
        sys.exit("Please input an integer")
    if question != answer:
        sys.exit(text)

    print(f"c{'='*num}3")
    

if __name__ == "__main__":
    main()