while(1):
    pa = input()
    if pa == '#':
        break
    par = pa[:-1]
    sum_ = 0
    for i in pa:
        if i == '1':
            sum_ = sum_ + 1
    isOdd = sum_ % 2

    if pa[-1] == 'e':
        if isOdd == 1:
            par = par + '1'
        else:
            par = par + '0'
    else:
        if isOdd == 1:
            par = par + '0'
        else:
            par = par + '1'

    print(par)