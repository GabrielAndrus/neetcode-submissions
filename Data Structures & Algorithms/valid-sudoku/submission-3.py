class Solution:
    def isValidSequence(self, sequence: list[str]) -> bool:
        seen = set()
        for val in sequence:
            if val == ".":
                continue
            else:
                if val in seen:
                    return False
                seen.add(val)
        return True


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = {}

        for r in range(9):
            if not self.isValidSequence(board[r]):
                return False
        
        for c in range(9):
            column = [board[r][c] for r in range(9)]
            if not self.isValidSequence(column):
                return False

        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    
                    val = board[r][c]
                    
                    val = board[r][c]
                    key = (r // 3, c // 3)
                    
                    if key not in boxes:
                        boxes[key] = set()
                    
                    if val in boxes[key]:
                        return False
                        
                    boxes[key].add(val)
                else:
                    pass
                
        return True

    





    # Optional refactoring at the end: Combine the isValidRow and isValidColumn methods into 
    # one single isValidSequence function -- Actually probably can't do this, since columns are traversed 
    # Differently...

    