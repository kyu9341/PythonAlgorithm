'''
분해합
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	192 MB	10108	5464	4503	53.716%
문제
어떤 자연수 N이 있을 때, 그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미한다. 어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라 한다. 예를 들어, 245의 분해합은 256(=245+2+4+5)이 된다. 따라서 245는 256의 생성자가 된다. 물론, 어떤 자연수의 경우에는 생성자가 없을 수도 있다. 반대로, 생성자가 여러 개인 자연수도 있을 수 있다.

자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 N(1 ≤ N ≤ 1,000,000)이 주어진다.

출력
첫째 줄에 답을 출력한다. 생성자가 없는 경우에는 0을 출력한다.

예제 입력 1
216
예제 출력 1
198

'''

N = str(input())
N_int = int(N)

def disSum(n): # 분해합을 구하는 함수
    n = str(n)
    n_list = list(map(int, n))
    dissum = sum(n_list)
    return int(n)+dissum

temp_list = list() # 분해합을 저장할 리스트

if N_int < 100:
    for i in range(101):
        temp_list.append(disSum(i))
    if N_int in temp_list:
        print(temp_list.index(N_int))
    else:
        print(0)
else: # 범위가 자연수 1 ~ 1,000,000 이므로 N과 생성자의 최대 차이는 9+9+9+9+9+9 = 54, 여유 있게 100 잡고 분리하여 계산(시간 고려)
    for i in range(N_int-100, N_int+1):
        temp_list.append(disSum(i))
    if N_int in temp_list:
        print(temp_list.index(N_int)+N_int-100)
    else:
        print(0)






