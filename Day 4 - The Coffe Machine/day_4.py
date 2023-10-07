total = 0
global water, milk, coffe
water = 300
milk = 200
coffe = 100
flavor = "none"

def report(x):
  print("Water = {} ml".format(water))
  print("Milk = {} ml". format(milk))
  print("Coffe = {} g".format(coffe))
  print("Money = ${:.2f}".format(x))

def money():
  penny = int(input("Input Penny : "))
  nickel = int(input("Input Nickle : "))
  dime = int(input("Input Dime : "))
  quarter = int(input("Input Quarter : "))
  global total
  total = (penny*0.01)+(nickel*0.05)+(dime*0.1)+(quarter*0.25)

while flavor != "exit":
  flavor = input("What would you like? (espresso/latte/cappuccino) : ")

  if flavor == "espresso":
    money()
    print("Your money is : ${}".format(total))
    if total > 1.50 and water > 50 and coffe > 18 :
      water = water - 50
      coffe = coffe - 18
      total = total - 1.50
      print("Your change is : ${}".format(total))
      print("Please enjoy your espresso \n")
    else :
      print("Your money is not enough/resource is not enough, money refunded.")
  elif flavor == "latte":
    money()
    print("Your money is : ${}".format(total))
    if total > 2.50 and water > 200 and coffe > 24 and milk > 150 :
      water = water - 200
      coffe = coffe - 24
      milk = milk - 150
      total = total - 2.50
      print("Your change is : ${:.2f}".format(total))
      print("Please enjoy your latte \n")
    else :
      print("Your money is not enough/resource is not enough, money refunded.")
  elif flavor == "cappuccino":
    money()
    print("Your money is : ${:.2f}".format(total))
    if total > 3 and water > 250 and coffe > 24 and milk > 100 :
      water = water - 250 
      coffe = coffe - 24
      milk = milk - 100
      total = total - 3
      print("Your change is : ${:.2f}".format(total))
      print("Please enjoy your cappuccino \n")
    else :
      print("Your money is not enough/resource is not enough, money refunded.")
  elif flavor == "report":
    report(total)
  elif flavor == "refil":
    water = 300
    milk = 200
    coffe = 100
  else:
    print("No input selected.")

