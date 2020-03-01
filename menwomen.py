men=int(input("How many men are in the class? "))
women=int(input("How many women are in the class? "))

sum_of_students=men+women
men_in_class=(men/sum_of_students)*100
women_in_class=(women/sum_of_students)*100

print("The total percentage of men in the class is "+ format(men_in_class, ".2f")+"%,"\
      " the total percentage of women in the class is "+ format(women_in_class, ".2f")+"%.")
