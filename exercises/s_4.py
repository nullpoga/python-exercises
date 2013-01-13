
tmp = 0
print 'a >= b'
a = int(raw_input('a'))
b = int(raw_input('b'))

ta = a
tb = b

while 1:
    if b == 0 :
        print 'gdb = %d' %a
        break

    tmp = b
    b = a % b
    a = tmp

lcm = ta * tb / a
print 'lcm = %d' %lcm
