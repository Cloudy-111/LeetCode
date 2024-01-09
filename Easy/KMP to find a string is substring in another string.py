def createLSP(prefix, size):
    lsp = [0] * size
    len = 0
    i = 1
    while i < size:
        if prefix[i] == prefix[len]:
            len += 1
            lsp[i] = len
            i += 1
        else:
            if len != 0:
                len = lsp[len - 1]
            else:
                lsp[i] = 0
                i += 1
    return lsp


def KMP(text, pattern):
    lsp = createLSP(pattern, len(pattern))
    i, j = 0, 0
    n = len(text)
    m = len(pattern)
    while i < n and j < m:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == m:
            return True
        elif i < n and text[i] != pattern[j]:
            if j > 0:
                j = lsp[j - 1]
            else:
                i += 1
    return False
