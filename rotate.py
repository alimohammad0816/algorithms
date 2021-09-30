def rotate(s, k):
    duble_s = s + s
    if k <= len(s):
        return duble_s[k:k+len(s)]
    else:
        return duble_s[k-len(s):k]


print(rotate("ali", 5))