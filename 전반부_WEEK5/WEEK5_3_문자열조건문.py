#문자열 예시
articles = ["손흥민은 손으로 상대의 얼굴을 밀며 맞받아쳤다.", "AS로마의 니콜로 자니올로", "이강인의 팀 동료 페란 토레스"]

for a in articles:
    if "손흥민" in a:
        print("손흥민 기사")
    elif "이강인" in a:
        print("이강인 기사")
    elif "니콜로" in a:
        print(1)
    else:
        print("손흥민/이강인이 나오지 않는 기사")

#예시
players = ["손흥민", "이강인", "황희찬"]
if "손흥민" in players:
    print(1)