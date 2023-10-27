# Sample datasets
dataset1 = [{'ID': 1, 'Name': 'Alice', 'Salary': 50000},
            {'ID': 2, 'Name': 'Bob', 'Salary': 60000},
            {'ID': 3, 'Name': 'Charlie', 'Salary': 75000}]

dataset2 = [{'ID': 2, 'City': 'New York', 'Salary': 70000},
            {'ID': 3, 'City': 'Los Angeles', 'Salary': 80000},
            {'ID': 4, 'City': 'Chicago', 'Salary': 65000}]

# Function to find the union of two datasets
def union(dataset1, dataset2):
    union_result = dataset1.copy()
    for record in dataset2:
        if record not in union_result:
            union_result.append(record)
    return union_result

# Function to find the intersection of two datasets
def intersection(dataset1, dataset2):
    intersection_result = [record for record in dataset1 if record in dataset2]
    return intersection_result

# Function to find the difference of two datasets
def difference(dataset1, dataset2):
    difference_result = [record for record in dataset1 if record not in dataset2]
    return difference_result

# Function to perform a natural join on two datasets based on a common attribute
def natural_join(dataset1, dataset2, common_attribute):
    join_result = []
    for record1 in dataset1:
        for record2 in dataset2:
            if record1.get(common_attribute) == record2.get(common_attribute):
                join_record = {**record1, **record2}
                join_result.append(join_record)
    return join_result

# Perform union, intersection, difference, and natural join based on 'ID'
common_attribute = 'ID'
union_result = union(dataset1, dataset2)
intersection_result = intersection(dataset1, dataset2)
difference_result = difference(dataset1, dataset2)
natural_join_result = natural_join(dataset1, dataset2, common_attribute)

# Print the results
print("Dataset 1:")
for record in dataset1:
    print(record)

print("Dataset 2:")
for record in dataset2:
    print(record)

print("Union Result:")
for record in union_result:
    print(record)

print("Intersection Result:")
for record in intersection_result:
    print(record)

print("Difference Result:")
for record in difference_result:
    print(record)

print("Natural Join Result (based on 'ID'):")
for record in natural_join_result:
    print(record)
