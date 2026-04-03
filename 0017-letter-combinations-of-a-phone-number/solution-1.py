class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashmap = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']}
        
        res = []

        def backtrack(index, cur):
            if index == len(digits):
                res.append(cur[:])
                return 

            for letter in hashmap[digits[index]]:
                backtrack(index + 1, cur + letter)

        backtrack(0, '')
        return res

        '''
        backtrack(0, "")
        ├── backtrack(1, "a")
        │    ├── backtrack(2, "ad") → append → return
        │    ├── backtrack(2, "ae") → append → return
        │    └── backtrack(2, "af") → append → return
        ├── backtrack(1, "b")
        │    ├── backtrack(2, "bd") → append → return
        │    ├── backtrack(2, "be") → append → return
        │    └── backtrack(2, "bf") → append → return
        └── backtrack(1, "c")
            ├── backtrack(2, "cd") → append → return
            ├── backtrack(2, "ce") → append → return
            └── backtrack(2, "cf") → append → return
        '''