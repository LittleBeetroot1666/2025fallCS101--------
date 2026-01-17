while True:
    try:
        t = float(input())
        x = 1
        y = 1 - t
        k = 0
        while abs(y/(2 * x)) > 1e-6:
            x -= y / (2 * x)
            y = x ** 2 - t
            k += 1
        x -= y / (2 * x)
        k += 1
        print(k, "%.2f" % x)
    except:
        break
