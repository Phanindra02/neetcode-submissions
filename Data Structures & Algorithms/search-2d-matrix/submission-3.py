class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        if not mat or not mat[0]:
            return False

        rows, cols = len(mat), len(mat[0])
        r, c = 0, cols - 1

        while r < rows and c >= 0:
            val = mat[r][c]
            if val == target:
                return True
            elif val > target:
                c -= 1
            else:
                r += 1

        return False