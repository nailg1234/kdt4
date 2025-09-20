# 다리를 지나는 트럭

# 문제 설명
#   트럭 여러 대가 강을 가로지르는 일차선 다리를 정해진 순으로 건너려 합니다. 
#   모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다.
#   다리에는 트럭이 최대 bridge_length대 올라갈 수 있으며,
#   다리는 weight 이하까지의 무게를 견딜 수 있습니다.
#   단, 다리에 완전히 오르지 않은 트럭의 무게는 무시합니다.

# 예를 들어, 트럭 2대가 올라갈 수 있고 무게를 10kg까지 견디는 다리가 있습니다.
# 무게가 [7, 4, 5, 6]kg인 트럭이 순서대로 최단 시간 안에 다리를 건너려면 다음과 같이 건너야 합니다.


# solution 함수의 매개변수로 다리에 올라갈 수 있는 트럭 수 bridge_length,
# 다리가 견딜 수 있는 무게 weight, 트럭 별 무게 truck_weights가 주어집니다.이때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return 하도록 solution 함수를 완성하세요.

# 제한 조건
# bridge_length는 1 이상 10,000 이하입니다.
# weight는 1 이상 10,000 이하입니다.
# truck_weights의 길이는 1 이상 10,000 이하입니다.
# 모든 트럭의 무게는 1 이상 weight 이하입니다.

def solution(bridge_length, weight, truck_weights):
    
    with_index_list = [[truck, 0] for truck in truck_weights]
    with_index_list.reverse()
    river_list = []
    
    sec = 0
    while len(with_index_list) or len(river_list): # 대기트럭, 다리를 건너는 트럭 있는 동안
        if len(with_index_list):
            # 다리가 견디는 무게 > 다리에 트럭 무게 + 다음 트럭무게 and 다리 길이 > 다리에 트럭 대수
            if (weight >= sum([truck for [truck, time] in river_list] + [with_index_list[-1][0]]) and bridge_length > len(river_list)):
                river_list.append(with_index_list.pop()) # 트럭 1대 다리위로 이동
        
        if len(river_list):
            for in_river_truck in river_list:
                in_river_truck[1] += 1 # 다리위에 머무른 시간 체크
            else:
                if bridge_length < river_list[0][1]:
                    river_list.pop(0) # 첫번째 트럭 다리 지나감
                    if len(with_index_list):
                        # 다리가 견디는 무게 > 다리에 트럭 무게 + 다음 트럭무게 and 다리 길이 > 다리에 트럭 대수
                        if (weight >= sum([truck for [truck, time] in river_list] + [with_index_list[-1][0]]) and bridge_length > len(river_list)):
                            pop_value = with_index_list.pop() # 대기 트럭 다리위로 올리기
                            river_list.append([pop_value[0], 1]) # 대기 트럭 다리위로 올라갔으니 정차시간 1초
        sec += 1
    return sec