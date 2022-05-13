class Solution:
    def twoSum(self, numbers, target):
        
        l, r = 0, len(numbers) - 1

        while l < r:
            diff = numbers[l] + numbers[r]
            if diff == target:
                return [l+1, r+1]
            elif diff > target:
                r -= 1
            else:
                l += 1
        
    
        
    
sol = Solution()
print(sol.twoSum([2,7,11,15],9), "=> [1, 2]")
print(sol.twoSum([2,3,4],6), "=> [1, 3]")
print(sol.twoSum([-1,0],-1), "=> [1, 2]")
