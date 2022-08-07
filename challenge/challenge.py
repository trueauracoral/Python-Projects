def find_duplicate(string):
    values = list(string)
    for i, value in enumerate(values):
        values[i] = values[i].lower()
    duplicates = []
    for i, letter in enumerate(values):
        if letter == " ":
            pass
        elif i == len(values)-1:
            pass
        elif values[i] == values[i+1]:
            duplicates.append(letter)
    if len(duplicates) == 0:
        return "No duplicates found."
    elif len(duplicates) == 1:
        return f"{duplicates[0]} is the duplicate character."
    else:
        return f"{', '.join(duplicates)[:-1]} and {duplicates[-1]} are duplicate characters.".replace("  ", " ")

input_string = input("Which string do you want to find duplicates of? ")
print(find_duplicate(input_string))
