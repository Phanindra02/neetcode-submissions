class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        if not mat or not mat[0]:
            return False

        rows, cols = len(mat), len(mat[0])
        left, right = 0, rows * cols - 1

        while left <= right:
            mid = left + (right - left) // 2
            val = mat[mid // cols][mid % cols]

            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1

        return False