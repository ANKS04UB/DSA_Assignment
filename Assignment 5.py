#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Ans 1) code to convert a 1D array into a 2D array 
def convert2DArray(original, m, n):
    result = []
    for i in range(m):
        result.append([])
        for j in range(n):
            result[i].append(original[i * n + j])
    return result


# In[2]:


original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
m = 3
n = 3

convert2DArray(original, m, n)


# In[4]:


# Ans 2) code to find the number of complete rows in a staircase with n coins
def staircase(n):
    result = 0
    i = 1
    while n >= i:
        result += 1
        n -= i
        i += 1
    return result


# In[5]:


staircase(5)


# In[6]:


# Ans 3) 
def sortedSquares(nums):
    result = []
    for num in nums:
        result.append(num ** 2)
    result.sort()
    return result


# In[7]:


nums = [-4,-1,0,3,10]
sortedSquares(nums)


# In[8]:


# Ans 4) code to find the two lists of distinct integers in two arrays
def findDifference(nums1, nums2):
    result = [[], []]
    for num in nums1:
        if num not in nums2:
            result[0].append(num)
    for num in nums2:
        if num not in nums1:
            result[1].append(num)
    return result


# In[11]:


nums1 = [1, 2, 3]
nums2 = [2, 4, 6]

findDifference(nums1, nums2)


# In[13]:


# Ans 5) code to find the distance value between two arrays 
def findDistance(arr1, arr2, d):
    result = 0
    for num in arr1:
        if not any(abs(num - num2) <= d for num2 in arr2):
            result += 1
    return result


# In[17]:


arr1 = [4, 5, 8]
arr2 = [10, 9, 1, 8]
d = 2

print(findDistance(arr1, arr2, d))


# In[18]:


# Ans 6) code to find the integers that appear twice in an array
def findDuplicates(nums):
    result = []
    for num in nums:
        if nums[abs(num) - 1] < 0:
            result.append(abs(num))
        else:
            nums[abs(num) - 1] *= -1
    return result


# In[19]:


nums = [4, 3, 2, 7, 8, 2, 3, 1]

print(findDuplicates(nums))


# In[20]:


# Ans 7) code to find the minimum element in a rotated sorted array
def findMin(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]


# In[21]:


nums = [3, 4, 5, 1, 2]

print(findMin(nums))


# In[27]:


# Ans 8) code to find the original array from a doubled array
def undouble(changed):
    result = []
    for num in changed:
        if num % 2 == 0:
            result.append(num // 2)
        else:
            return []
    return result


# In[28]:


changed = [1, 3, 4, 2, 6, 8]

print(undouble(changed))


# In[ ]:




