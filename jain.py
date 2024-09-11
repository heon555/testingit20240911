character = {"name": "moon", "quote": "human is first"}
year = 1953
age = 1
start = str(input("Hellow who are you? "))
if start == "moon" :
    print(character["quote"])
    for i in range(1, 72) :
        print("I am president Jae-in Moon, I was ", age,"years old in ", year)
        year += 1
        age += 1
else :
    print(...)