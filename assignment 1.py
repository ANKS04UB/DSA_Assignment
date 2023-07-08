#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Ans 1)
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [i, seen[complement]]
        else:
            seen[num] = i

    return []


# In[6]:


nums = [2, 7, 11, 15]
target = 9

indices = two_sum(nums, target)

print(indices)


# In[7]:


# Ans 2) code to remove all occurrences of a value in an array in-place in Python
def remove_val(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1

    return k


# In[8]:


nums = [3, 2, 2, 3]
val = 3

k = remove_val(nums, val)

print(nums)
print(k)


# In[9]:


# Ans 3) the code to find the index of a target value in a sorted array in Python
def search_sorted_array(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# In[10]:


nums = [1, 3, 5, 6]
target = 5

index = search_sorted_array(nums, target)

print(index)


# In[11]:


# ans 4) the code to increment a large integer represented as an array of digits in Python
def increment_integer(digits):
    carry = 1
    for i in range(len(digits) - 1, -1, -1):
        digit = digits[i] + carry
        if digit == 10:
            digit = 0
            carry = 1
        else:
            carry = 0
            digits[i] = digit

        if carry == 1:
            digits.append(1)

    return digits


# In[12]:


digits = [1, 2, 3]

incremented_digits = increment_integer(digits)

print(incremented_digits)


# In[15]:


# Ans 5) code to merge two sorted arrays in Python
def merge_sorted_arrays(nums1, m, nums2, n):
    i = 0
    j = 0
    k = 0

    while i < m and j < n:
        if nums1[i] <= nums2[j]:
            nums1[k] = nums1[i]
            i += 1
        else:
            nums1[k] = nums2[j]
            j += 1
        k += 1

    while i < m:
        nums1[k] = nums1[i]
        i += 1
        k += 1

    while j < n:
        nums1[k] = nums2[j]
        j += 1
        k += 1


# In[16]:


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

merge_sorted_arrays(nums1, m, nums2, n)

print(nums1)


# In[17]:


# Ans 6) code to check if any value appears at least twice in an array in Python
def contains_duplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True
        else:
            seen.add(num)

    return False


# In[18]:


nums = [1, 2, 3, 1]

contains_duplicate(nums)


# In[19]:


# Ans 7) code to move all 0's to the end of an array in Python
def move_zeros(nums):
    i = 0
    j = 0

    while i < len(nums):
        if nums[i] != 0:
            nums[j] = nums[i]
            j += 1
        i += 1

    while j < len(nums):
        nums[j] = 0
        j += 1

    return nums


# In[20]:


nums = [0, 1, 0, 3, 12]

move_zeros(nums)

print(nums)


# In[21]:


# Ans 8) code to find the number that occurs twice and the number that is missing in an array in Python
def find_duplicate_and_missing(nums):
    seen = set()
    duplicate = None
    missing = None

    for num in nums:
        if num in seen:
            duplicate = num
        else:
            seen.add(num)

    for i in range(1, len(nums) + 1):
        if i not in seen:
            missing = i

    return [duplicate, missing]


# In[22]:


nums = [1, 2, 2, 4]

duplicate_and_missing = find_duplicate_and_missing(nums)

print(duplicate_and_missing)


# In[ ]:




