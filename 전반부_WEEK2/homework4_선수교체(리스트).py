# 선수교체 브로그램 만들기(리스트 연습하기)
players = ["황의조", "황희찬", "구자철", "이재성", "기성용"]
print("현재 경기 중인 선수: ")
for i in range(len(players)) :
    print(players[i])

print("-" * 40)

Out = int(input("OUT 시킬 선수 번호: "))
In = input("IN 할 선수 이름: ")
print("-"*40)

del players[Out -1]
players.append(In)

print("교체결과: ")
for i in range(len(players)) :
    print(players[i])

