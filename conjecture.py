
def even(no):
    if no % 2 == 0:
        return True
    else:
        return False

def findSteps(no):
    steps = 0
    while no != 1:
        if even(no):
            no/=2
            steps+=1
        else:
            no*=3
            no+=1
            steps+=1

    print "No of steps : %s" %steps

def userInput():
    while True:
        x = raw_input("Enter number greater than 1 : ")

        try:
            number = int(x)
            if number > 1:
                return number
        except ValueError:
            print "Enter a number"

def main():
    no = userInput()
    findSteps(no)

if __name__ == "__main__":
    main()