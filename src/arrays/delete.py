
def firstUniqChar(s: str) -> int:
    uniques = dict()
    dups = set()
    for i in range(len(s)):
        if s[i] in dups:
            continue
        if s[i] in uniques:
            del uniques[s[i]]
            dups.add(s[i])
        else:
            uniques[s[i]] = i
    
    values = list(uniques.values())
    return min(values) if values else -1

print(firstUniqChar('leetcode')) # 0
print(firstUniqChar('aabb')) # -1
