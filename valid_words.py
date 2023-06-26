from collections import Counter

def valid_words(input_string, wordDict):
    wordSet = set(wordDict)
    subsets = []
    permutations = []
    res = []
    
    # get subsets for input string 
    find_subsets(input_string, [], 0, subsets)

    # for each subset get the permutations and check for duplicates
    for subset in subsets:
        permute(subset, permutations)
    
    for word in permutations:
        # check if word is valid English word
        if word in wordSet:
            res.append(word)

    return res

def find_subsets(s, subset, i, subsets):
    if i >= len(s):            
        subsets.append(subset[::])
        return

    subset.append(s[i])
    find_subsets(s, subset, i + 1, subsets)
    subset.pop()
    
    # excludes duplicates
    while i + 1 < len(s) and s[i] == s[i + 1]:
        i += 1
        
    find_subsets(s, subset, i + 1, subsets)

def permute(word, res):
    perm = []
    count = Counter(word)

    def backtrack():
        if len(perm) == len(word):
            res.append(''.join(perm[::]))
            return

        for n in count:
            if count[n] > 0:
                perm.append(n)
                count[n] -= 1

                backtrack()

                count[n] += 1
                perm.pop()
    backtrack()
    return res


# Test the function
input_string = "oogd"
dictionary = ["go", "good", "god", "dog", "do", "log", "loop"]
words = valid_words(input_string, dictionary)
print(words)

'''
We can also go with Python library itertools powerset O(2^n), then find permutations O(n!) of the subsets, and finally check against valid English words. 
Though I think the best solution to this if we know all possible words is to build a trie O(n) then search words using the given characters. Searching a Trie would be fastest O(k)
'''