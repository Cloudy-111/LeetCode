def sortVowels(s: str) -> str:
    vowel = ''
    conso = ''
    for i in s:
        if i in 'aeiuoAEIUO':
            vowel += i
            conso += '.'
        else:
            conso += i
    vowel = sorted(vowel)
    res = ''
    k = 0
    for i in conso:
        if i == '.':
            res += vowel[k]
            k = k + 1
        else:
            res += i
    return res


s = 'lEetcOde'
print(sortVowels(s))
