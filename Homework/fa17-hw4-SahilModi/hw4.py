"""
======================================================================
Homework 4

Released: 2017-10-17
Due Date: 2017-10-24, EoD

They told me I could be anything...
...so I became void*.
======================================================================
"""


# is unique
def is_unique(word):
    """
    Given a string, return true if the string's characters are unique.

    Args:
        (str) word: the input string.

    Returns:
        (bool) True if the string's characters are unique, False otherwise.
    """
    # word = word.lower()
    isUnique = True
    wordList = list(word)

    for i in range(len(wordList)):
        try:
            if wordList.index(wordList[i], i + 1, len(wordList)) >= 0:
                isUnique = False
                break
        except:
            pass
    return isUnique


# Counting Anagrams
def count_anagrams(arr, uniq):
    """
    Given a list of strings, returns the exact anagrams of uniq in the list.

    Args:
        (List[str]) arr:  a list of strings.
        (str)       uniq: a string.

    Returns:
        (int) the number of anagrams of uniq in arr.
    """
    uniq = uniq.lower()
    uniq = sorted(uniq)
    count = 0
    for i in range(len(arr)):
        arr[i] = arr[i].lower()
        arr[i] = sorted(arr[i])
        if uniq == arr[i]:
            count = count + 1

    return count


# Anagram of Palindrome
def anagram_of_palindrome(word):
    """
    Given a string, return true if the string is an anagram of a palindrome.

    Args:
        (str) word: the input string

    Returns:
        (bool) whether or not the input string is an anagram of a palindrome.
    """
    is_anagram = False
    word = word.lower()
    word = ''.join([char for char in word if (char.isalpha() or char == ' ')])
    one_odd_found = False

    for i in range(len(word)):
        letter = word[i]
        count = word.count(letter)
        if count % 2 == 0:
            is_anagram = True
        elif not one_odd_found:
            one_odd_found = True
        else:
            is_anagram = False
            break

    return is_anagram


# Reverse Dictionary
def reverse_dictionary(d):
    """
    Given a dictionary d, reverse its keys and values.
    The values will all be unique.

    Args:
        (Dict[Any, Any]) d: the dictionary.

    Returns:
        (Dict[Any, Any]) a dictionary where the keys of d are its values and vice-versa.
    """
    my_dict = {}
    for key in d.keys():
        my_dict[d[key]] = key
    return my_dict


# Alphabet Finder
def alphabet_finder(sentence):
    """
    Given a string, returns the shortest substring that:
        1. starts from the beginning of the string
        2. contains all the letters of the alphabet (case insensitive)
    If this is never true, return None.

    Args:
        (str) sentence: the input string

    Returns:
        (str) the shortest substring of sentence that satisfies both (1) and (2).
    """
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    sentence = sentence.lower()
    index_end = 0

    for i in range(len(alphabet)):
        tempIndex = sentence.find(alphabet[i])
        if tempIndex > index_end:
                index_end = tempIndex
        elif tempIndex == -1:
            return None


    return sentence[:index_end + 1]


# Happy Numbers
def happy_numbers(n):
    """
    Given n, return the number of happy numbers between 1 and n (inclusive).
    https://en.wikipedia.org/wiki/Happy_number

    Args:
        (int) n: the upper bound.

    Returns:
        (int) the number of happy numbers from 1 to n.
    """

    happy_number_count = 0
    MAX_RUN_AMOUNT = 50

    # CALCULATE SUM:
    for i in range(n + 1):
        temp_sum = 0
        runCount = 0
        digit_list = [int(d) for d in str(i)]
        while (runCount <= MAX_RUN_AMOUNT):
            for j in range(len(digit_list)):
                temp_sum += pow(digit_list[j], 2)
            if temp_sum == 1:
                happy_number_count += 1
                break
            digit_list = [int(d) for d in str(temp_sum)]
            temp_sum = 0
            runCount += 1

    return happy_number_count
