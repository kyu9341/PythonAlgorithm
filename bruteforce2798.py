'''

문제
카지노에서 제일 인기 있는 게임 블랙잭의 규칙은 상당히 쉽다. 카드의 합이 21을 넘지 않는 한도 내에서, 카드의 합을 최대한 크게 만드는 게임이다. 블랙잭은 카지노마다 다양한 규정이 있다.

한국 최고의 블랙잭 고수 김정인은 새로운 블랙잭 규칙을 만들어 상근, 창영이와 게임하려고 한다.

김정인 버젼의 블랙잭에서 각 카드에는 양의 정수가 쓰여 있다. 그 다음, 딜러는 N장의 카드를 모두 숫자가 보이도록 바닥에 놓는다. 그런 후에 딜러는 숫자 M을 크게 외친다.

이제 플레이어는 제한된 시간 안에 N장의 카드 중에서 3장의 카드를 골라야 한다. 블랙잭 변형 게임이기 때문에, 플레이어가 고른 카드의 합은 M을 넘지 않으면서 M과 최대한 가깝게 만들어야 한다.

N장의 카드에 써져 있는 숫자가 주어졌을 때, M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하시오.

입력
첫째 줄에 카드의 개수 N(3 ≤ N ≤ 100)과 M(10 ≤ M ≤ 300,000)이 주어진다. 둘째 줄에는 카드에 쓰여 있는 수가 주어지며, 이 값은 100,000을 넘지 않는다.

합이 M을 넘지 않는 카드 3장을 찾을 수 있는 경우만 입력으로 주어진다.

출력
첫째 줄에 M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 출력한다.

예제 입력 1
5 21
5 6 7 8 9
예제 출력 1
21

'''
from itertools import combinations

N, M = map(int, input().split())
nums = []
nums = input().split()
nums = list(map(int, nums))

cards = list(combinations(nums, 3)) # nums의 3개로 이루어진 중복하지 않는 모든 조합을 구함
# [(5, 6, 7), (5, 6, 8), (5, 6, 9), (5, 7, 8), (5, 7, 9), (5, 8, 9), (6, 7, 8), (6, 7, 9), (6, 8, 9), (7, 8, 9)]
cards_lists = [list(i) for i in cards] # 리스트 내의 튜플의 형태를 리스트 내의 리스트로 변환
# [[5, 6, 7], [5, 6, 8], [5, 6, 9], [5, 7, 8], [5, 7, 9], [5, 8, 9], [6, 7, 8], [6, 7, 9], [6, 8, 9], [7, 8, 9]]
cards_sum = []
for i in range(0, len(cards_lists)): # 각 리스트의 합을 원소로 하는 리스트 cards_sum
    cards_sum.append(sum(cards_lists[i]))

M_list = [M for i in range(0, len(cards_sum))] # 모든 원소가 M인 cards_sum과 크기가 같은 리스트 생성
sub_list = []

for i in range(0, len(cards_sum)):
    if M_list[i]-cards_sum[i] < 0: # 차가 0보다 작아지는 경우 최소값으로 나오지 않도록 지정
        sub_list.append(30000000)
    else:
        sub_list.append(M_list[i]-cards_sum[i]) # 각 원소의 차이를 저장하는 리스트 sub_list

min_num = min(sub_list)
print(cards_sum[sub_list.index(min_num)])


