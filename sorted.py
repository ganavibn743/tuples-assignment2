def sort_tuples_by_last_elem(tuples):
    return sorted(tuples,key=lambda x: x[-1])

tuples = [(1,4),(2,1),(5,8),(4,2)]
sorted_tuples = sort_tuples_by_last_elem(tuples)
print(sorted_tuples)
