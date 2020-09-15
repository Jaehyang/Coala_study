data = ["조회수: 1,500", "조회수: 1,002", "조회수: 300", "조회수: 251", "조회수: 13,432", "조회수: 998"]
sum = 0

#1. 리스트 안에 있는 데이터 출력하기
for i in data:
    print(i)

#2. 리스트 안에 있는 데이터에서 숫자만 추출하기
for i in range(0, 6):
    data[i] = data[i].replace(',', '')
    data[i] = data[i].replace('조회수: ', '')
    print(data[i])

#3. 조회수 총 합 구하기
for i in range(0, 6):
    sum = sum + int(data[i])
print("총합:", sum)