def main():
    howmany = eval(input("How many numbers do you want summed?"))
    ssum = 0
    
    for i in range(howmany):
        a = eval(input("Type a number to be summed."))
        ssum = a + ssum
        
    print("The sum of all of your numbers is", ssum)
    
main()