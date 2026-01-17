l = int(input())
for i in range(l):
    st_ = input()
    if len(st_) > 10:
        ss = str(len(st_)-2)
        print(st_[0] + ss + st_[-1])
    else:
        print(st_)
