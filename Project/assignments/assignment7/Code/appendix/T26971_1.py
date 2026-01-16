# Greed and Miserliness
def mount(listie):
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


starie = 1
n = int(input())
js = list(map(int, input().split()))
sgm = 0
j = 1
b_cat = 0

while j < len(js):
    if js[j] == js[j - 1]:
        starie = 1
        sgm += starie
        j += 1
        b_cat = 1

    else:
        mnt = [js[j - 1]]
        while j < len(js) and js[j] != js[j - 1]:
            mnt.append(js[j])
            j += 1
        starie = mount(mnt)
        sgm += starie
        if b_cat == 1:
            sgm -= 1
        b_cat = 0

print(sgm)
