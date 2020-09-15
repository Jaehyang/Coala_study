#별찍기
#1. 순서대로 별찍기

for i in range(1, 11) :
    print("*"*i)

# 2. 2단위로 별찍기(1, 3, ..., 9)
for i in range(1, 10, 2) :
    print("*"*i)

# 3. 거꾸로 별찍기(10, 9,..., 1)
for i in range(10, 0, -1):
    print("*"*i)