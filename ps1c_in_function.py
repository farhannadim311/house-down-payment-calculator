def part_c(initial_deposit):
    ##############################################
    ## Your original code starts here unchanged ##
    ##############################################

    cost_of_house = 800000
    down_payment = 0.25
    required_payment = cost_of_house * down_payment
    epsilon = 100
    time = 36
    low = 0
    high = 1
    r = (low + high) / 2
    steps = 1
    found = True

    while(True):
        amount_saved = initial_deposit
        for m in range(time):
            amount_saved = (amount_saved * (1 + r / 12))
        
        if(abs(amount_saved - required_payment) <= epsilon):
            break
        if(low >= high):
            found = False
            steps = 0
            r = None
            break
            
        elif(amount_saved > required_payment):
            high = r
        else:
            low = r

        r = (low + high) / 2
        steps += 1

    if(found):
        print(f"Best savings rate: {r}")
        print(f"Steps in bisection search: {steps}")
    else:
        print(f"Best stavings rate: None")
        print(f"Steps in bisection search: 0")

    return r, steps
