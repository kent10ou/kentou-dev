'''
to return a list of valid dictionary words given an input_string, run `valid_words(input_string, dictionary)`
valid_words() will find all subsets of the given input string and then find all permutations of the subsets
finally, it will check all permutations against the dictionary and return a list of string that matches.
'''

from collections import Counter

# returns a list of valid English word from a given input string
def valid_words(input_string, word_dict):
    word_set = set(word_dict)
    subsets = []
    permutations = []
    res = []
    
    # find all subsets excluding duplicates
    find_subsets(input_string, [], 0, subsets)

    # for each subset get the permutations 
    for subset in subsets:
        permute(subset, permutations)
    
    # check if word in permutations is a valid English word
    for word in permutations:
        if word in wordSet:
            res.append(word)

    return res

# returns the subsets for a given input string and exclude duplicates -> List[List[string]]
# ex. subsets of 'abc': [['a', 'b', 'c'], ['a', 'b'], ['a', 'c'], ['a'], ['b', 'c'], ['b'], ['c'], []]
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

# returns the permutations of word and join the string -> List[string]
# ex. permutation of ['a', 'b', 'c']: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
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
# input_string = "oogd"
# dictionary = ["go", "good", "god", "dog", "do", "log", "loop"]
# words = valid_words(input_string, dictionary)
# print(words)

'''
subsets: [['o', 'o', 'g', 'd'], ['o', 'o', 'g'], ['o', 'o', 'd'], ['o', 'o'], ['o', 'g', 'd'], ['o', 'g'], ['o', 'd'], ['o'], ['g', 'd'], ['g'], ['d'], []]
permutations: ['oogd', 'oodg', 'ogod', 'ogdo', 'odog', 'odgo', 'good', 'godo', 'gdoo', 'doog', 'dogo', 'dgoo', 'oog', 'ogo', 'goo', 'ood', 'odo', 'doo', 'oo', 'ogd', 'odg', 'god', 'gdo', 'dog', 'dgo', 'og', 'go', 'od', 'do', 'o', 'gd', 'dg', 'g', 'd', '']

We can also go with Python library itertools powerset O(2^n), then find permutations O(n!) of the subsets, and finally check against valid English words. 
Though I think the best solution to this if we know all possible words is to build a trie O(n) then search words using the given characters. Searching a Trie would be fastest O(k)
'''
