# main.py

from user import *
from pymongo import MongoClient
client = MongoClient()
db = client["sns"]

def mainpage(db):
    
    select_num = 1
    
    while select_num:
        print("-"*70)
        print("{:^60}".format("\"Hello, I'm Monstagram.\""))
        print("-"*70)
        print("{:^60}".format("1. Sign Up"))
        print("{:^60}".format("2. Sign In"))
        print("{:^60}".format("3. Exit   "))
        print("-"*70)
        print("{:^40}".format("Select number in [1, 2, 3]:"), end="")
        select_num = eval(input())
    
        if select_num == 1:
            print()
            signup(db)
        elif select_num == 2:
            print()
            select_num = 0
            signin(db)
        elif select_num == 3:
            print()
            print("{:^60}".format("### Bye! ###"))
            exit()
                  

if __name__ == '__main__':
    while True:
        mainpage(db)
                  
