#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Ans 1) the code to find three integers in an array whose sum is closest to a given target
def threeSumClosest(nums, target):
    nums.sort()
    res = float('inf')
    for i in range(len(nums)):
        l = i + 1
        r = len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if abs(s - target) < abs(res - target):
                res = s
            if s < target:
                l += 1
            elif s > target:
                r -= 1
            else:
                return s
    return res


# In[3]:


nums = [-1, 2, 1, -4]
target = 1

threeSumClosest(nums, target)


# In[4]:


# Ans 4) code to find all the quadruplets in an array whose sum is equal to a given target
def fourSum(nums, target):
    nums.sort()
    res = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            l = j + 1
            r = len(nums) - 1
            while l < r:
                s = nums[i] + nums[j] + nums[l] + nums[r]
                if s == target:
                    res.append([nums[i], nums[j], nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
    return res


# In[5]:


nums = [1, 0, -1, 0, -2, 2]
target = 0
fourSum(nums, target)


# In[6]:


# Ans 3) code to find the next permutation of an array
def nextPermutation(nums):
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    if i >= 0:
        j = len(nums) - 1
        while j >= 0 and nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1:] = nums[i + 1:][::-1]


# In[8]:


nums = [1, 2, 3]

nextPermutation(nums)

print(nums)


# In[9]:


# Ans 4) code to find the index of a target in a sorted array
def searchInsert(nums, target):
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return l


# In[10]:


nums = [1, 3, 5, 6]
target = 5

searchInsert(nums, target)


# In[11]:


# Ans 5) code to increment a large integer represented as an integer array
def plusOne(digits):
    n = len(digits)
    carry = 1
    for i in range(n - 1, -1, -1):
        digits[i] += carry
        carry = digits[i] // 10
        digits[i] %= 10
    if carry:
        digits.insert(0, 1)
    return digits


# In[12]:


digits = [1, 2, 3]

plusOne(digits)

print(digits)


# In[13]:


# Ans 6) code to find the single element in an array
def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result


# In[14]:


nums = [2, 2, 1]

singleNumber(nums)


# In[15]:


# Ans 7) 
def findMissingRanges(nums, lower, upper):
    ranges = []
    prev = lower - 1
    for num in nums:
        if num > prev + 1:
            ranges.append([prev + 1, num - 1])
        prev = num
    if prev < upper:
        ranges.append([prev + 1, upper])
    return ranges


# In[16]:


nums = [0, 1, 3, 50, 75]
lower = 0
upper = 99

findMissingRanges(nums, lower, upper)


# In[17]:


# Ans 10)  code to determine if a person could attend all meetings in an array
def canAttendMeetings(intervals):
    intervals.sort(key=lambda x: x[0])
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False
    return True


# In[18]:


intervals = [[0, 30], [5, 10], [15, 20]]

canAttendMeetings(intervals)


# In[ ]:




