class Solution(object):
    def removeDuplicateLetters(self, s):
        last_occurrence = {char: i for i, char in enumerate(s)}
        stack = []
        seen = set()

        for i, char in enumerate(s):
            if char in seen:
                continue

            # Remove characters that are bigger than current char
            # and they will appear later again
            while stack and char < stack[-1] and last_occurrence[stack[-1]] > i:
                removed = stack.pop()
                seen.remove(removed)

            stack.append(char)
            seen.add(char)

        return ''.join(stack)
