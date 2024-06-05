class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        results = []
        for idx_1 in range(len(nums)):
                for idx_2 in range(idx_1+1, len(nums),1):
                    temp = nums[idx_1] + nums[idx_2]
                    if temp == target:
                        results.append(idx_1)
                        results.append(idx_2)
                        return results
                    else:
                        continue
                    
                    