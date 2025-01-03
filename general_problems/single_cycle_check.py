def single_cycle_check(array):
    """
    Array of integers where each integer is a jump in the array. If the jump spills
    out of the bounds of the array then it wraps around. Check if the jumps in the array
    form a single cycle. Start at any index in the array and if it jumps through every element before
    going back to the first one that is a single cycle jump
    """


    length = len(array)

    # Start off with the first index for ease

    num_visited = 1
    has_returned = False
    idx = 0

    while num_visited < length:

        if num_visited > 0 and idx == 0:
            return False


        # Start the iteration
        idx += array[idx]

        # Wrap around to the front
        if idx > length - 1:
            idx = idx - length - 1
        elif idx < 0:
            idx = length - 1 + idx

        if idx == 0:
            has_returned = True

        num_visited += 1

    if num_visited == length:
        return True
    return False


