hashmap = {'hello': 'world'}
print(hashmap['hello'])

def count_characters():
    inputStr = 'AABCCHELLO'
    for c in inputStr:
        hashmap[c] = inputStr.count(c)

    for key in hashmap.keys():
        print(key + ': ', hashmap[key])

count_characters()