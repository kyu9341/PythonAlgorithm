'''
문제
지민이는 N쪽인 책이 한권 있다. 첫 페이지는 1쪽이고, 마지막 페이지는 N쪽이다. 각 숫자가 모두 몇 번이 나오는지 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 0이 총 몇 번 나오는지, 1이 총 몇 번 나오는지, ..., 9가 총 몇 번 나오는지를 출력한다.

예제 입력 1
11
예제 출력 1
1 4 1 1 1 1 1 1 1 1
'''
# 런타임 에러

n = int(input())

pagelist = [] # 각 숫자가 몇 번 나오는지를 저장할 리스트
for i in range(0,10): # 0~9 인덱스를 각각 0으로 초기화
    pagelist.insert(i, 0)
#print(pagelist)
def page(num): # 재귀함수 작성

    if num == 0:
        return pagelist
    else:
        for i in str(num):
            pagelist[int(i)] +=1
        return page(num-1)
#print(page(n))
for i in page(n):
    print(i, end=" ")

