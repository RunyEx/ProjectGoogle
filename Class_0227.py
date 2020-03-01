# 부모 클래스
class Parents:
    father = "kim"

    def father_name(self):
        print(self.father)
# 자식 클래스
class MySon(Parents):
    def __init__(self, name, age, kind, distinct, speak):
        self.name = name
        self.age = age
        self.kind = kind
        self.distinct = distinct
        self.speak = speak
    description = "animal"

    def bark(self):
        print(self.speak)
# 오버라이드
    def father_name(self):
        print("Lee")
# 실행
MySon1 = MySon("baba", "20", "mix", "cute", "kabuki")
MySon1.bark()
MySon1.father_name()
print((type(MySon1)))
print(MySon1.kind)
print(MySon1.description)

# 클래스의 함수 확인하는 방법
print(dir(list))