#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Ans 1) Maximum Sum
def solve(nums):
    nums.sort()
    return sum(nums[i] for i in range(0, len(nums), 2))


# In[2]:


nums = [1, 4, 3, 2]

maximized_sum = solve(nums)

print(maximized_sum)


# In[18]:


# Ans 3) code to find the length of the longest harmonious subsequence in an array in Python
def longest_harmonious_subsequence(nums):
    max_map = {}
    min_map = {}

    for num in nums:
        if num not in max_map:
            max_map[num] = 1
        else:
            max_map[num] += 1

        if num not in min_map:
            min_map[num] = 1
        else:
            min_map[num] += 1

    longest = 0
    for num, count in max_map.items():
        if num in min_map and num - min_map[num] == 1:
            longest = max(longest, count)

    return longest


# In[19]:


nums = [1, 3, 2, 2, 5, 2, 3, 7]

longest_harmonious_subsequence = longest_harmonious_subsequence(nums)

print(longest_harmonious_subsequence)


# In[20]:


# Ans 4) code to determine if n new flowers can be planted in a flowerbed in Python
def canPlaceFlowers(flowerbed, n):
    count = 0
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
            count += 1
            flowerbed[i] = 1
    return count >= n


# In[22]:


flowerbed = [1, 0, 0, 0, 1]
n = 1

canPlaceFlowers(flowerbed, n)


# In[24]:


# Ans 5)code to find the maximum product of three numbers in an array
def maximumProduct(nums):
    nums.sort()
    return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])


# In[25]:


nums = [1, 2, 3]

maximumProduct(nums)


# In[26]:


# Ans 6) code to search for a target in a sorted array
def search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# In[27]:


nums = [-1, 0, 3, 5, 9, 12]
target = 9

search(nums, target)


# In[28]:


# Ans 7) 
def isMonotonic(nums):
    return (all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1)) or
            all(nums[i] >= nums[i + 1] for i in range(len(nums) - 1)))


# In[29]:


nums = [1, 2, 2, 3]

isMonotonic(nums)


# In[36]:


# Ans 8) code to find the minimum score of an array
def min_score(nums, k):
    min_val = nums[0]
    max_val = nums[0]

    for i in range(1, len(nums)):
        min_val = min(min_val, nums[i] - k)
        max_val = max(max_val, nums[i] + k)

    return max_val - min_val


# In[37]:


nums = [1]
k = 0

min_score(nums, k)


# In[ ]:




