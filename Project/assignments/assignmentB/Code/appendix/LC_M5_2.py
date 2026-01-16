def is_palindrome(strry):
    js = []
    for j0 in strry:
        js.append(j0)
    if js == js[::-1]:
        return True
    else:
        return False


print(is_palindrome('abc'))
print(is_palindrome('aba'))
