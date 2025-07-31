from typing import List
    def removeElement(self, nums: List[int], val: int) -> int:
        p = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[p] = nums[i]
                p += 1
        
        return p

#input
nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2

sol = Solution()
new_length = sol.removeElement(nums, val)

print(f"Returned Length: {new_length}")
print(f"Modified nums (first {new_length} elements): {nums{:new_length}")


""" Expected Output:
Returned Length: 5
Modified nums (first 5 elements): [0, 1, 3, 0, 4]
"""
