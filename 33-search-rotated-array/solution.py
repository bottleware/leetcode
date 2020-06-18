class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # We're going to do a modified binary search 
        # First we need to find the lowest value
        lo, hi = 0, len(nums) -1
        # We find the lowest value when lo == hi
        while (lo < hi):

            # grab the midpoint
            mid = (lo + hi) // 2

            # if the mid is greater, then the smaller value is at the higher
            # chunk
            if nums[mid] > nums[hi]:
                lo = mid + 1
            # otherwise, it's in the lower chunk
            else:
                hi = mid


        # lo == hi == the lowest value. let's reassign this for our special
        # binary search
        rot = lo

        # we need to redefine some variables
        lo, hi = 0, len(nums) - 1
        n = len(nums)
        # now let's do a regular binary search, but this time rotate it so
        # we're always dealing with a linear array
        while (lo <= hi):

            # we need to get the floor
            mid = (lo+hi)//2
            # Let's get the real mid we're searching for. This binary search
            # basically has a permanent shift to it. We want the modulo of N to
            # make sure we don't go over the array length And we're
            # repositioning from the lowest value, so we get the actual mid of
            # the array.
            realmid = (int)(mid + rot) % n
            print(realmid)
            if nums[realmid] == target:
                return realmid
            elif nums[realmid] < target:
                lo = mid + 1
            elif nums[realmid] > target:
                hi = mid-1

        return -1
