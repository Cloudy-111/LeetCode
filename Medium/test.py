def frequencySort(s):
    freq = [0 for _ in range(122)]
    for i in s:
        freq[ord(i)] += 1
    for i in set(s):
        print(i, freq[ord(i)])
    return ''.join(sorted(s, key=lambda x: -freq[ord(x)]))


s = "eeaabbccatcr"
print(frequencySort(s))
