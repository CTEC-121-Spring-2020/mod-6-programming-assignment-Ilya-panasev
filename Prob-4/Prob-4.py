# Module 7
#   Programming Assignment 10
#     Prob-4.py

# Ilya Panasevich

def main():
    rate = float(input("Please enter your interest rate: "))
    file = open('Prob-4/balances.txt','r')
    data = file.readline()
    
    while(data):
        print(data)
        data = file.readline()
main()    