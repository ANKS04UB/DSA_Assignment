#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Ans 1) code to find the integers that appeared in all three arrays
def intersect(arr1, arr2, arr3):
    result = []
    i, j, k = 0, 0, 0
    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        if arr1[i] == arr2[j] == arr3[k]:
            result.append(arr1[i])
            i += 1
            j += 1
            k += 1
        elif arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr3[k]:
            j += 1
        else:
            k += 1
    return result


# In[3]:


arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 5, 7, 9]
arr3 = [1, 3, 4, 5, 8]

intersect(arr1, arr2, arr3)


# In[4]:


# Ans 2) code to find the two lists of distinct integers in two arrays
def findDifference(nums1, nums2):
    result = [[], []]
    nums1_set = set(nums1)
    nums2_set = set(nums2)
    for num in nums1:
        if num not in nums2_set:
            result[0].append(num)
    for num in nums2:
        if num not in nums1_set:
            result[1].append(num)
    return result


# In[5]:


nums1 = [1, 2, 3]
nums2 = [2, 4, 6]

findDifference(nums1, nums2)


# In[7]:


# Ans 3) code to find the transpose of a 2D integer array
def transpose(matrix):
    result = []
    for i in range(len(matrix[0])):
        result.append([matrix[j][i] for j in range(len(matrix))])
    return result


# In[8]:


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

transpose(matrix)


# In[10]:


# Ans 4) code to find the maximum sum of the minimum elements in pairs in an integer array
def arrayPairSum(nums):
    nums.sort()
    result = 0
    for i in range(0, len(nums), 2):
        result += nums[i]
    return result


# In[11]:


nums = [1, 4, 3, 2]

arrayPairSum(nums)


# In[12]:


# Ans 5) code to find the number of complete rows in a staircase with n coins
def staircase(n):
    result = 0
    for i in range(1, n + 1):
        if n >= i:
            result += 1
            n -= i
    return result


# In[13]:


n = 5

staircase(n)


# In[14]:


# Ans 6) 
def sortedSquares(nums):
    result = []
    for num in nums:
        result.append(num ** 2)
    result.sort()
    return result


# In[16]:


nums = [-4,-1,0,3,10]

sortedSquares(nums)


# In[18]:


# Ans 7) code to find the number of maximum integers in a matrix after performing all the operations
def maxCount(m, n, ops):
    result = 0
    for ai, bi in ops:
        result = max(result, ai * bi)
    return result


# In[19]:


m = 3
n = 3
ops = [[2,2], [3,3]]

maxCount(m, n, ops)


# In[20]:


# Ans 8) code to rearrange the elements of an array
def shuffle(nums, n):
    result = []
    for i in range(n):
        result.append(nums[i])
        result.append(nums[i + n])
    return result


# In[21]:


nums = [2, 5, 1, 3, 4, 7]
n = 3

shuffle(nums, n)


# In[ ]:




