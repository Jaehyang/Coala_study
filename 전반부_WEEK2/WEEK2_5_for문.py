# MAX = 10
#
# for i in range(1, MAX) :
#     print(i)
#     print("반복문을 배워봅시다.")
#
# for abc in range(0, 10, 2):
#     print(abc)
#     print('반복문을 배워봅시다.')

players = ["황의조", "황의찬", "구자철", "이재성", "기성용"]

print("2019년 아시안컵 출전명단")
''
for i in range(0, 5) :
    print(players[i])
print("명단 출력 끝")

for i in range(len(players)) :
    print(players[i])
print("명단 출력 끝")

for p in players:
    print(p)
print("명단 출력 끝")
