# 실습1. 첫번째, 마지막 요소 출력
nums = [10, 20, 30, 40, 50]
print(nums[0])  # 10 //첫번째 요소
print(nums[-1])  # 50 //마지막 요소

# 실습2. 가운데 세 개의 요소 추출
nums = [100, 200, 300, 400, 500, 600, 700]
mid = 7//2
print(nums[mid-1:mid+2])  # [300, 400, 500]

# 실습3. 리스트의 원소 두배 하기
nums = [1, 2, 3, 4, 5]
for i in range(5):
    nums[i] *= 2

print('nums', nums)
