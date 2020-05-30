# Module 7
#   Programming Assignment 10
#     Prob-3.py

# Ilya Panasevich

def main():
    
    # do not change the while loop definition below
    sum = 0
    while True:
        number = float(input("Enter a positive number to add (negative to quit): "))
        if number >= 0:
            sum = sum + number
        else:
            break
    print("The sum of the numbers you entered is", sum)     

main()    