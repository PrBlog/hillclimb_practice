import operator

my_dict = {(5,2): 1, (1,3): 5, (2,1): 3}
print(max(my_dict.items(), key=operator.itemgetter(1))[0])