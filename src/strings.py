
def reverse_words(words: str) -> str:
    word_list = words.split(' ')
    word_list.reverse()
    return ' '.join(filter(lambda x: x.strip(), word_list))


# print(reverse_words("the sky is blue"))
# print(reverse_words("  hello world  "))
# print(reverse_words("a good   example"))
# print(reverse_words("Je suis tres content"))

def halves_are_alike(s: str) -> bool:
    left_count = 0
    right_count = 0
    vowels = {'a': True, 'e': True, 'i': True, 'o': True, 'u': True, 'A': True, 'E': True, 'I': True, 'O': True, 'U': True}
    for i in range(len(s)//2):
        left = i
        right = (len(s)-1) - i
        if s[left] in vowels:
            left_count+=1
        if s[right] in vowels:
            right_count+=1

    return left_count == right_count
    
# print(halves_are_alike('book')) # True

def can_change(start: str, target: str) -> bool:
    return False

print(can_change(start = "_L__R__R_", target = "L______RR"))
print(can_change(start = "R_L_", target = "__LR"))
print(can_change(start = "_R", target = "R_"))
