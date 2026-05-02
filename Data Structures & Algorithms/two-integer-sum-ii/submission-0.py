class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r, l = 0, len(numbers) - 1

        while r < l:
            wsum = numbers[r] + numbers[l]
            if wsum > target:
                l -=1
            elif wsum < target:
                r += 1
            else:
                return [r+1, l+1]