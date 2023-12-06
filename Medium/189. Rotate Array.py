class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        lst = []
        for i in nums:
            lst.append(i)
        n = len(nums)
        t = n - k % n
        for i in range(len(nums)):
            nums[i] = lst[(t + i) % n]

    # O(1) Solution Extra Space
    # mảng sau khi xoay xong chính là mảng ban đầu xoay ngược, xoay ngược lại từ 0 đến k, xoay ngược từ k đến cuối
    # như vậy, không cần tạo thêm mảng và có độ phức tạp khôngg gian là O(1)
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n

        def rev(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        rev(nums, 0, n - 1)
        rev(nums, 0, k - 1)
        rev(nums, k, n - 1)
