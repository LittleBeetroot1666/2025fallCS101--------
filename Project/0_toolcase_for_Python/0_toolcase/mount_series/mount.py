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
