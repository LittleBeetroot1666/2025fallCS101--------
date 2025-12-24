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


def poup(sest_002):
    while not up(sest_002):
        for _ in range(len(sest_002) - 1):
            if sest_002[_] > sest_002[_ + 1]:
                sest_002[_], sest_002[_ + 1] = sest_002[_ + 1], sest_002[_]
    return sest_002


