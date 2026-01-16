def longestPalindrome(s):
    def is_palindrome(strry):
        js = []
        for j0 in strry:
            js.append(j0)
        ts = js.copy
        js.reverse()
        if js == ts:
            return True
        else:
            return False

    n = len(s)
    res = []
    for i in range(n):
        for j in range(i, n):
            if is_palindrome(s[i: j]):
                res.append([j - i, s[i: j]])
    res.sort(reverse=True)
    return res[0][1]


print(longestPalindrome(input()))
