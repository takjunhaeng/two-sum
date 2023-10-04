from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    
    print("Input: nums =", nums, ", target =", target)
    
    nums_length = len(nums)
    for i in range(nums_length - 1):
        for n in range(i+1, nums_length):
            if nums[i] + nums[n] == target:
                return [i, n]

def main():
    nums_input = input('Enter list: ')
    nums = [int(x) for x in nums_input.split(',')]
    
    target = int(input('Enter target: '))
    
    result = twoSum(nums, target)
    
    print("Output:", result)
    
    
main()
