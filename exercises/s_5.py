
for i in range(1,10000):

    yakusuu = 0
    j = 1

    while j <= i :
        if i % j == 0 :
            yakusuu += 1
        j += 1

    if yakusuu == 2 :
        print '%d' %i
