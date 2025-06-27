# 74. Search a 2D Matrix 
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Hints
        # Compiled to Debug

        row_s = 0
        row_e = len(matrix) - 1
        candidate_row_found = False
        while row_s <= row_e:
            row_mid = (row_e + row_s) // 2
            if matrix[row_mid][0] <= target and target <= matrix[row_mid][-1]:
                candidate_row_found = True
                break
            elif matrix[row_mid][0] > target:
                row_e = row_mid - 1
            else:
                row_s = row_mid + 1

        if not candidate_row_found:
            return False
        
        left_col = 0
        right_col = len(matrix[0]) - 1
        while left_col <= right_col:
            mid_col = (right_col + left_col) // 2
            if matrix[row_mid][mid_col] == target:
                return True
            elif matrix[row_mid][mid_col] > target:
                right_col = mid_col - 1
            else:
                left_col = mid_col + 1
        
        return False