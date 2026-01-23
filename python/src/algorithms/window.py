from typing import Dict


def minWindowSubstring(n: str, k: str):
    k_dict: Dict[str, int] = {}
    for c in k:
        if c in k_dict:
            k_dict[c] += 1
        else:
            k_dict[c] = 1

    distinct_k_chars = len(k_dict.keys())
    min_window = len(k)
    min_answer = n
    l, r = 0, min_window
    while r <= len(n):
        if r - l < min_window:
            r += 1
            continue
            
        n_sub_dict: Dict[str, int] = {}
        n_sub = n[l:r]
        for c in n_sub:
            if c in n_sub_dict:
                n_sub_dict[c] += 1
            else:
                n_sub_dict[c] = 1
        
        distinct_n_sub_chars = len(n_sub_dict.keys())
        if distinct_n_sub_chars >= distinct_k_chars:
            valid = all(n_sub_dict.get(x) and n_sub_dict[x] >= k_dict[x] for x in k_dict.keys())
            if valid and len(n_sub) < len(min_answer):
                min_answer = n_sub
                l += 1
            else: 
                r += 1
        else:
            r += 1

    return min_answer

print(minWindowSubstring("ahffaksfajeeubsne", "jefaa")) # aksfaje
print(minWindowSubstring("aaffhkksemckelloe", "fhea")) # affhkkse