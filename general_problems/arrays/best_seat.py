def bestSeat(seats):

    # Find longest continguous array of 0s

    idx = 0
    largest_contiguous = []

    for i in range(len(seats)):
        if seats[i] == 0:
            idx += 1
            largest_contiguous.append(idx)
        else:
            idx = 0
            largest_contiguous.append(idx)

    if max(largest_contiguous) == 1:
        return seats.index(0) + 1


    # Go from highest contiguous and choose the first largest block

    block = max(largest_contiguous)

    idx = seats.index(block) - (block // 2)
    return idx





    return -1
