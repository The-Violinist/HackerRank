import collections
arr = [1, 1, 2, 2, 3]

occurrences = collections.Counter(arr)

def id_occurence():
    highest = 0
    item_id = 1000000
    for item in occurrences:
        if occurrences[item] >= highest:
            if item < item_id:
                item_id = item
                highest = occurrences[item]
    return highest
