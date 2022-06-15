#!/usr/bin/env python
text = input("What text? ")
icon = '''
             \\        ___
              \\   \\__| o \\
                  /   \\  |
                       | |     o
                     __| |__  //
                    |_______|//
                    \\_______//

'''

"""-----------No package repos?-----------"""
num = 30
num2 = len(text)
final = int((num-num2)*0.5)
print("-"*final+text+"-"*final)
print(icon)
