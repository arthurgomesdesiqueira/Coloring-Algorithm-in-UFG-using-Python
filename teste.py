import bisect

l = ['1', '11', '2']


valor = bisect.bisect_left(l, '2', 0, len(l))

print(valor)