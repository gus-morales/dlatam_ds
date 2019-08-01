def letra_i(n):

    ct = 1
    while ct <= n:
        
        if ct == 1 or ct == n:
            for i in range(n):
                print("*", end="")
            print()
        else:
            for i in range(n):
                if i != int(n/2):
                    print(" ", end="")
                else:
                    print("*", end="")
            print()

        ct += 1

    return None
