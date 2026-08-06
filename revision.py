def roman_int(s):
    val = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }
    total = 0
    for i, char in enumerate(s):
        current_val = val[char]
        if i < len(s) - 1:
            next_val = val[s[i+1]]
            if current_val < next_val:
                total = total - current_val
            else:
                total = total + current_val
        else:
                total = total + current_val
    return total
