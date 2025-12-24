def sorting(items):
    for i in range(len(items)):
        for j in range(i+1, len(items)):
            if items[i] > items[j]:
                items[i], items[j] = items[j], items[i]
    return items