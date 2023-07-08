#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Ans 1) code to find the lowest ASCII sum of deleted characters to make two strings equal 
def lowest_ascii_sum_of_deleted_characters(s1, s2):
    ascii_sum = 0
    i = j = 0
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            ascii_sum += ord(s1[i])
            i += 1
        else:
            i += 1
            j += 1
    ascii_sum += ord(s1[i:]) if i < len(s1) else 0
    ascii_sum += ord(s2[j:]) if j < len(s2) else 0
    return ascii_sum


# In[5]:


s1 = "sea"
s2 = "eat"

print(minimumDeleteSum(s1, s2))


# In[6]:


# Ans 2) code to check if a string is valid using '*' in Python
def checkValidString(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if not stack:
                return False
            stack.pop()
        elif c == '*':
            if not stack:
                stack.append(c)
            else:
                stack.pop()
    return not stack


# In[7]:


s = "()"

print(checkValidString(s))


# In[8]:


# Ans 3) code to find the minimum number of steps required to make two strings the same
def minDistance(word1, word2):
    dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
    for i in range(len(word1) + 1):
        for j in range(len(word2) + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            else:
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1)
    return dp[-1][-1]


# In[10]:


word1 = "sea"
word2 = "eat"

print(minDistance(word1, word2))


# In[17]:


# Ans 4) code to construct a binary tree from a string
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def construct_binary_tree(str):
    if not str:
         return None

    root = TreeNode(int(str[0]))
    i = 1
    if str[i] == "(":
        root.left = construct_binary_tree(str[i + 1:])
        i += len(str[i + 1:].split("("))
    if str[i] == "(":
        root.right = construct_binary_tree(str[i + 1:])
        i += len(str[i + 1:].split("("))
    return root


# In[18]:


str = "1(2(3)(4))(5)"

print(construct_binary_tree(str))


# In[24]:


# Ans 6) code to find all the start indices of an anagram of a string
def findAnagrams(s, p):
    ans = []
    n = len(s)
    m = len(p)
    count = [0] * 26
    for i in range(m):
        count[ord(p[i]) - ord('a')] += 1
    for i in range(n - m + 1):
        temp = count.copy()
        for j in range(m):
            temp[ord(s[i + j]) - ord('a')] -= 1
        if all(x == 0 for x in temp):
            ans.append(i)
    return ans


# In[25]:


s = "cbaebabacd"
p = "abc"

print(findAnagrams(s, p))


# In[33]:


# Ans 8) code to check if two strings can be obtained by swapping two letters in one another
def buddyStrings(s, goal):
    n = len(s)
    if n != len(goal):
        return False
    
    diff = 0
    for i in range(n):
        if s[i] != goal[i]:
            diff += 1
            if diff > 2:
                return False
            
    if diff == 0:
        return any(s[i] == s[j] for i in range(n) for j in range(i + 1, n))
    
    return True


# In[34]:


s = "ab"
goal = "ba"

print(buddyStrings(s, goal))


# In[ ]:




