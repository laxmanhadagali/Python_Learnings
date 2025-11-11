print("::-WELCOME TO UPCOMING CODERS EVENT MANAGEMENT::-\n")

venue=int(input("enter the budget of venue "))
decorations=int(input("enter the budget of decoration "))
catering=int(input("enter the cost of food for each plate "))
guests=int(input("enter the Total number of guests "))

total_budget=venue+decorations+(catering*guests)
print(total_budget)

gifts=input("Given gifts(Y/N) ")
if gifts=='y'  or gifts=='Y':
   giftC=int(input("enter the cost of gifts or favors "))
   numberofPeople=(int(input("enter the number gifts or favor given to guests ")))
   total_budget=total_budget+(giftC*numberofPeople)
#else:
    #print(total_budget)
   

print("Total budget of Event Including All the Costs and Gifts is \n", total_budget)
print("\n")
print("Thank You")


