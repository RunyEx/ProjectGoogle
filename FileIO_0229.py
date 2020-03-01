# ========================== 파일 열기, 파일이 없으면 자동으로 생성한다/ 데이터를 쓰면 기존 데이터 삭제
f = open("some.txt", "w")
for i in range(1, 9+1):
    data = "5 * {} = {}\n".format(i, 5*i)
    f.write(data)
f.close()

# ========================== 파일 읽기
# 전체 읽기
f = open("some.txt", "r")
print(f.read())
f.close()

# 한줄 읽기
f = open("some.txt", "r")
while True:
    data = f.readline()
    if not data:
        break
    print(data, end="")
f.close()

# 반복문을 사용해서 읽기
f = open("some.txt", "r")
data = f.readlines() # list
f.close()
for line in data:
    print(line, end="")

# x 새파일 작성모드
# a 추가모드