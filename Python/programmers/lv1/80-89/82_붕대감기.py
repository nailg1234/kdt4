def solution(bandage, health, attacks):
    d = dict(attacks) # {공격시간, 공격력}
    fight_time = attacks[-1][0] # 전투 시간
    heal_time = bandage[0] # 시전 시간
    heal_sec = bandage[1] # 초당 회복량
    heal_add = bandage[2] # 추가 회복량
    r_health = health # 현재 체력
    con_time = 0 # 연속 성공 시간
    for _sec in range(1, fight_time + 1):
        ack = d.get(_sec, 0)
        if ack: # 몬스터 공격
            con_time = 0
            r_health -= ack
            if r_health <= 0:
                break
        else: # 회복 가능
            con_time += 1
            heal = 0
            if heal_time == con_time:
                con_time = 0
                heal = heal_add
            if r_health < health :
                heal += heal_sec
                if r_health + heal >= health :
                    r_health = health
                else:
                    r_health += heal
    return -1 if r_health <= 0 else r_health