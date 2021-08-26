def solution(cacheSize, cities):
    cache = []
    time = 0
    if cacheSize == 0:
        time = 5 * len(cities)
    else:
        for city in cities:
            time = LRU(cache, city, time, cacheSize)
        print(time)
    return time


def LRU(cache, data, time, cacheSize):
    # Miss!
    data=data.upper()
    if data not in cache:
        if len(cache) < cacheSize:
            cache.append(data)
        else:
            cache.pop(0)
            cache.append(data)
        time += 5

    # Hit!
    else:
        cache.pop(cache.index(data))
        cache.append(data)
        time += 1

    return time
solution(3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"])