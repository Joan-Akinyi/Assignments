#Basic Calculator Program

while True:
  print("choose an operation")
  print("1 - add")
  print("2 - Subtract")
  print("3 - Multiply")
  print("4 - Divide")
  print("5 - Exit")

  try:
    option = int(input("choose an operation: "))
  except ValueError:
    print("Please enter a valid number.")
    continue


  if option == 5:
    print("Exiting the calculator. Goodbye!")
    break



  if (option in [1,2,3,4]):
    try:
      num1 = int(input("enter first number: "))
      num2 = int(input("enter second number: "))
    except ValueError:
       print("Please enter valid numbers")
       continue

    if(option == 1):
      result = num1 + num2
      symbol = "+"
    elif(option == 2):
      result = num1 - num2
      symbol = "-"
    elif(option == 3):
      result = num1 * num2
      symbol = "*"
    elif(option == 4):
      symbol = "/"
      if num2 !=0:
       result = num1 // num2
      else:
        result = "Error: division by zero is not allowed"

    if isinstance(result, int):
      print(f"{num1} {symbol} {num2} = {result}")
    else:
      print(result)
    
    print("The result of the operation is {}".format(result))
  else:
    print("Invalid option.Please choose between 1 and 5.")
