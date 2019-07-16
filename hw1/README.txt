PART I:

Hello World-
print("Hello!")

Converter-
def main():
    celsius = eval(input("What is the temperature in celsius?"))
    for i in range(5):
        fahrenheit = 9/5*celsius+32
        print("The temperature is", fahrenheit, "degrees fahrenheit.")
    
main()

Unit Conversion-
def main():
    centimeters = eval(input("How many centimeters?"))
    inches = centimeters/2.54
    print("you have", inches, "inches.")
    
main()

Slope-
def main():
    howmany = eval(input("How many numbers do you want summed?"))
    ssum = 0
    
    for i in range(howmany):
        a = eval(input("Type a number to be summed."))
        ssum = a + ssum
        
    print("The sum of all of your numbers is", ssum)
    
main()

Fibonacci Sequence-
def fibonacci(n):
    n = eval(input("enter a whole integer"))
    if n<0:
        print ("integer cannot be less than zero")
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)






PART II:
My change program is as follows-

def small_change(n, c_for_use, c_atm):
    print("You're at a register, and the cashier has just handed you your change.")
    n = eval(input("How much change are you owed?"))
    coins = [.01, .05, .10, .25]
    
    if sum(c_atm) == n:
        yield c_atm
    elif sum(c_atm) > n:
        pass
    elif c_for_use == []:
        pass
    else:
        for c in small_change(n, c_for_use[:], c_atm+[c_for_use[0]]):
            yield c
        for c in small_change(n, c_for_use[1:], c_atm):
            yield c
            
    c_returned = [s for s in small_change(n, coins, [])]
    
    min(c_returned, key=len)
    print(len)
        

small_change()


- For this program, I thought to approach it by defining my variables in the "header" of this code.
- I defined "n" within the program as well, because it was important for the user input.
- When outlining my array, I made sure to sort my "coins" from least to greatest.
- I programmed it so that the interpreter would calculate all the coins that would be returned.  However, in order to make it so that the interpreter didn't print all of those values, I defined a variable that allowed me to later print only the minimum number of coins to give back, as opposed to every possible combination of coins to return.