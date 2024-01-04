def solution(s: str):
    try:
        stack = []
        for c in s:
            if c == "(":
                stack.insert(-1, c)
            elif c == ")":
                stack.pop()
        return len(stack) == 0
    except:
        return False


print(solution("()"))
print(solution("())"))
print(solution("(()"))
print(solution("(3 + (4 * 5))"))
print(solution("( () ( () ) )"))
print(solution(")("))
