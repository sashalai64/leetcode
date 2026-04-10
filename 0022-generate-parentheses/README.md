# [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)

## [Solution 1](#solution-1-code)


<a id="solution-1-code"></a>
```python
class Solution(object):
    def generateParenthesis(self, n):
        def dfs(l, r, s):
            if l == r == n:
                res.append(s)
                return 
            
            if l < n:
                dfs(l + 1, r, s + '(')

            if l > r:
                dfs(l, r + 1, s + ')')

        res = []
        dfs(0, 0, '')
        return res
```
