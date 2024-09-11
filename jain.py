character = {"name": "moon", "quote": "human is first"}

start = str(input("안녕하세요. 당신은 누구입니까? "))
if start == "moon" :
    print(character["quote"])
    for i in range(1, 73) :
        print("안녕하세요, 저는 대한민국 전 대통령 문재인입니다. 저는 ", i + 1952,"년도에 ", i, "살이었습니다.")
    print("사람이 먼저다")
else :
    print(...)

print("대화가 끝났습니다.")
print("좋은 하루 되세요.")