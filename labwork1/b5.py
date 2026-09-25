info ={"Red", "Green", "Blue", "Yellow", "Orange", "Purple"}
mau = input("What is your favorite color? ")
if mau in info:
    print("Your favorite color is at index " + str(list(info).index(mau)) + " in the list.")
else:
    print("Sorry,I could not find your color")