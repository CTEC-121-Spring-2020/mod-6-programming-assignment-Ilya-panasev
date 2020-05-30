# Module 7
#   Programming Assignment 10
#     Prob-2.py

# Ilya Panasevich


def main():
    file = open('Prob-2/Prob-2-Input.txt','r')
    data = file.readlines()
    while(data):
        print(data)
        data = file.readlines()
    
    while(data):
        num = data.split()
        print(num)
main()    