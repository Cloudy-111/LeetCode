class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l = moves.count('L')
        r = moves.count('R')
        dash = moves.count('_')
        if l == 0 or r == 0:
            return len(moves)
        if l > r:
            return l - r + dash
        elif l < r:
            return r - l + dash
        else:
            return dash
