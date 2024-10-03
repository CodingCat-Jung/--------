# a와 b로만 이루어진 문자열이 주어질 때,  a를 모두 연속으로 만들기 위해서 필요한 교환의 회수를 최소로 하는 프로그램
# 이 문자열은 원형. 예를 들어,  aabbaaabaaba이 주어졌을 때, 2번의 교환이면 a를 모두 연속으로 만들 수 있다.

# 문자열을 입력 받음. 최대 길이는 1000
ab = input().strip() 

a_count = ab.count('a')

# 원형이므로 문자열을 2배로 늘림 (원형 성질을 고려하기 위해) - 슬라이딩 윈도우 방식으로 쉽게 탐색 위함
ab_double = ab * 2
n = len(ab)

# 슬라이딩 윈도우를 이용해 최소 교환 횟수 구하기
# 처음에는 a_count만큼의 구간에서 'b'의 개수를 센 다음
# 그런 다음, 슬라이딩 윈도우 방식을 이용해 구간을 한 칸씩 이동하며 교환할 'b'의 개수를 업데이트
# min_changes에 최소 교환 횟수를 저장하고, 최종적으로 그 값을 출력

min_changes = float('inf')  # 최소 교환 횟수를 저장할 변수, 처음엔 무한대 설정
current_b_count = 0  # 현재 윈도우 안에서 'b'의 개수

# 초기 윈도우 (처음 a_count만큼의 구간에서 'b'의 개수 세기)
for i in range(a_count):
    if ab_double[i] == 'b':
        current_b_count += 1

# 첫 번째 윈도우에서의 교환 횟수 저장
min_changes = current_b_count

# 슬라이딩 윈도우 시작 (i는 윈도우의 시작 인덱스)
for i in range(1, n):
    # 윈도우에서 이전에 빠지는 문자
    if ab_double[i - 1] == 'b':
        current_b_count -= 1

    # 새로 들어오는 문자
    if ab_double[i + a_count - 1] == 'b':
        current_b_count += 1

    # 최소 교환 횟수 업데이트
    min_changes = min(min_changes, current_b_count)

# 최소 교환 횟수 출력
print(min_changes)