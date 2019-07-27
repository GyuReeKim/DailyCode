# if문을 활용한 선택 프로그램 작성
import random

print("게임 이름을 입력하세요.")
game_name = input()

hunter = ["타격감", "솔플", "운영"]
survivor = ["멘탈", "팀워크", "스릴", "뚝배기"]

# 랜덤 추출1
hunt_random1 = random.choice(hunter)
surv_random1 = random.choice(survivor)

# 질문1
print(f"당신에게는 {hunt_random1}과 {surv_random1} 중에 어떤 것이 중요합니까?")
print(f"{hunt_random1}과 {surv_random1} 중에 선택하세요.")

# 대답 입력1
first_q = input()

# if문을 활용한 추천1
if first_q == "멘탈":
    rec_first = "멘탈"
elif first_q == f"{hunt_random1}":
    rec_first = "감시자"
else:
    rec_first = "생존자"

# 먼저 나온 랜덤값을 제거하기 위한 num1 출력
if hunt_random1 == "타격감":
    num1 = 0
elif hunt_random1 == "솔플":
    num1 = 1
elif hunt_random1 == "운영":
    num1 = 2

# num1 제거
del hunter[num1]

# 먼저 나온 랜덤값을 제거하기 위한 num2 출력
if surv_random1 == "멘탈":
    num2 = 0
elif surv_random1 == "팀워크":
    num2 = 1
elif surv_random1 == "스릴":
    num2 = 2
elif surv_random1 == "뚝배기":
    num2 = 3

# num2 제거
del survivor[num2]

# 랜덤 추출2
hunt_random2 = random.choice(hunter)
surv_random2 = random.choice(survivor)

# 질문 2
print(f"당신에게는 {hunt_random2}과 {surv_random2} 중에 어떤 것이 중요합니까?")
print(f"{hunt_random2}과 {surv_random2} 중에 선택하세요.")

# 대답 입력2
second_q = input()

# if문을 활용한 추천2
if second_q == "멘탈":
    rec_second = "멘탈"
elif second_q == f"{hunt_random2}":
    rec_second = "감시자"
else:
    rec_second = "생존자"

# 서로 다른 선택지를 선택했을 시 랜덤 출력
character = ["감시자", "생존자"]
random_choice = random.choice(character)

# 둘 중 한가지 추천
if rec_first == "멘탈":
    print(f"당신의 {rec_first}로 감시자를 하기에는 무리입니다. 생존자를 추천합니다.")
elif rec_second == "멘탈":
    print(f"당신의 {rec_second}로 감시자를 하기에는 무리입니다. 생존자를 추천합니다.")
elif rec_first == rec_second:
    recommend = rec_first
    print(f"당신에게는 {game_name}의 {recommend}를 추천합니다.")
else:
    recommend = random_choice
    print(f"당신에게는 {game_name}의 {recommend}를 추천합니다.")