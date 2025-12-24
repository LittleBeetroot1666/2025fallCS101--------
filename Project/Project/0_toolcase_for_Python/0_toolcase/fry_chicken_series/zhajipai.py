def zhajipai(js, k):
    js.sort(reverse=True)
    res = sum(js) / k
    if js[0] <= res:
        return res
    else:
        new_js = js[1:]
        nk = k-1
        return zhajipai(new_js, nk)
