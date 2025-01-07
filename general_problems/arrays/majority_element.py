def majorityElement(array):
    if not array:
        return -1  

    candidate = None
    count = 0
    for num in array:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    if array.count(candidate) > len(array) // 2:
        return candidate
    else:
        return -1  
