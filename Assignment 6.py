#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Ans 1) code to reconstruct the permutation from a string
def reconstruct_permutation(s):
    permutation = []
    for i in range(len(s)):
        if s[i] == 'I':
            permutation.append(i)
        else:
            permutation.append(i + 1)

    return permutation


# In[6]:


s = "IDID"

reconstruct_permutation(s)


# In[7]:


# Ans 2) code to find if a target is in a matrix
def searchMatrix(matrix, target):
    row = 0
    col = len(matrix[0]) - 1
    while row < len(matrix) and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            col -= 1
        else:
            row += 1
    return False


# In[8]:


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
target = 10

print(searchMatrix(matrix, target))


# In[9]:


# Ans 3) code to check if an array is a mountain array
def validMountainArray(arr):
    if len(arr) < 3:
        return False
    increasing = True
    decreasing = True
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            increasing = False
        if arr[i] > arr[i - 1]:
            decreasing = False
        if not increasing and not decreasing:
            return False
    return increasing and decreasing


# In[10]:


arr = [1, 2, 3, 4, 5, 3, 2, 1]

print(validMountainArray(arr))


# In[12]:


# Ans 4) code to find the maximum length of a contiguous subarray with an equal number of 0s and 1s 
def findMaxLength(nums):
    n = len(nums)
    count = 0
    max_len = 0
    hashmap = {0: -1}
    for i in range(n):
        if nums[i] == 0:
            count -= 1
        else:
            count += 1
        if count in hashmap:
            max_len = max(max_len, i - hashmap[count])
        else:
            hashmap[count] = i
    return max_len


# In[13]:


nums = [0, 1]

print(findMaxLength(nums))


# In[14]:


# Ans 5) code to find the minimum product sum of two arrays 
def minProductSum(nums1, nums2):
    nums1.sort()
    nums2.sort(reverse=True)
    return sum(nums1[i] * nums2[i] for i in range(len(nums1)))


# In[15]:


nums1 = [5, 3, 4, 2]
nums2 = [4, 2, 2, 5]

print(minProductSum(nums1, nums2))


# In[20]:


# Ans 7) code to generate a spiral matrix 
def generateMatrix(n):
    matrix = [[0 for i in range(n)] for j in range(n)]
    i, j, count = 0, 0, 1
    while count <= n * n:
        for k in range(j, n):
            matrix[i][k] = count
            count += 1
        i += 1
        for k in range(i, n):
            matrix[k][n - 1] = count
            count += 1
        n -= 1
        for k in range(n - 1, j - 1, -1):
            matrix[n][k] = count
            count += 1
        j += 1
        for k in range(n - 1, i - 1, -1):
            matrix[k][j] = count
            count += 1
    return matrix


# In[21]:


n = 3

print(generateMatrix(n))


# In[22]:


# Ans 8) code to multiply two sparse matrices
def multiply(mat1, mat2):
    m, k = len(mat1), len(mat1[0])
    n = len(mat2[0])
    result = [[0 for i in range(n)] for j in range(m)]
    for i in range(m):
        for j in range(n):
            for k in range(k):
                result[i][j] += mat1[i][k] * mat2[k][j]
    return result


# In[23]:


mat1 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
mat2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(multiply(mat1, mat2))


# In[ ]:




