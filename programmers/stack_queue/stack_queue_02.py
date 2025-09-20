# 기능개발

# 문제 설명
#   프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.

# 또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고,
# 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.
# 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 
# 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 
# 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.

# 제한 사항
#   작업의 개수(progresses, speeds배열의 길이)는 100개 이하입니다.
#   작업 진도는 100 미만의 자연수입니다.
#   작업 속도는 100 이하의 자연수입니다.
#   배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정합니다. 예를 들어 진도율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다.

def solution(progresses, speeds):
    
    compl_days = []
    for i in range(len(progresses)):
        rest_time = 100 - progresses[i] # 남은 작업 시간
        rest_day = rest_time // speeds[i] + 1 if rest_time % speeds[i] else rest_time // speeds[i]
        compl_days.append(rest_day) # 완료되는데 걸리는 일수
    
    dist_count = 1
    work_dist_list = []
    compl_days.reverse()

    pop_value = compl_days.pop()

    while len(compl_days):
        '''
            기준 작업일수를 이후 작업일수와 비교
        '''
        if pop_value >= compl_days[-1]: # 기준 작업일수보다 비교 작업일수가 작거나 같으면 같은 경우
            compl_days.pop() # 비교한 작업일수는 pop
            dist_count += 1 # 배포 카운트 + 1
        else: # 기준 작업일수보다 비교 작업일수가 큰 경우
            work_dist_list.append(dist_count) # 날짜가 바뀌므로 push
            pop_value = compl_days.pop() # 기준 작업일수 변경
            dist_count = 1
    else:
        work_dist_list.append(dist_count)

    return work_dist_list

print('solu', solution([95, 92, 92, 93], [1, 1, 1, 1]))
print('solu', solution([95, 95, 93, 92, 92, 90], [1,1,1,1,1,1]))
