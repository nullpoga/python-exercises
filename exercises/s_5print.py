import time

f = open("primenumber.txt", 'w')
starttime = time.clock()

for i in range(1,10000):

    yakusuu = 0
    j = 1

    while j <= i :
        if i % j == 0 :
            yakusuu += 1
        j += 1

    if yakusuu == 2 :
        f.write("%d\n" %i)
        print '%d' %i

f.close()

time1 = time.clock()
print time1 - starttime


