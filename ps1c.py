## 6.100A PSet 1: Part C
## Name:
## Time Spent:
## Collaborators:

##############################################
## Get user input for initial_deposit below ##
##############################################
initial_deposit = float(input("Enter the inital depost: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
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


##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################
while(True):
    amount_saved = initial_deposit
    for m in range(time):
        amount_saved = (amount_saved * (1 + r / 12))
    
    if(abs(amount_saved - required_payment) <= epsilon):
        break
    if(low >= high):
        found = False
        r = None
        steps = 0
        break
    elif(amount_saved > required_payment):
        high = r
    else:
        low = r
    r = (low + high) / 2
    steps +=1
if(found):
    print(f"Best savings rate: {r}")
    print(f"Steps in bisection search: {steps}")
else:
    print(f"Best stavings rate: {r}")
    print(f"Steps in bisection search: {steps}")


