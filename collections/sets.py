# sets are a collection of unique items
# sets are iterable collections with no indexes
# sets are wrapped in curly braces

new_set = {1, 2, 3}
print(new_set)

# the order of items in a set do not matter
# python sorts a set in a way that makes sense to python

# adding an item
new_set.add(4)
print(new_set)

# sets can be combined with the update method
newer_set = {5, 6, 7, 8}
even_newer_set = {9, 10, 11, 12}
new_set.update(newer_set, even_newer_set)
print(new_set)

# remove items
# this method removes an item from the set,
# but can throw an error if it doesn't exist
new_set.remove(12)
print(new_set)

# discard is a better alternative, as it will not do anything
# if the item does not exist
new_set.discard(1000)
print(new_set)

# we can also pop items from a set
print(new_set.pop())
print(new_set)

# mathematical set operations
first_set = set(range(10))
second_set = {1, 3, 5, 7, 9, 11, 13, 15}

# union (all items from the sets)
merged = first_set.union(second_set)
merged_detail = 'The merged set is {}'.format(merged)
print(merged_detail)

# intersection (all common items between sets)
intersection = first_set.intersection(second_set)
intersection_detail = 'The intersection is {}'.format(intersection)
print(intersection_detail)

# the intersection operator is an ampersand

# difference (all unique items between sets)
difference = first_set.difference(second_set)
difference_detail = 'The difference between sets is{}'.format(difference)
print(difference_detail)

# the difference operator is a hyphen (-)

# symmetric difference (all the items not in the set used as an argument)
symm_diff = first_set.symmetric_difference(second_set)
symm_detail = 'The symmetric difference between sets is {}'.format(symm_diff)
print(symm_detail)

# the symmetric difference operator is a caret (^)

COURSES = {
    "Python Basics": {"Python", "functions", "variables",
                      "booleans", "integers", "floats",
                      "arrays", "strings", "exceptions",
                      "conditions", "input", "loops"},
    "Java Basics": {"Java", "strings", "variables",
                    "input", "exceptions", "integers",
                    "booleans", "loops"},
    "PHP Basics": {"PHP", "variables", "conditions",
                   "integers", "floats", "strings",
                   "booleans", "HTML"},
    "Ruby Basics": {"Ruby", "strings", "floats",
                    "integers", "conditions",
                    "functions", "input"}
}

query = { 'input', 'conditions' }

def covers(query):
    category_list = []
    for category in COURSES:
        current_course_list = COURSES[category]
        _overlapping_courses = current_course_list.intersection(query)
        overlapping_courses = list(_overlapping_courses)
        has_overlap = len(overlapping_courses) > 0
        if has_overlap:
            category_list.append(category)
    return category_list

print(covers(query))

def covers_all(query):
    query_length = len(list(query))
    category_list = []
    for category in COURSES:
        current_course_list = COURSES[category]
        _overlapping_courses = current_course_list.intersection(query)
        overlapping_courses = list(_overlapping_courses)
        has_match = len(overlapping_courses) == query_length
        if has_match:
            category_list.append(category)
    return category_list

print(covers_all(query))