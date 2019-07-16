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