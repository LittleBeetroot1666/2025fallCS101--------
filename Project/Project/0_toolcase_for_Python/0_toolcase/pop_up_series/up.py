def up(sest_001):
    blacklist_001 = 0
    if len(sest_001) == 1:
        return True
    else:
        for _ in range(len(sest_001) - 1):
            if sest_001[_] > sest_001[_ + 1]:
                blacklist_001 += 1
        if blacklist_001 == 0:
            return True
        else:
            return False
