#!/usr/bin/env python3
import sys
import textwrap
import random
import json

snake = """
         \\        ___
          \\   \\__| o \\
              /   \\  |
                   | |     o
                 __| |__  //
                |_______|//
                \\_______//
"""
cow = """
        \\   ^__^
         \\  (oo)\\_______
            (__)\\       )\\/\\
                ||----w |
                ||     ||
"""
tux = """
       \\
        \\
            .--.
           |o_o |
           |:_/ |
          //   \\ \\
         (|     | )
        /'\\_   _/`\\
        \\___)=(___/
"""

fortunes = """
A body makes his own luck, be it good or bad. - unknown
Change yourself and fortune will change. - Portuguese (on fortune)
Good things come when you least expect them. - unknown
It is possible to have too much of a good thing. - Aesop
Lightning never strikes the same place twice. - P. H. Myers
May the wind be always at your back. - unknown
Sum up at night what thou hast done by day. - George Herbert
The new boat will find the old stones. - Estonian (on perversity)
Venture a small fish to catch a great one. - English (on buying and selling)
When fortune calls, offer her a chair. - Yiddish (on fortune)
When fortune turns against you, even jelly breaks your teeth. - Iranian
Diligence is the mother of good fortune.- Benjamin Disraeli
A wise man turns chance into good fortune.- Thomas Fuller
Fortune, which has a great deal of power in other matters but especially in war, can bring about great changes in a situation through very slight forces.- Julius Caesar
Fortune favors the prepared mind. - Louis Pasteur
Come what may, all bad fortune is to be conquered by endurance.- Virgil
The day of fortune is like a harvest day, We must be busy when the corn is ripe.- Goethe
I`ve seen the smiling of Fortune beguiling, I`ve felt all its favours and found its decay.- Alison Cockburn 
There is frequently a poison in fortune`s gifts.- Edward Counsel
The loss of fortune to a true man is but the trumpet challenge to renewed exertion, not the thunder stroke of destruction.- E.H. Chapin
Fortune may raise up or abuse the ordinary mortal, but the sage and the soldier should have minds beyond her control.- Sir Walter Scott
We make a goddess of Fortune ... and place her in the highest heaven. But it is not fortune that is exalted and powerful, but we ourselves that are abject and weak.- Charles Caleb Colton
It is madness to make fortune the mistress of events, because by herself she is nothing and is ruled by prudence. - John Dryden
If a man`s fortune does not fit him, it is like the shoe in the story; if too large it trips him up, if too small it pinches him. - Horace
Fortune does not so much change men, as it unmasks them. - Anonymous
Fortune knocks at every man`s door once in a life, but in a good many cases the man is in a neighboring saloon and does not hear her. - Mark Twain
Fortune is like glass--the brighter the glitter, the more easily broken. - Publilius Syrus
Fortune has something of the nature of a woman. If she is too intensely wooed, she commonly goes the further away. - Charles V
He that waits upon fortune, is never sure of a dinner. - Benjamin Franklin
Good fortune and evil fortune come to all things alike in this world of time.- Moasi 
Fortune is a great deceiver. She sells very dear the things she seems to give us. - Vincent Voiture
If a man look sharply and attentively, he shall see Fortune; for though she be blind, yet she is not invisible. - Francis Bacon
Behind every great fortune there is a crime. - Honor de Balzac
Fortune is ever seen accompanying industry. - Oliver Goldsmith
Fortune is the rod of the weak, and the staff of the brave. - James Russell Lowell
Fortune brings in some boats that are not steered.- William Shakespeare
The way of fortune is like the milky way in the sky; which is a number of smaller stars, not seen asunder, but giving light together; so it is a number of little and scarce discerned virtues, or rather faculties and customs, that make men fortunate- Francis Bacon
We should manage our fortune as we do our health - enjoy it when good, be patient when it is bad, and never apply violent remedies except in an extreme necessity- Francois de la Rochefoucauld
No one is satisfied with his fortune, nor dissatisfied with his intellect- Antoinette Deshoulieres
Fortune and misfortune are two buckets in the same well- German Proverb
The power of fortune is confessed only by the miserable; for the happy impute all their success to prudence and merit- Jonathan Swift
A great fortune is a great slavery.- Seneca
Fortune sells her wares; she never gives them. In some form or other, we pay for her favors; or we go empty away. - Amelia E. Barr 
No man`s fortune can be an end worthy of his being. - Francis Bacon
The brave man carves out his fortune and every man is the son of his own works. - Miguel de Cervantes
Friends and acquaintances are the surest passport to fortune. - Arthur Schopenhauer
We always take credit for the good and attribute the bad to fortune. - Charles Kuralt
To attract good fortune, spend a new penny on an old friend, share an old pleasure with a new friend and lift up the heart of a true friend by writing his name on the wings of a dragon. - Proverb
Fortune, the great commandress of the world, Hath diverse ways to advance her followers: To some she gives honor without deserving; To other some, deserving without honor; Some wit, some wealth,--and some, wit without wealth; Some wealth without wit; some nor wit nor wealth. - George Chapman
On what a slender threads our fortune and our life hang!- Alexandre Dumas
That is a dream also, only he has remained asleep, while you have awakened and who knows which of you is the most fortunate?- Alexandre Dumas
All fortune is good fortune, for it either rewards, disciplines, amends, or punishes, and so is either useful or just.- Boethius
Love, like Fortune, favors the bold.- E.A. Bucchianeri
This is your karma. You do not understand now, but you will understand later. The source of pain is within your own larger expression of being.- H. Raven Rose
Instead of comparing our lot with that of those who are more fortunate than we are, we should compare it with the lot of the great majority of our fellow men. It then appears that we are among the privileged.- Helen Keller
I have always believed, and I still believe, that whatever good or bad fortune may come our way we can always give it meaning and transform it into something of value.- Hermann Hesse
You`ll never make a fortune working for the boss man.- Jeannette Walls
Self-education will make you a fortune.- Jim Rohn
I often think how unfairly life`s good fortune is sometimes distributed. - Leo Tolstoy
Diligence is the mother of good fortune.- Miguel de Cervantes Saavedra
Diligence is the mother of good fortune.- Miguel de Cervantes Saavedra
Nadia Scrieva- Ralph Waldo Emerson
"""
fortunes = fortunes.splitlines()

