
# user.py

import time


def signup(db):
    
    user_collection = db["user"]
    
    print("-"*70)
    print("{:^60}".format("Sign Up"))
    print("-"*70)
    
    # user_id
    unique_id = False
    
    while not unique_id:
        print("{:^40}".format("User ID"), end="")
        user_id = input()
        
        result = user_collection.count_documents({"user_id" : user_id})
        
        if result == 1:
            print("{:^20}".format("**This ID already exists. Please use another ID!**"))
            print()
            continue
        else:
            unique_id = True
        
    # user_name
    print("{:^40}".format("User Name"), end="")
    user_name = input()
    
    # user_pw
    match_pw =False
    
    while not match_pw:
        print("{:^40}".format("Password"), end="")
        user_pw = input()
    
        print("{:^40}".format("Password"), end="")
        user_pw2 = input()
        
        if user_pw != user_pw2:
            print("{:^30}".format("**No matching with above password. Please write again!**"))
            print()
            continue
        else:
            match_pw = True
            
    try:
        user_doc = user_collection.insert_one(
            {"user_id":user_id, "user_name":user_name, "pw":user_pw, 
             "status_message":"Hello, world!", "Followers":0, "Following":0})
        print("-"*70)
        print("{:^60}".format("Success to Sign Up!"))
        print()
        print("{:>40}".format("Wait 3 seconds..."))
        time.sleep(3)
        
    except Exception as e:
        print("-"*70)
        print("{:^60}".format("***Try again. Fail to Sign Up***"))

        
def signin(db):
    
    user_collection = db["user"]
    
    print("-"*70)
    print("{:^60}".format("Sign In"))
    print("-"*70)
    
    info_match = False
    
    while not info_match:
        print("{:^40}".format("User ID"), end="")
        user_id = input()
        print("{:^40}".format("Password"), end="")
        user_pw = input()
    
        result_id = user_collection.count_documents({"user_id" : user_id})
        
        if result_id == 0:
            print("{:>20}".format("***ID does not exist. Try again!***"))
            print()
            continue
        
        result = user_collection.find_one({"user_id": user_id})
        result_pw = result["pw"]
        result_name = result["user_name"]
    
        if str(result_pw) != user_pw:
            print("{:>20}".format("***Wrong password. Try again!***"))
            print()
            continue
        else:
            info_match = True
            
    print("-"*70)
    print("{:>30}".format("Welcome, ")+result_name+" !")
    print("{:>40}".format("Wait 2 seconds..."))
    time.sleep(2)
    userpage(db, user_id)
    
    
def userpage(db, user_id):
    
    print("="*70)
    print("{:^60}".format("Welcome to Monstagram!"))
    print("-"*70)
    print("{:^60}".format("1. My status"))
    print("{:^60}".format("2. News feed"))
    print("{:^60}".format("3. Wall     "))
    print("{:^60}".format("4. Post     "))
    print("{:^60}".format("5. Follow   "))
    print("{:^60}".format("6. Unfollow "))
    print("{:^60}".format("7. Logout   "))
    print("-"*70)
    
    page_num = 1
    
    while page_num:
        print("{:^40}".format("Select number you want to see: "), end="")
        page_num = eval(input())
    
        if page_num == 1:
            mystatus(db, user_id)
        elif page_num == 2:
            pass
        elif page_num == 3:
            pass
        elif page_num == 4:
            pass
        elif page_num == 5:
            pass
        elif page_num == 6:
            pass
        elif page_num == 7:
            print()
            print("{:^60}".format("### Bye! ###"))
            break
        else:
            print("{:^40}".format("***Please select in [1, 2, 3, 4, 5]***"))
            print()
            page_num = True
            

            
def mystatus(db, user_id):

    user_collection = db["user"]
    
    result = user_collection.find_one({"user_id": user_id})
    result_msg = result["status_message"]
    result_flwr = result["Followers"]
    result_flwn = result["Following"]
    
    print("="*70)
    print("{:^60}".format("My Status"))
    print("-"*70)
    print("{:>20}".format("# My Profile"))
    print("{:>30}".format(result_msg))
    print()
    print("{:>20}".format("# Followers:"),result_flwr)
    print()
    print("{:>20}".format("# Following:"),result_flwn)
    print()
    print("-"*70)
    print("{:^60}".format("[If you want to go back, press enter key.]"))
    exit_page = input()
    
