#!/usr/bin/env python
import csv

def readCSV(file):
    #https://www.digitalocean.com/community/tutorials/parse-csv-files-in-python#parsing-a-csv-file-in-python
    with open(file, 'r', encoding='utf-8') as csv_file:
        parsedCSV = csv.reader(csv_file)

        jsonDict = []
        listofnames = []
        for row in parsedCSV:
            if (row == [] or row == None):
                continue
            url = row[1]
            name = row[2]
            entry = {"name": name, "url": url}
            jsonDict.append(name)
    return jsonDict

account1csv = readCSV("subscriptions.csv")
account2csv = readCSV("subscriptions2.csv")

def setFormatter(setList, symbol):
    newList = []
    for val in setList:
        newList.append(f"{symbol} {val}")
    return newList

#https://www.geeksforgeeks.org/python-find-missing-additional-values-two-lists/
print("Account 1")
acc1dif = set(account2csv).difference(account1csv)
acc1d = setFormatter(acc1dif, "-")
acc1add = set(account1csv).difference(account2csv)
acc1a = setFormatter(acc1dif, "+")

print("\n".join(f"{x}\t\t|\t{y}" for x,y in zip(acc1d, acc1a)))

print()

print("Account 2")
acc2dif = set(account1csv).difference(account2csv)
setFormatter(acc2dif, "-")
acc2add = set(account2csv).difference(account1csv)
setFormatter(acc2dif, "+")

