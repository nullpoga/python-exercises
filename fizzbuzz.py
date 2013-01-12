import sys

def main(list):
    
    list = []

    for i in range(1,100):
        if i % 13 == 0:
            list.append(i)

    list.reverse()
    print list

if __name__ == "__main__":    
    main(*sys.argv)






