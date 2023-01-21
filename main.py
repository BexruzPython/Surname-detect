a = input("Enter a surname:")
if a[-1] == "v" and a[-2] == "e" and a[-3] == "y":
    print("This is the surname of a boy!")
#If the last 3 letters are completed with 'yev', it will be a boy family
elif a[-1] == "a" and a[-2] == "v" and a[-3]== "e" and a[-4] == "y":
    print("This is the surname of a girl!")
#If the last 4 letters are completed with 'yeva', it will be a girl family
elif a[-1] == "v" and a[-2] == "o":
    print("This is the surname of a boy!")
#If the last 2 letters are completed with 'ov',it will be a boy family
elif a[-1] == "a" and a[-2] == "v" and a[-3] == "o":
    print("This is  surname of a girl!")
#If the last  3letters are completed with 'ova', it will be a girl family
else:
    print("This is not a surname!")
