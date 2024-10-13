def has_merge_conflict(pull_requests)-> bool:

    temp = []
    for lista in pull_requests:
        for i in range(min(lista),max(lista)+1):
            if i in temp:
                return True
        else:
            temp.append(i)
    return False

has_merge_conflict([[5, 10], [15, 40], [25, 50]])
