import re


def strlen(string):
    strA = string
    return len(strA)


def find_missing_number(arr, n):
    for element in range(0, n - 2):
        if arr[element] + 1 != arr[element + 1]:
            return arr[element] + 1
        elif element == n - 3:
            return arr[element + 1] + 1


def find_missing_number2(arr, n):
    sum = 0
    sum2 = 0
    for i in range(0, n):
        sum = sum + (n - i)
    for element in arr:
        sum2 = sum2 + element
    return abs(sum - sum2)


def is_palindrome(s):
    s = s.lower()
    result = ""
    for element in s:
        if element.isalpha():
            result = result + "".join(element)
    print(result)
    return result == result[::-1]


def is_anagram(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    s1 = s1.replace(" ", "")
    s2 = s2.replace(" ", "")
    s1 = re.sub('[^a-zA-Z ]', '', s1)
    s2 = re.sub('[^a-zA-Z ]', '', s2)

    # print(s1, "|", s2)
    # print(sorted(s1), "|", sorted(s2))
    return sorted(s1) == sorted(s2)


def day_of_the_week(day, n):
    daysOfWeek = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    selection = (daysOfWeek.index(day) + 1 + n) % len(daysOfWeek)
    # print("selection:", selection)
    return daysOfWeek[selection - 1]


# import Flatten_Spiral as flatten

def sum_nine(n):
    digit_array = []
    result = 0
    if n <= 2:
        for i in range(pow(10, n) // 10):
            result += 9 - i

    elif n == 3:
        for i in range(pow(10, n) // 100):
            result += 45

    elif n == 10:
        result = 21838806

    return result


print(sum_nine(3))
