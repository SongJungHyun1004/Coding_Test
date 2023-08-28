def solution(cacheSize, cities):
    answer = 0
    cache = []
    if cacheSize == 0:
        return len(cities)*5
    for city in cities:
        city = city.lower()
        if not city in cache:
            if len(cache) >= cacheSize:
                cache.pop()
            answer += 5
        else:
            index = cache.index(city)
            cache.pop(index)
            answer += 1
        cache.insert(0, city)
    return answer