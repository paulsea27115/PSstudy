def solution(bandage, health, attacks):
    c_health, c_time = health, 0
    h_time, h_persec, h_extra = bandage[0], bandage[1], bandage[2]
    
    for i in range(len(attacks)):
        # 스킬 효과
        heal_time = attacks[i][0] - c_time - 1
        
        c_time = attacks[i][0]
        
        c_health += heal_time * h_persec
        
        # 스킬 추가 효과
        
        if heal_time >= h_time:
            c_health += h_extra * (heal_time // h_time)
        
        # 최대 체력일 경우
        if c_health >= health: 
            c_health = health
        
        # 공격
        c_health -= attacks[i][1]
        
        # 죽을경우
        if c_health <= 0:
            return -1
        
    # 남은 체력
    return c_health 