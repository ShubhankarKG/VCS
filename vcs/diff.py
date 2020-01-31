def lcs(str1, str2):
    m = len(str1)
    n = len(str2)
    dp_list = [[0 for i in range(n + 1)] for i in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp_list[i][j] = 0
            elif str1[i-1] == str2[j-1]:
                dp_list[i][j] = dp_list[i - 1][j - 1] + 1
            else:
                dp_list[i][j] = max(dp_list[i-1][j], dp_list[i][j-1])
    return dp_list[m][n]


def get_diff(str1, str2):
    leng = lcs(str1, str2)
    print("--- ", len(str1) - leng, sep='')
    print("+++ ", len(str2) - leng, sep='')


def diff(original_file, modified_file):
    original_file = open(original_file, "r+")
    modified_file = open(modified_file, "r+")
    lines_in_original_file = original_file.readlines()
    lines_in_modified_file = modified_file.readlines()
    # diff = len(lines_in_modified_file) - len(lines_in_original_file)
    line_tuple = zip(lines_in_original_file, lines_in_modified_file)
    for tuple_element in line_tuple:
        get_diff(tuple_element[0], tuple_element[1])
