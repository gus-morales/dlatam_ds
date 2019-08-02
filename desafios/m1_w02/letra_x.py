def letra_x(n):

    result_str = ""
    i=0
    j=n-1
    for row in range(n):
        for col in range(n):
            if row==i and col==j:
                result_str += "*"
                i += 1
                j -= 1
            elif row == col:
                result_str += "*"
            else:
                result_str += " "
        result_str += "\n"

    return result_str

print(letra_x(5))