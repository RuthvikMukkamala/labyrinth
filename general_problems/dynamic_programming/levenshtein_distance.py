def levenshtein_distance_helper(str1, str2, len_1, len_2, memo):
    if len_1 == 0:
        return len_2
    if len_2 == 0:
        return len_1

    if (len_1, len_2) in memo:
        return memo[(len_1, len_2)]

    if str1[len_1 - 1] == str2[len_2 - 1]:
        memo[(len_1, len_2)] = levenshtein_distance_helper(str1, str2, len_1 - 1, len_2 - 1, memo)
    else:
        memo[(len_1, len_2)] = 1 + min(
            levenshtein_distance_helper(str1, str2, len_1 - 1, len_2, memo),       
            levenshtein_distance_helper(str1, str2, len_1, len_2 - 1, memo),       
            levenshtein_distance_helper(str1, str2, len_1 - 1, len_2 - 1, memo)    
        )
    
    return memo[(len_1, len_2)]

def levenshteinDistance(str1, str2):
    memo = {}
    return levenshtein_distance_helper(str1, str2, len(str1), len(str2), memo)
