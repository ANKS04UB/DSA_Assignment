#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1. Write a Python program to reverse a string without using any built-in string reversal functions.
def reverse_string(string):
    reversed_string = ""
    for i in range(len(string) - 1, -1, -1):
        reversed_string += string[i]
    return reversed_string


# In[3]:


string="Ankush"
reverse_string(string)


# In[4]:


# 2. Implement a function to check if a given string is a palindrome
def is_palindrome(string):
    if len(string) == 0:
        return True
    elif len(string) == 1:
        return True
    else:
        for i in range(len(string) // 2):
            if string[i] != string[len(string) - i - 1]:
                return False
        return True


# In[5]:


string="hashsah"
is_palindrome(string)


# In[6]:


# 3.Write a program to find the largest element in a given list
def find_largest_element(list):
    largest = list[0]
    for element in list:
        if element > largest:
            largest = element
    return largest


# In[7]:


list=[4,6,8,4,7,9,5,8,90]
find_largest_element(list)


# In[8]:


# 4. Implement a function to count the occurrence of each element in a list.
def count_occurrences(list):
    count = {}
    for element in list:
        if element in count:
            count[element] += 1
        else:
            count[element] = 1
    return count


# In[9]:


list=[7,5,3,6,7,4,3,6,7,4]
count_occurrences(list)


# In[10]:


# 5. Write a Python program to find the second largest number in a list
def find_second_largest(list):
    largest = list[0]
    second_largest = list[0]
    for element in list:
        if element > largest:
            second_largest = largest
            largest = element
        elif element > second_largest:
            second_largest = element
    return second_largest


# In[11]:


list=[5,3,3,6,8,4,34,22,97]
find_second_largest(list)


# In[12]:


# 6.Implement a function to remove duplicate elements from a list.
def remove_duplicates(list):
    unique_list = []
    for element in list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list


# In[13]:


list=[5,3,3,6,8,4,34,22,97]
remove_duplicates(list)


# In[14]:


# 7. Write a program to calculate the factorial of a given number.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# In[15]:


factorial(5)


# In[16]:


# 8.  Implement a function to check if a given number is prime
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# In[17]:


is_prime(8)


# In[18]:


# 9. Write a Python program to sort a list of integers in ascending order.
def sort_list(list):
    list.sort()
    return list


# In[19]:


list=[5,3,3,6,8,4,34,22,97]
sort_list(list)


# In[20]:


# 10. Implement a function to find the sum of all numbers in a list.
def sum_list(list):
    sum = 0
    for element in list:
        sum += element
    return sum


# In[21]:


list=[5,3,3,6,8,4,34,22,97]
sum_list(list)


# In[22]:


# 11. Write a program to find the common elements between two lists
def find_common_elements(list1, list2):
    common_elements = []
    for element in list1:
        if element in list2:
            common_elements.append(element)
    return common_elements


# In[23]:


list1=[5,3,3,6,8,4,34,22,97]
list2=[7,5,3,6,7,4,3,6,7,4]
find_common_elements(list1, list2)


# In[24]:


# 12. Implement a function to check if a given string is an anagram of another string
def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    str1 = sorted(str1)
    str2 = sorted(str2)
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False
    return True


# In[25]:


str1='Ankush'
str2='Borkar'
is_anagram(str1, str2)


# In[26]:


# 13.Write a Python program to generate all permutations of a given string
def generate_permutations(string):
    if len(string) == 0:
        return []
    if len(string) == 1:
        return [string]
    permutations = []
    for i in range(len(string)):
        for permutation in generate_permutations(string[:i] + string[i + 1:]):
            permutations.append(string[i] + permutation)
    return permutations


# In[27]:


str="abc"
generate_permutations(str)


# In[1]:


# 14.Implement a function to calculate the Fibonacci sequence up to a given number of terms
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# In[2]:


fibonacci(12)


# In[3]:


# 15. Write a program to find the median of a list of numbers.
def median(nums):
    nums.sort()
    n = len(nums)
    if n % 2 == 0:
        return (nums[n // 2] + nums[n // 2 - 1]) / 2
    else:
        return nums[n // 2]


# In[4]:


list1=[5,3,3,6,8,4,34,22,97]
median(list1)


# In[5]:


# 16. Implement a function to check if a given list is sorted in non-decreasing order.
def is_sorted(nums):
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True


# In[7]:


list1=[5,3,3,6,8,4,34,22,97]
is_sorted(list1)


# In[8]:


# 17.Write a Python program to find the intersection of two lists.
def intersection(list1, list2):
    result = []
    for item in list1:
        if item in list2:
            result.append(item)
    return result


# In[9]:


list1=[5,3,3,6,8,4,34,22,97]
list2=[7,5,3,6,7,4,3,6,7,4]
intersection(list1, list2)


# In[10]:


# 18 Implement a function to find the maximum subarray sum in a given list
def max_subarray_sum(nums):
    max_ending_here = max_so_far = nums[0]
    for i in range(1, len(nums)):
        max_ending_here = max(nums[i], max_ending_here + nums[i])
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


# In[11]:


list1=[5,3,3,6,8,4,34,22,97]
max_subarray_sum(list1)


# In[12]:


#19. Write a program to remove all vowels from a given string
def remove_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    new_str = ''
    for char in str:
        if char not in vowels:
            new_str += char
    return new_str


# In[13]:


str="Ankush"
remove_vowels(str)


# In[14]:


# 20.Implement a function to reverse the order of words in a given sentence
def reverse_words(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)


# In[15]:


sentence="My name is ankush"
reverse_words(sentence)


# In[16]:


# 21. Write a Python program to check if two strings are anagrams of each other.
def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    str1 = sorted(str1)
    str2 = sorted(str2)
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False
    return True


# In[17]:


str1="abcd"
str2="brcde"
is_anagram(str1, str2)


# In[18]:


# 22.  Implement a function to find the first non-repeating character in a string.
def first_non_repeating_char(str):
    char_count = {}
    for char in str:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    for char in str:
        if char_count[char] == 1:
            return char


# In[19]:


str="acbddgeds"
first_non_repeating_char(str)


# In[20]:


#23.Write a program to find the prime factors of a given number
def prime_factors(n):
    factors = []
    for i in range(2, n + 1):
        while n % i == 0:
            factors.append(i)
            n = n // i
    return factors


# In[22]:


prime_factors(45)


# In[23]:


# 24. Implement a function to check if a given number is a power of two.
def is_power_of_two(n):
    if n == 0:
        return False
    while n % 2 == 0:
        n = n // 2
    return n == 1


# In[24]:


is_power_of_two(65)


# In[25]:


# 25. Write a Python program to merge two sorted lists into a single sorted list
def merge_lists(list1, list2):
    result = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    while i < len(list1):
        result.append(list1[i])
        i += 1
    while j < len(list2):
        result.append(list2[j])
        j += 1
    return result


# In[26]:


list1=[5,3,3,6,8,4,34,22,97]
list2=[7,5,3,6,7,4,3,6,7,4]
merge_lists(list1, list2)


# In[27]:


# 26. Implement a function to find the mode of a list of numbers.
def mode(nums):
    count = {}
    for num in nums:
        if num not in count:
            count[num] = 1
        else:
            count[num] += 1
    max_count = max(count.values())
    mode = [key for key, value in count.items() if value == max_count]
    return mode[0]


# In[28]:


list2=[7,5,3,6,7,4,3,6,7,4]
mode(list2)


# In[29]:


# 27. Write a program to find the greatest common divisor (GCD) of two numbers
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# In[30]:


a=45
b=67
gcd(a, b)


# In[31]:


# 28. Implement a function to calculate the square root of a given number
def sqrt(n):
    if n < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    low = 0
    high = n
    while low <= high:
        mid = (low + high) // 2
        if mid * mid == n:
            return mid
        elif mid * mid < n:
            low = mid + 1
        else:
            high = mid - 1
    return mid


# In[32]:


sqrt(78)


# In[33]:


#29. Write a Python program to check if a given string is a valid palindrome ignoring non-alphanumeric characters.
def is_palindrome(string):
    # Remove all non-alphanumeric characters from the string.
    string = ''.join(c for c in string if c.isalnum())
    # Reverse the string.
    reversed_string = string[::-1]
    # Check if the string is equal to its reversed version.
    return string == reversed_string


# In[34]:


string="malaalam"
is_palindrome(string)


# In[35]:


# 30. Implement a function to find the minimum element in a rotated sorted list.
def find_min(nums):
    low = 0
    high = len(nums) - 1
    while low < high:
        mid = (low + high) // 2
        if nums[mid] > nums[high]:
            low = mid + 1
        else:
            high = mid
    return nums[low]


# In[36]:


list=[3,5,7,8,9,35,67]
find_min(list)


# In[37]:


# 31. Write a program to find the sum of all even numbers in a list
def sum_even_numbers(nums):
    sum = 0
    for num in nums:
        if num % 2 == 0:
            sum += num
    return sum


# In[38]:


list=[3,5,7,8,9,35,67]
sum_even_numbers(list)


# In[39]:


# 32. Implement a function to calculate the power of a number using recursion.
def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent == 1:
        return base
    else:
        return base * power(base, exponent - 1)


# In[40]:


base=4
exponent=3
power(base, exponent)


# In[41]:


# 33.Write a Python program to remove duplicates from a list while preserving the order.
def remove_duplicates(nums):
    seen = set()
    new_nums = []
    for num in nums:
        if num not in seen:
            seen.add(num)
            new_nums.append(num)
    return new_nums


# In[42]:


list2=[7,5,3,6,7,4,3,6,7,4]
remove_duplicates(list2)


# In[43]:


# 34. Implement a function to find the longest common prefix among a list of strings.
def longest_common_prefix(strings):
    if not strings:
        return ""
    prefix = strings[0]
    for string in strings[1:]:
        while not string.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix


# In[48]:


string="Mr. ankush"
longest_common_prefix(string)


# In[49]:


# 35. Write a program to check if a given number is a perfect square.
def is_perfect_square(num):
    if num < 0:
        return False
    root = num ** 0.5
    return root == int(root)


# In[50]:


is_perfect_square(25)


# In[51]:


# 36.  Implement a function to calculate the product of all elements in a list.
def product(nums):
    product = 1
    for num in nums:
        product *= num
    return product


# In[53]:


list2=[7,5,3,6,7,4,3,6,7,4]
product(list2)


# In[54]:


# 37. Write a Python program to reverse the order of words in a sentence while preserving the word order
def reverse_words(sentence):
    words = sentence.split(" ")
    reversed_words = words[::-1]
    return " ".join(reversed_words)


# In[55]:


sentence="Borkar sirname is cool"
reverse_words(sentence)


# In[56]:


# 38. Implement a function to find the missing number in a given list of consecutive numbers.
def find_missing_number(nums):
    expected_sum = (len(nums) + 1) * (len(nums) + 2) // 2
    return expected_sum - sum(nums)


# In[58]:


list2=[7,5,3,6,7,4,3,6,7,4]
find_missing_number(list2)


# In[59]:


# 39. Write a program to find the sum of digits of a given number.
def sum_of_digits(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return sum


# In[60]:


sum_of_digits(46)


# In[61]:


# 40. Implement a function to check if a given string is a valid palindrome considering case sensitivity
def is_palindrome(string):
    reversed_string = string[::-1]
    return string == reversed_string


# In[62]:


string="Marodadoram"
is_palindrome(string)


# In[63]:


# 41. Write a Python program to find the smallest missing positive integer in a list.
def find_smallest_missing_positive_integer(nums):
    for i in range(1, len(nums) + 2):
        if i not in nums:
            return i


# In[64]:


list2=[7,5,3,6,7,4,3,6,7,4]
find_smallest_missing_positive_integer(list2)


# In[65]:


# 42. Implement a function to find the longest palindrome substring in a given string
def longest_palindrome(string):
    longest_palindrome = ""
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            if string[i:j] == string[i:j][::-1]:
                if len(string[i:j]) > len(longest_palindrome):
                    longest_palindrome = string[i:j]
    return longest_palindrome


# In[66]:


string="nopalindromr"
longest_palindrome(string)


# In[67]:


# 43. Write a program to find the number of occurrences of a given element in a list.
def count_occurrences(list, element):
    count = 0
    for item in list:
        if item == element:
            count += 1
    return count


# In[69]:


list2=[7,5,3,6,7,4,3,6,7,4]
element=7
count_occurrences(list2, element)


# In[70]:


# 44.  Implement a function to check if a given number is a perfect number.
def is_perfect_number(num):
    factors = []
    for i in range(1, num):
        if num % i == 0:
            factors.append(i)
    sum_of_factors = sum(factors)
    return sum_of_factors == num


# In[71]:


is_perfect_number(45)


# In[72]:


# 45. Write a Python program to remove all duplicates from a string.
def remove_duplicates(string):
    seen = set()
    new_string = ""
    for char in string:
        if char not in seen:
            new_string += char
            seen.add(char)
    return new_string


# In[73]:


string="Moramona"
remove_duplicates(string)


# In[74]:


# 46. Implement a function to find the first missing positive
def find_first_missing_positive(nums):
    for i in range(len(nums)):
        if nums[i] != i + 1:
            for j in range(i + 1, len(nums)):
                if nums[j] == i + 1:
                    nums[i], nums[j] = nums[j], nums[i]
                    break
    return nums[i] + 1


# In[75]:


list2=[7,5,3,6,7,4,3,6,7,4]
find_first_missing_positive(list2)


# In[ ]:




