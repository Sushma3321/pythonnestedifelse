expected_month=int(input("enter expected month"))
return_month=int(input("enter return month"))
if expected_month<=12 and return_month<=12:
       print("sucess")
       if expected_month>return_month:
              print(500*(expected_month-return_month))
              expected_year=int(input("enter expected year"))
              return_year=int(input('enter return year'))
       else:
              print("fine is less")
       if expected_year>return_year:
              print("10000 fixed fine")
              expected_date=int(input("enter expected date"))
              return_date=int(input("enter return date"))
       if expected_date>return_date:
              print(15*(expected_date-return_date))
       if expected_date<return_date:
              print("no fine")
else:
    print("enter valid month")
       


    
