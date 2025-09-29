def main():
    total = 0
    number = 0
    while number >= 0:
        number = getinput()
        if number >= 0:
            total = addsum(total, number)
       
        
        output(total)


def getinput():
     num = int(input("enter a number that is not negative, -1 to quit"))
     return num

def addsum(total, num):
    
    total = total + num
    return total


def output(total):
    print("total is", total)

main()
