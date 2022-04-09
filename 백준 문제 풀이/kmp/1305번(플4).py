n = int(input())
pat = input()
lps = [0] * n

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
                leng = lps[leng-1]
            else:
                lps[i] = 0
                i += 1

computeLPS(pat, lps)

a = lps[n - 1]

b = len(pat[0 : (n - a)])

print(b)
