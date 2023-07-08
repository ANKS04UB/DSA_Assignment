#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Ans 1) code to check if two strings are isomorphic
def isIsomorphic(s, t):
    mapping = {}
    for i in range(len(s)):
        if s[i] not in mapping:
            mapping[s[i]] = t[i]
        elif mapping[s[i]] != t[i]:
            return False
    return True


# In[2]:


s = "egg"
t = "add"

print(isIsomorphic(s, t))


# In[3]:


# Ans 2) code to check if a string is strobogrammatic
def isStrobogrammatic(num):
    num = num.replace("0", "0")
    num = num.replace("1", "1")
    num = num.replace("6", "9")
    num = num.replace("9", "6")
    return num == num[::-1]


# In[4]:


num = "69"

print(isStrobogrammatic(num))


# In[5]:


# Ans 3) code to add two strings representing non-negative integers
def addStrings(num1, num2):
    result = ""
    i, j, carry = len(num1) - 1, len(num2) - 1, 0
    while i >= 0 or j >= 0:
        sum = carry
        if i >= 0:
            sum += int(num1[i])
            i -= 1
        if j >= 0:
            sum += int(num2[j])
            j -= 1
        carry = sum // 10
        result += str(sum % 10)
    return result[::-1] if carry == 0 else "1" + result[::-1]


# In[6]:


num1 = "11"
num2 = "123"

print(addStrings(num1, num2))


# In[7]:


# Ans 4) code to reverse the order of characters in each word in a sentence
def reverseWords(s):
    return " ".join([word[::-1] for word in s.split(" ")])


# In[8]:


s = "Let's take LeetCode contest"

print(reverseWords(s))


# In[9]:


# Ans 5) code to reverse the first k characters for every 2k characters in a string
def reverseStr(s, k):
    n = len(s)
    res = ""
    for i in range(0, n, 2 * k):
        res += s[i:i + k][::-1] + s[i + k:i + 2 * k]
    return res + s[n - k:] if n % 2 == 1 else res


# In[10]:


s = "abcdefg"
k = 2

print(reverseStr(s, k))


# In[11]:


# Ans 6) code to check if a string can be obtained from another string by a series of shifts
def canBeEqual(s, goal):
    return sorted(s) == sorted(goal)


# In[12]:


s = "abcde"
goal = "cdeab"

print(canBeEqual(s, goal))


# In[13]:


# Ans 7) code to check if two strings are equal after being typed into empty text editors
def backspaceCompare(s, t):
    s = s.replace("#", "")
    t = t.replace("#", "")
    return s == t


# In[14]:


s = "ab#c"
t = "ad#c"

print(backspaceCompare(s, t))


# In[15]:


# Ans 8) code to check if a set of points make a straight line
def checkStraightLine(coordinates):
    x1, y1 = coordinates[0]
    x2, y2 = coordinates[1]
    x_diff = x2 - x1
    y_diff = y2 - y1
    for x, y in coordinates[2:]:
        if (x - x1) / x_diff != (y - y1) / y_diff:
            return False
    return True


# In[16]:


coordinates = [[1, 2], [2, 3], [3, 4]]

print(checkStraightLine(coordinates))


# In[ ]:




