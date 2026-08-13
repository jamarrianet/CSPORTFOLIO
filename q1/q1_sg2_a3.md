## CN/NAME : #30 SORIANO, MARRIANE AUDREY F.
## SECTION : BALINGKILAT
## DATE : 08/13/26

CODE : 

while True:
    birth = int(input("What is your birth year?: "))
    if birth >= 1900:
        break
    elif birth < 1900:
        print("Invalid Year, it should not be earlier than 1900")

zodiacs = ["Rat", "Ox", "Tiger","Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog","Pig"]

def chinesezodiac():
    calc = birth-1900
    sign = zodiacs[calc%12]
    print("Your Chinese Zodiac Sign is :", (sign))
chinesezodiac()

or

birth = int(input("What is your birth year?: "))

if birth < 1900:
    print("Invalid Year, it should not be earlier than 1900")
else: 
    zodiacs = ["Rat", "Ox", "Tiger","Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog","Pig"]
    calc = birth-1900
    sign = zodiacs[calc%12]
    print("Your Chinese Zodiac Sign is :", (sign))
