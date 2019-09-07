def letra_i(n):

    result_str = ""

    for row in range(0, n):
        for col in range(0, n):
            cond1 = (row == 0 or row == n-1)
            cond2 = (col == n//2)
            if cond1 or cond2:
                result_str += "*"
            else:
                result_str += " "
        result_str += "\n"

    return result_str

print(letra_i(5))