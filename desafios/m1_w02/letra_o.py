def letra_o(n):

    ct = 1
    while ct <= n:
        
        if ct == 1 or ct == n:
            for i in range(n):
                print("*", end="")
            print()
        else:
            for i in range(n):
                if i == 0 or i == n-1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()

        ct += 1

    return None

letra_o(5)