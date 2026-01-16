def to_listie(n_to_listie):
    return [i_to_listie for i_to_listie in range(n_to_listie)]


def str_to_listie(n_to_listie):
    return [str(i_to_listie) for i_to_listie in range(n_to_listie)]


def to_str(listy):
    return [str(i_in_listy) for i_in_listy in listy]


def cata_findm(n0, m0):
    if m0 == 1:
        return 0
    else:
        return min(n0 + 1, m0)


def alter_listie(listy):
    first = listy.pop(0)
    listy.append(first)
    return listy


def kpj(strry_listy):
    return ' '.join(strry_listy)


def mounti(listie):
    mount_altitude = [0]
    for i in range(1, len(listie)):
        if listie[i] > listie[i - 1]:
            mount_altitude.append(mount_altitude[-1] + 1)
        elif listie[i] < listie[i - 1]:
            mount_altitude.append(mount_altitude[-1] - 1)
        else:
            mount_altitude.append(mount_altitude[-1])
    base_altitude = min(mount_altitude) - 1
    mount_waterfill = -len(listie) * base_altitude
    mount_seasum = sum(mount_altitude)
    mount_landsum = mount_seasum + mount_waterfill
    return mount_landsum


def hillgravedown(listy):
    hillgravedown_n = len(listy)
    hilldown_left = [0] * hillgravedown_n
    for i in range(hillgravedown_n):
        if i > 0 and listy[i] > listy[i - 1]:
            hilldown_left[i] = hilldown_left[i - 1] + 1
        else:
            hilldown_left[i] = 1

    hilldown_right = hillgravedown_dust = 0
    for i in range(hillgravedown_n - 1, -1, -1):
        if i < hillgravedown_n - 1 and listy[i] > listy[i + 1]:
            hilldown_right += 1
        else:
            hilldown_right = 1
        hillgravedown_dust += max(hilldown_left[i], hilldown_right)

    return hillgravedown_dust
