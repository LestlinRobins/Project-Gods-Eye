import subprocess
from itertools import permutations

def getListsOfUsernames(name):
    usernames=[]
    name_parts = name.lower().split()
    for i in range(1, len(name_parts) + 1):
        for combo in permutations(name_parts, i):
            usernames.append(''.join(combo))
            usernames.append('_'.join(combo))
            usernames.append('-'.join(combo))
            usernames.append('.'.join(combo))
            usernames.append(''.join([part.capitalize() for part in combo]))
            usernames.append('_'.join([part.capitalize() for part in combo]))
            usernames.append('-'.join([part.capitalize() for part in combo]))
            usernames.append('.'.join([part.capitalize() for part in combo]))
        usernames.sort(key=lambda x: (not '_' in x, x.islower(), x))
        usernames = list(set(usernames))
    return usernames

def run_sherlock(username):
    result = subprocess.run(['python', '../sherlock/sherlock_project/sherlock.py', username], capture_output=True, text=True)
    print(result.stdout)

def run_what(text):
    result = subprocess.run(['python', '../what/what.py', text], capture_output=True, text=True)
    print(result.stdout)

print("""
 GGGGG    OOOOO    DDDD    '  SSSSS       EEEEE   Y     Y  EEEEE
G        O     O   D   D     S            E         Y Y    E
G    GG  O     O   D    D     SSSSS       EEEE       Y     EEEE
G     G  O     O   D   D           S      E          Y     E
 GGGG     OOOOO    DDDD       SSSSS       EEEEE      Y     EEEEE                                                                                             
""")
def display_menu():
    print("Select the information you want to provide (enter numbers separated by commas):")
    print("1. Name")
    print("2. Social Media Username")
    print("3. Birthday")
    print("4. House Name")
    print("5. Email Address")
    print("6. Phone Number")
    print("7. Address")
    print("8. Occupation")
    print("9. Favorite Color")

display_menu()
choices = input("Enter your choices: ").split(',')

user_info = {}
if '1' in choices:
    user_info['name'] = input("Enter the name: ")
if '2' in choices:
    user_info['social_media_username'] = input("Enter the social media username: ")
if '3' in choices:
    user_info['birthday'] = input("Enter the birthday: ")
if '4' in choices:
    user_info['house_name'] = input("Enter the house name: ")
if '5' in choices:
    user_info['email_address'] = input("Enter the email address: ")
if '6' in choices:
    user_info['phone_number'] = input("Enter the phone number: ")
if '7' in choices:
    user_info['address'] = input("Enter the address: ")
if '8' in choices:
    user_info['occupation'] = input("Enter the occupation: ")
if '9' in choices:
    user_info['favorite_color'] = input("Enter the favorite color: ")

print("Collected Information:", user_info)
name=input("Enter the name of the person you want to search: ")
print(f"<----Searching for all possible combinations of the given {name}---->")
print("Collected Information:", user_info)
for i in getListsOfUsernames(name):
    print(f"Searching for {i}")
    # run_sherlock(i)

print(run_what("+91 9526969878"))
