class Solution:
    # vì mảng đã được sắp xếp, nên khi xoay mảng thì 1 trong 2 nửa trái hoặc phải của mid sẽ được sắp xếp
    # nếu mảng bên trái được sắp xếp thì nums[left] phải <= nums[mid], còn nếu nums[left] mà > nums[mid] thì mảng bên phải sẽ được sắp xếp
    # còn lại là kiểm tra xem target có nằm trong các nửa đó không
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
