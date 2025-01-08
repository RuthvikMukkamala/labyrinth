def maxSumIncreasingSubsequence(array):
    # Given an array on non-empty integers return the greatest sum that can be 
    # generated from a strictly increasing subsequence in the array


    # Idea - keep getting the max of the previous subsequences 

    if len(array) == 0:
        return 0
    if len(array) == 1:
        return array[0]

    max_array = [0 for _ in array]

    for i in range(len(max_array)):
        