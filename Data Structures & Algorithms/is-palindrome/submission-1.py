class Solution:
    def isPalindrome(self, s: str) -> bool:
        def is_valid(ch: str) -> bool:
            return ch.isascii() and ch.isalnum()

        left = 0
        right = len(s) - 1

        while left < right:
            if not is_valid(s[left]):
                left += 1
                continue

            if not is_valid(s[right]):
                right -= 1
                continue

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True