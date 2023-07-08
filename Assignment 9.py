#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Ans 1) code to check if an integer is a power of two 
def isPowerOfTwo(n):
    if n == 0:
        return False
    return n & (n - 1) == 0


# In[2]:


n = 1

print(isPowerOfTwo(n))


# In[3]:


# Ans 2) code to find the sum of the first natural numbers 
def sum_of_n(n):
    return n * (n + 1) // 2


# In[4]:


n = 3
print(sum_of_n(n))


# In[5]:


# Ans 3) find the factorial of a positive integer
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


# In[7]:


n = 5

print(factorial(n))


# In[8]:


# Ans 4) code to find the exponent of a number raised to a given power
def power(n, p):
    if p == 0:
        return 1
    return n * power(n, p - 1)


# In[9]:


n = 5
p = 2
print(power(n, p))


# In[14]:


# Ans 6) code to find the Nth term of an arithmetic progression series
def nth_term(a, d, n):
    return a + (n - 1) * d


# In[15]:


a = 2
d = 1
n = 5

print(nth_term(a, d, n))


# In[16]:


# Ans 7) code to print all permutations of a string
def permute(s):
    if len(s) == 0:
        return []
    elif len(s) == 1:
        return [s]
    else:
        result = []
        for i in range(len(s)):
            for p in permute(s[:i] + s[i + 1:]):
                result.append(s[i] + p)
        return result
print(permute('ABC'))


# In[17]:


# Ans 8) code to find the product of all array elements
def product(arr, n):
    if n == 1:
        return arr[0]
    return arr[n - 1] * product(arr, n - 1)


# In[18]:


arr = [1, 2, 3, 4, 5]
n = len(arr)

print(product(arr, n))


# In[ ]:




