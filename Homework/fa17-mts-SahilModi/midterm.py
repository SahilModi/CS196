###################
#	Midterm
#	Due: Tuesday, November 28 2017
###################

# Array Almost Product
#
# Write a function that, given a list of integers, will return a list of
# integers 'output' wherein the value of output[i] is the product of all the
# numbers in the input array except for input[i].
#
# You will lose points if your solution uses division.
# Your solution should run in O(n) time.
# Your solution should not allocate any space other than the output list.
#
# Example(s)
# ----------
# Example 1:
#   Input: [2,3,4,5]
#       Output should be [3*4*5, 2*4*5, 2*3*4]
#   Output: [60, 40, 30, 24]
#
# Example 2:
#   Input: [3,6,9,-3,2,-2]
#   Output:
#   [648, 324, 216, -648, 972, -972]
#
# Parameters
# ----------
# arr : List[int]
#   A list of integers, with len(arr) > 1
#
# Returns
# -------
# List[int]
#   Returns a list where every element of the list is the product of
#   all the numbers in the input list except for the number at the index
#   being evaluated.
#


# O(2n), Done
def array_almost_product(arr):
    result_arr = []
    running_product = 1
    length_arr = len(arr)
    for i in range(length_arr):
        result_arr.append(running_product)
        running_product *= arr[i]

    running_product = 1
    for i in range(length_arr - 1, -1, -1):
        result_arr[i] *= running_product
        running_product *= arr[i]

    return result_arr


# Pascal's Triangle
#
# Write a function that, given an index i, returns the i'th row of Pascal's Triangle.
#
# This Wikipedia page on Pascal's triangle may be useful:
#   https://en.wikipedia.org/wiki/Pascal%27s_triangle
#
# Your solution should run in O(i) time and use O(i) space.
#
# Example(s)
# ----------
# Example 1:
#   Input: 2
#   Output: [1,2,1]
#
# Example 2:
#   Input: 6
#   Output: [1,6,15,20,15,6,1]
#
# Parameters
# ----------
# i : int
#   The row index of the row of Pascal's Triangle you are searching for
#
# Returns
# -------
# List[int]
#   Returns the i'th row of Pascal's Triangle as a list of ints
#

# Done?
def pascals_triangle(row_num):
    result_row = [1]
    for i in range(row_num):
        temp_num_1 = result_row[i] * (row_num - i)
        temp_num_2 = temp_num_1 // (i + 1)
        # result_row.append(round(result_row[i] * (row_num - i) / (i + 1)))
        result_row.append(temp_num_2)
    return result_row


# Alive People
#
# Write a function that, given a list of strings representing a person's birth year: age of death,
# will return the year that had the most people alive (inclusive).
# If there are multiple years that tie, return the earliest.
# You can think of a birthdate and a deathdate as a range of years.
# Of all the birth years in the list, find the one where the highest
# amount of people in the list were still alive.
#
# Examples
# ----------
# Example 1:
#   Input: ["1920: 80", "1940: 22", "1961: 10"]
#   Output: 1961
#
# Example 2:
#   Input: ["2000: 46", "1990: 17", "1200: 97", "1995: 20"]
#   Output: 2000
#
# Parameters
# ----------
# people : List[string]
#   A list of strings each representing a birth year and final age
#
#
# Returns
# -------
# int
#   Returns earliest year with the most people alive
#

# Done, O(n^somewhat_good)
def alive_people(people):
    import re
    birth_death_map = {}  # Birth Year : Death Year
    earliest_born = 0
    latest_death = 0
    alive_count_map = {}  # Year : Count of people alive during year
    highest_count = 0
    highest_count_year = 0

    # convert input into an integer array
    for i in range(len(people)):
        person = people[i]
        # temp_birth_string = ""
        # temp_death_string = ""
        # colon_index = len(person)

        for j in range(len(person)):
            # if person[j] != ':' and j < colon_index:
            #     temp_birth_string += person[j]
            # elif person[j] == ':':
            #     colon_index = j
            # elif j > colon_index + 1:
            #     temp_death_string += person[j]
            #
            # if j == len(person) - 1:
                # death_date = int(temp_birth_string) + int(temp_death_string)
                # if death_date > latest_death:
                #     latest_death = death_date
                # if int(temp_birth_string) < earliest_born:
                #     earliest_born = int(temp_birth_string)
                # birth_death_map[int(temp_birth_string)] = death_date

            split_string_arr = re.split('[:]', person)
            birth_date = int(split_string_arr[0])
            death_date = birth_date + int(split_string_arr[1])

            if i == 0:
                earliest_born = birth_date
                latest_death = death_date
            else:
                if death_date > latest_death:
                    latest_death = death_date
                if birth_date < earliest_born:
                    earliest_born = birth_date
            birth_death_map[birth_date] = death_date

    for year in range(earliest_born, latest_death + 1):
        for key in birth_death_map:
            # If year is in between birth year and death year
            if year in range(key, birth_death_map[key] + 1):
                if alive_count_map.get(year, 0) == 0:
                    alive_count_map[year] = 1
                else:
                    alive_count_map[year] += 1

                if alive_count_map[year] > highest_count:
                    highest_count = alive_count_map[year]
                    highest_count_year = year

                if highest_count == len(people):
                    return highest_count_year

    return highest_count_year


# String, My One True Love
#
# Your favorite course staff member really likes strings that have the same occurences of letters.
# This means the staff member likes "aabbcc" and "ccddee" and even strings like "abcabcabc"
#
# But the person who wrote all of your homework wants to trick the staff with really long string,
# that either could be the string that the staff member likes, or something that becomes such a string
# when you remove a single character from the string.
#
# Your goal is to return True if it's a string that the homework creator made
# and False otherwise.
#
# Restrictions
# ------------
# Inputs are only given as lower case alphabets, without punctuation, spaces, etc.
# Your solution must run in O(n) time.
#
# Example(s)
# ----------
# Example 1:
#   Input: "abcbabcdcdda"
#   There is 3 a's, 3 b's, 3 c's, and 3 d's. That means it is a very likable string!
#   Output:
#   True
#
# Example 2:
#   Input: "aaabbbcccddde"
#   Again there are 3 a's, 3 b's, 3 c's, and 3 d's. However, we also have 1 e!
#   We can remove this string however, and it will become a likeable string, so this is valid.
#   Output:
#   True
#
# Example 3:
#   Input: "aaabbbcccdddeeffgg"
#   This string is similar to the other ones, except with 2 e's, f's and g's at the end.
#   To make this string likable, we need to remove the 2 e's, f's, and g's or we can remove
#   one a, b, c, and d. However all of these require more than one removal, so it becomes invalid.
#   Output:
#   False
#
# Parameters
# ----------
# the_string : str
#   The string to check whether it is likeable or not.
#
# Returns
# -------
# bool
#   True if the string is likable, or removing a single character makes it likable.
#   False if the string is not likeable, and we need to remove more than 1 character to become likable.


# character distribution?, Done
def string_my_one_true_love(the_string):
    char_count_map = {}
    last_char_count = ''
    total = 0
    length_string = len(the_string)
    for i in range(length_string):
        char = the_string[i:i + 1]
        if char_count_map.get(char, 0) == 0:
            char_count_map[char] = 1
        else:
            char_count_map[char] += 1
        last_char_count = char_count_map[char]

    last_index = True
    for count in char_count_map:
        if last_char_count != char_count_map[count] and last_index:
            last_char_count = char_count_map[count]
        char_count_map[count] -= last_char_count
        total += char_count_map[count]
        last_index = False

    return total == 0 or total == 1 or total == -last_char_count + 1


# Longest Palindromic Substring
#
# Given a string, find the longest substring that is a palindrome. If
#
# Ideal runtime: o(n), but we will give full credit for o(n^2) solutions.
#
# RESTRICTIONS:
# There is guaranteed to be exactly 1 longest palindrome
#
# Example(s)
# ----------
# Example 1:
#   Input: "ABBAC"
#
#   Output:
#   "ABBA"
#
# Example 2:
#   Input: "A"
#
#   Output:
#   "A"
#
# Parameters
# ----------
# word: str
#   String input
#
# Returns
# -------
# String
#    Longest Palindrome substring
def longest_palindrome_substring(word):
    longest_palindrome = ""
    length_word = len(word)

    if length_word == 1:
        return word

    for i in range(length_word):
        for j in range(0, i):
            chunk = word[j:i + 1]
            # chunk_no_space = ''.join([char for char in chunk if (char.isalpha())])  # removes spaces
            if chunk == chunk[::-1] and len(chunk) > len(longest_palindrome):
                longest_palindrome = chunk

    return longest_palindrome


# Longest Unique Substring
#
# Given a string, find the longest unique substring
#
# Ideal runtime: o(n). full credit only given for o(n).
# Do not consider case. Therefore, 'A' and 'a' are considered the same character
#
# RESTRICTIONS:
# There is guaranteed to be exactly 1 longest unique substring
#
# Example(s)
# ----------
# Example 1:
#   Input: "zzAabcdefFgg"
#
#   Output:
#   "abcdef"
#
# Example 2:
#   Input: "AA"
#
#   Output:
#   "A"
#
# Parameters
# ----------
# word: str
#   String input
#
# Returns
# -------
# String
#    Longest unique substring

# Done, O(??)
def longest_unique_substring(word):
    char_arr = list(word)
    char_seen_map = {}
    results_arr = []
    j = 0
    i = 0
    result = ""

    while i < len(word) and j < len(word):
        current_char = char_arr[j]

        if not char_seen_map.get(current_char.lower(), False):
            char_seen_map[current_char.lower()] = True
            result += current_char
            j += 1
        else:
            i += 1
            j = i
            results_arr.append(result)
            result = ""
            char_seen_map.clear()

    result = results_arr[0]
    for k in range(len(results_arr)):
        if len(results_arr[k]) > len(result):
            result = results_arr[k]
    return result


# Three Sum
#
# Given an array S of n integers and constant 'target', are there elements a, b, c in S such that
# a+b+c = target? Find all unique triplets in the array which gives the sum of target.
# return a 2d list, where all inner lists are triplets. There may be more than
# one pair of triplets.
#
# Runtime: o(n^2) will get full credit.
#
#
# Example(s)
# ----------
# Example 1:
#   Input: [-1, 0, 1, 2, -1, -4], 0
#
#   Output:
#   [
#  [-1, 0, 1],
#  [-1, -1, 2]
#   ]
#
#
# Parameters
# ----------
# arr: array
#   array of numbers
#
# target: int
#   target integer
#
# Returns
# -------
# 2d array
#    2d list, inner lists are triplets that add up to target.


# Done
def three_sum(arr, target):
    result_arr = []
    result_map = {}
    temp_str = ""
    for a in range(len(arr)):
        a_num = arr[a]
        for i in range(a, len(arr) - 2):
            b_num = arr[i + 1]
            c_num = arr[i + 2]
            if a_num + b_num + c_num == target:
                temp_arr = sorted([a_num, b_num, c_num], key=int)
                for k in range(len(temp_arr)):
                    temp_str += str(temp_arr[k])
                if not result_map.get(temp_str, False):
                    result_arr.append([a_num, b_num, c_num])
                    result_map[temp_str] = True
                temp_str = ""

    return result_arr


# Zero Sum
#
# Return True if a sub array (not any element) summed can create 0.
# Otherwise return False.
#
# Time Complexity
# ------------
# Optimal time complexity is O(n). You can assume the running time of updating a dictionary is O(1)
#
# You CANNOT assume the order given will be sorted.
#
# Example(s)
# ----------
# Example 1:
#   Input: zero_sum([0, 1, 2, 3, 4, 5])
#   We need to see if a subarray can create 0.
#   The first element gives us 0. So there is a subarray that can create 0.
#   Output:
#   True
#
# Example 2:
#   Input: zero_sum([10, 20, -20, 3, 21, 2, -6])
#   We need to see if a subarray can create 0.
#   The subarray [20, -20] can create zero.
#   Output:
#   True
#
# Parameters
# ----------
# arr: array
#   array of numbers

# O(n), Done
def zero_sum(arr):
    sum_map = {}
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]

        # If prefix sum is 0 or it is already present
        # If an array has a zero sum, then the prefix sum is repeated
        if sum == 0 or sum_map.get(sum, False) is True:
            return True

        sum_map[sum] = True

    return False


# Stair Stepping
#
# One day, Alice's power went out in her house.
# Because Alice is currently in 374, she decided to count how many distinct ways she can climb up her staircase
# (from the bottom to the last stair). Alice is able to skip some stairs because she has very long legs.
# Help Alice determine the number of distinct ways she can climb up the staircase
# given the number of stairs on the staircase (stairs)
# and the maximum number of stairs she can skip at each one of her steps (skip).
#
# Time Complexity
# ---------------
# Optimal time complexity is O(stairs).
# Example 1:
# stairs = 3
# skip = 0
#
#   #
#  ##
# ###
# 123
#
# Alice cannot skip any stairs, so there is only 1 way.
# BOTTOM -> 1 -> 2 -> 3
#
# Example 2:
# stairs = 3
# skip = 1
#
#   #
#  ##
# ###
# 123
#
# Alice can skip one stair at most, so there are 3 ways.
# BOTTOM -> 1 -> 2 -> 3
# BOTTOM -> 1 -> 3
# BOTTOM -> 2 -> 3
#
# Example 3:
# stairs = 5
# skip = 2
#
#     #
#    ##
#   ###
#  ####
# #####
# 12345
#
# Alice can skip two stairs at most, so there are 13 ways.
#
# BOTTOM -> 1 -> 2 -> 3 -> 4 -> 5
# BOTTOM -> 1 -> 2 -> 3 -> 5
# BOTTOM -> 1 -> 2 -> 4 -> 5
# BOTTOM -> 1 -> 3 -> 4 -> 5
# BOTTOM -> 2 -> 3 -> 4 -> 5
# ...
# ...
# BOTTOM -> 3 -> 5
#
# Note that Alice must start at the "0th" step and finish exactly at the Nth step where N is the number of stairs.
def staircase_ways(stairs, skip):
    if skip >= stairs + 1:
        skip = stairs
    elif skip < 0:
        skip = 0
    return staircase_ways_helper(stairs + 1, skip, {})


# Helper for above method
def staircase_ways_helper(stairs, skip, lookup):
    if stairs in lookup:
        return lookup[stairs]
    result = 0
    if skip == 0:
        return 1

    if stairs == 1 or stairs == 0:
        return 1
    elif stairs < 0:
        return 0

    for i in range(1, stairs):
        if i <= skip + 1:
            result += staircase_ways_helper(stairs - i, skip, lookup)
    lookup[stairs] = result
    return result


# Odd One Out
#
# Given an array of 2n + 1 integers where each integer except one is duplicated,
# return the number that only appears once in the array.
#
# Time complexity
# ---------------
# Optimal time complexity is O(n). Try to only use O(1) space/memory.
#
# Example 1:
# arr = [10]
# Answer is 10.
#
# Example 2:
#
# arr = [3, 2, 1, 3, 2, 4, 4]
# Answer is 1.
#
#
# Example 3:
# arr = [-1, 1, 0, 5, 0, 2, 1, 2, 5]
# Answer is -1.


# Done
def odd_one_out(arr):
    arr.sort(key=int)

    for i in range(1, len(arr) - 1):
        if arr[i] != arr[i + 1] and arr[i] != arr[i - 1]:
            return arr[i]
        if i == len(arr) - 2 and arr[i] != arr[i + 1]:
            return arr[i + 1]
    return arr[0]


# Circular Shift
#
# Given an array (arr) and a shift value (k), shift the array to the
# right by k. If the rightmost element will become out of bounds, move
# it to the front of the array (hence circular shift).
#
# Time complexity
# ---------------
# Optimal complexity is O(len(arr)). Try using only O(1) space/memory
#
# Example 1:
# arr = [1, 2, 3, 4, 5]
# k = 1
# Returns [5, 1, 2, 3, 4]
#
# Example 2:
# arr = [1, 2, 3, 4, 5]
# k = 2
# Returns [4, 5, 1, 2, 3]
#
# Example 3:
# arr = [1, 2, 3]
# k = 10
# Returns [3, 1, 2]

# O(n) space, Done
def circular_shift(arr, k):
    result_arr = [0] * len(arr)
    for i in range(len(arr)):
        if i + k > len(arr) - 1:
            temp_index = (i + k) % len(arr)
        else:
            temp_index = i + k

        result_arr[temp_index] = arr[i]
    return result_arr


# Reverse Linked List
#
# Given a linked list, reverse it in-place
#
# Time Complexity
# ---------------
# Optimal time complexity is O(n). Try to use only O(1) memory.
class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def __str__(self):
        node = self
        buffer = str(node.data)

        node = node.next_node
        while node:
            buffer += ' -> ' + str(node.data)
            node = node.next_node
        return buffer


# Done
def reverse_list(head):
    curr_node = head
    prev_node = None
    while curr_node:
        next_node = curr_node.next_node
        curr_node.next_node = prev_node
        prev_node = curr_node
        curr_node = next_node
    return prev_node
