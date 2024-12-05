import os

# Prompt the user to enter their name
user_name = input("Enter your name to store in file or press Enter to skip: ").strip()
if user_name:
    with open('user_info.txt', 'a') as file:
        file.write(user_name + "\n")
    print(f"Name '{user_name}' added successfully!")

# Ask if the user wants to see stored usernames
show_info = input("Do you want to see all stored usernames? (y/n): ").strip().lower()
if show_info == 'y':
    if os.path.exists('user_info.txt'):
        with open('user_info.txt', 'r') as file:
            content = file.readlines()
        if content:
            print("Stored Usernames:")
            for i, line in enumerate(content, 1):
                print(f"{i}. {line.rstrip()}")
        else:
            print("No usernames found in the file!")
    else:
        print("File 'user_info.txt' does not exist!")