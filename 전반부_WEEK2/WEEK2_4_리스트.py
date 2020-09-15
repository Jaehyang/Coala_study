# name1 = "황의조"
# name2 = "황의찬"
# name3 = "이재성"
# print(name1, name2, name3)
# 숫자 많아지면 일일이 못함.

# 리스트
players = ["황의조", "황의찬", "구자철", "이재성", "기성용"]
print(players)
print(players[0])

# 리스트에 값 추가
players.append("이승우")
print(players)
players.append("김민재")
print(players)

# 리스트 안 데이터값 지우기 del
del players[1]
print(players)

del players[1]
print(players)

# 리스트의 길이
print(len(players))

# 리스트 안 데이터 문자의 길이
print(len(players[0]))