#Day_2
#Data Types
## String Slicing
print("Hello"[4])

## Large integers can be replaced with _ to be easy readable
print(123_456_789)

## Boolean ==> True , False

## Float
float_num = 3.14
print(float_num)

## type() function gives the type of the data given
print(type(input("What is your name?")))

total_bill = input("What was the total bill? ") ## ==> Always return a string datatype
print(type(total_bill))

## Len(int_number) gives an error
## Strings cannot be concatinated with "integers"
## To fix this error use str() that's used to cast the intger ==> string 
name_len = len(input("What is your name?"))
print("Your name has " + str(name_len) + " characters.")

## Data type converting {casting} str() ,int() , float()
print(70 + float("100.5"))
print(str(70) + str(100))

## Mathimatical Opeartion ==> + , - , * , / , ** (exponent)
## Operations are excuted using the PEMDAS Rule ==> parentheses , exponent , Muls & Divs , Adds & Subs
## Result of division in python is float
print(type(16/4))

## Rounding methods round(A/B, C) C is the decimal places
## Floor rounding use //
## Rounding could be done also using "{:.nf}".format n = 1,2,3,... indicating the rounding precision
## but note that the returned value from format() is string not float!!!
print(round(8/3))
print(round(8/3,3))
rnd = 8/3
print("{:.10f}".format(rnd))

print(8//3) # ==> Floor

## /= ,*= , += , -= ==> Result = Result/2 or Result * 2 ....

## Instead of converting data_types to strings for concatination use "f-string" method
score = 90
print(f"your score is {score}")
print(int(2.7))

# print(float("$124.56")) ==> This cannot be converted because it includes $ sign which cannot be interpreted