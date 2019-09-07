def gen(nr):
    chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
             "k", "l", "m", "n", "o", "p", "q", "r", "s",
             "t", "u", "v", "w", "x", "y", "z"]

    result = chars[0:nr]
    
    string = ""
    for r in result:
        string += r
    
    return(string)
