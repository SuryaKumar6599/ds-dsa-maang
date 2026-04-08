class Soltions:
    def isValid(self, s: str) -> bool:
        stack = []
        match_map = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in match_map:
                if not stack or stack.pop() != match_map[char]:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0
        
# Example usage:
solution = Soltions()

print(solution.isValid("(]"))  # Output: False
print(solution.isValid("([)]"))  # Output: False
print(solution.isValid("{[]}"))  # Output: True
print(solution.isValid(""))  # Output: True

