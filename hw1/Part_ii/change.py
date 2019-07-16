def small_change(n, c_for_use, c_atm, pos):
    if pos < 0:
        return c_atm
    elif n < c_for_use[pos]:
        return small_change(n, c_for_use, c_atm, pos - 1)
    else:
        return small_change(n-c_for_use[pos], c_for_use, c_atm+1, pos)
    
def small_change2(n, c_for_use, c_atm, pos):
    if pos < 0:
        return c_atm
    else:
        fit = n//c_for_use[pos]
        remainder = n%c_for_use[pos]
        return small_change(remainder, c_for_use, c_atm+fit, pos-1)
        
if __name__ == '__main__':
    print("You're at a register, and the cashier has just handed you your change.")
    n = eval(input("How much change are you owed?"))
    coins = [.01, .05, .10, .25]
    coins1 = small_change(n, sorted(coins), 0, len(coins)-1)
    coins2 = small_change2(n, sorted(coins), 0, len(coins)-1)
    print("First function returned", coins1)
    print("Second function returned", coins2)