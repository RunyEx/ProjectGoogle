# map 함수 : 게으른 연산 / 결과값을 사용하려면 iterable한 타입으로 변환 필요
some_list = [1,2,3,4,5]
result = map(lambda x: x*2, some_list)
print(result)

result2 = list(map(lambda x: x*2, some_list))
print(result2)

some_list=[1,"1","one",4.567,{1:"one"}]
result_list = list(filter(lambda  x: isinstance(x, dict), some_list))
print(result_list)

# 재귀함수
def fib(n):
    if n<=2:
        return 1
    else:
        return  fib(n-1) + fib(n-2)

print(fib(5))