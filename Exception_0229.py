# 예외처리
import random

def numguess(try_cnt = 5, answer = random.randint(1, 100)):
    while True:
        if try_cnt == 0:
            print("your try Count is sold out\n Correct is {}".format(answer))
            break

        try:
            your_input = int(input("input the answer : "))
        except Exception as e:
            print(e)
        else:
            if answer == your_input:
                print("Correct : answer is {}".format(answer))
                break
            elif answer > your_input:
                try_cnt -= 1
                print(("bigger than {}".format(your_input)))
            else:
                try_cnt -= 1
                print(("smaller than {}".format(your_input)))
            # finally

# 나의 Exception
class MyError(Exception):
    def __str__(self):
        return "My Custom Error"