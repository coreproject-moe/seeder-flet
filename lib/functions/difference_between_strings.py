def find_difference(original, edited):
    difference = set(original.split()).symmetric_difference(set(edited.split()))
    return difference
