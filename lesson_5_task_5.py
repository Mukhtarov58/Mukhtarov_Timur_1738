from time import perf_counter
start = perf_counter()
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [el for el in src if src.count(el) == 1]
print(result, perf_counter() - start, type(result))


