class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_in_array = set()
        for x in nums:
            if x in nums_in_array:
                return True
            else:
                nums_in_array.add(x)
        return False



        