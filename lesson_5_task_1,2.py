#def odd_num_list(n):
#    for num_on in range(1, n+1, 2):
#        yield num_on


#odd_to_15 = odd_num_list(15)
n = 15
odd_to_15 = (num_on for num_on in range(1, n+1, 2))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))

