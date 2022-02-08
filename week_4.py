usernames = ['admin', 'Jason','Dave', 'Adam', 'Trevor']

for usernames in usernames:
    if usernames == 'admin' :
        print("Hello admin, would you like to see a status report?")
    else :
        print("Hello " + usernames +  ", thank you for logging in again.")

if usernames:
  for usernames in usernames:
      if usernames == 'admin' :
        print("Hello admin, would you like to see a status report?")
      else :
        print("Hello " + usernames +  ", thank you for logging in again.")
else :
    print("We need to find some users")

current_users = ['John', 'Dave', 'Jacob', 'Timothy','Daniel']
new_users = ['John', 'Mark', 'Cameron', 'Timothy', 'Robert']

current_users_lower = [user.lower() for user in current_users]
for new_user in new_users :
    if new_user.lower() in current_users_lower :
        print("Sorry " + new_user + " that username is taken")
    else :
        print("Great! " + new_user + " That username is available")

numbers = list(range(1,10))
for number in numbers :
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else :
       print(str(number) + "th")

number = input("Enter a number: ")

if(int(number) % 10 == 0):
    print("The number you have entered is a multiple of 10")
else:
    print("The number is not a multiple of 10")