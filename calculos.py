def porcentage_of_commission (Sales):
  if Sales >= 50000:
   return  0.10
  elif Sales >= 25000:
   return 0.07
  elif Sales >= 10000:
   return 0.05
  else:
    return 0.03
  
  

def Total_of_the_Commission (Sales):
  return Sales * porcentage_of_commission(Sales)

def calculate_bonus (sales):
  if sales >= 70000:
    bonus = 1500
  else:
    return 0

def sellers_total_of_the_commission(Total_of_the_Commission, calculate_bonus):
  return Total_of_the_Commission + calculate_bonus  
