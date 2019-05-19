# Addition

# Adding items to the end of a list
count = [1, 2, 3]
count.append(4)
print(count) # [1, 2, 3, 4]

# Merging two arrays
extended_count = [5, 6, 7]
count.extend(extended_count)
print(count) # [1, 2, 3, 4, 5, 6, 7]

# Literally adding two arrays
more_counting = [8, 9, 10]
more_counts = count + more_counting
print(more_counts) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]