from collections import defaultdict

def group_anagrams(a):
    dfdict = defaultdict(list)
    print(dfdict)
    for i in a:
        sorted_i = " ".join(sorted(i))
        print(sorted_i)
        dfdict[sorted_i].append(i)
    return dfdict.values()

a = ["tea", "eat", "bat", "ate", "arc", "car"]
print(group_anagrams(a))