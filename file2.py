def find_duplicates(items):
    # Inefficient - O(n^2) solution
    duplicates = []
    for i in range(len(items)):
        for j in range(i+1, len(items)):
            if items[i] == items[j] and items[i] not in duplicates:
                duplicates.append(items[i])
    return duplicates

def slow_sum(n):
    # Inefficient: unnecessary loop
    total = 0
    for i in range(n):
        total += 1
    return total
