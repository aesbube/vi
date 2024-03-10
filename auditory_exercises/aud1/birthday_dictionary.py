birthdays = {
    "Mila": "13/09/2003",
    "Marija": "01/01/2004",
    "Juan": "01/05/2005",
    "Juana": "14/07/2007"
}

print("The birthday dictionary:")
print("\n".join(birthdays.keys()))
print("Enter the birthday date you are looking for:")
user_input = input()

birthday = birthdays[user_input]
print(f"Birthday of the person {user_input} is {birthday}")
