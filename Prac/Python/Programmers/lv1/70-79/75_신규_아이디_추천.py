import re
def solution(new_id):
    
    # 1단계
    new_id = new_id.lower();
    
    # 2단계
    new_id = re.sub(r'[^a-z0-9\-_.]', '', new_id)
    
    # 3단계
    new_id = re.sub(r'\.{2,}', '.', new_id)
    
    # 4단계
    new_id = re.sub(r'^\.|\.$', '', new_id)
    
    # 5단계
    if new_id == '':
        new_id = 'a'
    
    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
    
    while new_id[-1] == '.':
        new_id = new_id[:-1]
    
    # 7단계
    
    while len(new_id) < 3:
        new_id += new_id[-1]
    
    return new_id