def error():
    print("ERROR: GIVE ME TEXT!")
    quit()
try:
    sys.argv[1]
except:
    error()
if sys.argv[1] == "fortune":
    text = fortunes[random.randint(0,len(fortunes))]
    thing = snake
elif sys.argv[1] == "-r" or sys.argv[1] == "-r" and sys.argv[2] == "fortune":
    rand = random.randint(1,3)
    if rand == 1:
        thing = snake
    if rand == 2:
        thing = cow
    if rand == 3:
        thing = tux
    if sys.argv[1] == "-r" and sys.argv[2] == "fortune":
        text = fortunes[random.randint(0,len(fortunes))]
    else:
        text = ' '.join(sys.argv[2:])
elif sys.argv[1] == "-s":
    thing = snake
    text = ' '.join(sys.argv[2:])
elif sys.argv[1] == "-c":
    thing = cow
    text = ' '.join(sys.argv[2:])
elif sys.argv[1] == "-t":
    thing = tux
    text = ' '.join(sys.argv[2:])
elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
    print("""This is a less feature rewrite of cowsay in python.

python snakesay.py QUERY - make a snake say something

python snakesay.py fortune - make a snake say a random fortune. Requires requests installed.

python snakesay.py -r QUERY - randomly selected a tux, cow or snake will say something
    
python snakesay.py -t QUERY - a tux will say something

python snakesay.py -s QUERY - a snake will say something

python snakesay.py -c QUERY - a cow will say something""")
    quit()
else:
    thing = snake
    text = ' '.join(sys.argv[1:])
    
if text == "":
    error()
dashes = len(text) + 2
if dashes > 30:
    dashes = 30
    print(" " + "-"*dashes)
    text = textwrap.fill(text, dashes-2).split("\n")
    for enter in text:
        stuff = "| " + enter
        length = dashes - len(stuff)
        print(stuff + " "*length+" |")
    print(" " + "-"*dashes)
else:
    print(" " + "-"*dashes)
    print("| " + text + " |")
    print(" " + "-"*dashes)

print(thing)
