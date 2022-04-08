# 내가 작성한 코드

txt = input()
pat = input()
K = []

def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)

    lps = [0] * M

    computeLPS(pat, lps)

    i = 0 
    j = 0 
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1
        elif pat[j] != txt[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

        if j == M:
            K.append(i - j + 1)
            j = lps[j - 1]

def computeLPS(pat, lps):
    leng = 0 

    i = 1
    while i < len(pat):
        if pat[i] == pat[leng]:
            leng += 1
            lps[i] = leng
            i += 1
        else:
            if leng != 0:
                leng = lps[leng - 1]
            else:
                lps[i] = 0
                i += 1

KMPSearch(pat, txt)

a = len(K)

print(a)

for i in range(a):
    print(K[i], end = " ")
