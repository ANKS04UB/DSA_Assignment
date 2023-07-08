#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Ans 1) code to check if an integer is a power of three
def isPowerOfThree(n):
    if n == 0:
        return False
    while n % 3 == 0:
        n = n // 3
    return n == 1


# In[2]:


n = 27
print(isPowerOfThree(n))


# In[3]:


# Ans 2) code to find the last number that remains in arr
def find_last_number(n):
    arr = list(range(1, n + 1))
    while len(arr) > 1:
        if len(arr) % 2 == 1:
            arr.pop(0)
        else:
            arr = arr[::-1]
            arr.pop()
            arr = arr[::-1]

    return arr[0]


# In[4]:


n = 10

print(find_last_number(n))


# In[7]:


# Ans 3) code to print all subsets of a set represented as a string
def subsets(set):
    if not set:
        return [[]]
    else:
        small_subsets = subsets(set[1:])
        ans = []
        for subset in small_subsets:
            ans.append(subset)
            ans.append([set[0]] + subset)
        return ans
set = input()
print(subsets(set))


# In[8]:


# Ans 4) code to calculate the length of a string using recursion
def length(str):
    if len(str) == 0:
        return 0
    return 1 + length(str[1:])


# In[10]:


str = "abc"
print(length(str))


# In[11]:


# Ans 5) code to find the count of all contiguous substrings starting and ending with the same character in a string
def count_substrings(s):
    count = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if s[i] == s[j - 1]:
                count += 1
    return count


# In[12]:


s = "abccba"
print(count_substrings(s))


# In[13]:


# Ans 6) code to solve the Tower of Hanoi puzzle
def tower_of_hanoi(n, from_rod, to_rod, aux_rod):
    if n == 1:
        print(from_rod, to_rod)
        return
    tower_of_hanoi(n - 1, from_rod, aux_rod, to_rod)
    print(from_rod, to_rod)
    tower_of_hanoi(n - 1, aux_rod, to_rod, from_rod)
n = int(input())
print(tower_of_hanoi(n, 1, 3, 2))


# In[20]:


# Ans 8) code to print all permutations of a string
def count_consonants(str):
    count = 0
    for i in range(len(str)):
        if str[i] not in "aeiouAEIOU":
            count += 1
    return count


# In[22]:


str = "geeksforgeeks portal"
print(count_consonants(str))


# In[ ]:




