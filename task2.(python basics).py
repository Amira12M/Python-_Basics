#create a boolean variable named x 
   x= true
   x= false
 
#create an integer variable named y
   y= 33

#create a float variable named z
   z=99.5

#create a string variable named s
   s="amira"

#convert the int variable to float
 m=float(x)
  
#can we convert the str to int? (ya&no)

// ya : if string as "txt" is a num 

$AS EX: 
        x="70" ------ n=int(x)

// no : if str is" txt " words meaning
 $AS EX:
        m= "i luv python"....... #   n=int(m)
that is wrong syntax and will create an error 

 
#create a list of numbers from 1 to 5
  my_list = [1,2,3,4,5]
  print ( my_list)

#create a tuple of numbers from 10 to 15
  my_tuple = (10,11,12,13,14,15)
  print (my_tuple)

#convert the list to tuple
 fruits = tuple(fruits)

#create a dict of 3 values
  my_dic={ 'name': "Amira M" , 'age':21, 'country':"Egypt" }  

# can we use semi colon; with python ?
---- ya , if there more than one statement in a line.

#python is interpreted or compiled ? 
--- interpreted language.

#what is the differences between low level & high level ?
'''
      - low level is a machine lang that is tough to understand the code written by.
      - high level is a programer friendly language , easy to understand.
'''
#What is the differences between = , ==
'''
 = is an assignment operator , but == is a comparsion operator if it equal or not .
'''

#What do we mean by using !=
''' that is meaning as a var is not equal the value .

#What is the operator precedence?
'''
the order of operations when coding 
++|--  ()  **  *|/  +|-

'''
# Create a variable x with value of 10
x = 10

# Increase x value by 15 using assignment operators
  x = x + 15 
  x += 15       

# Divide the x value by 5 using assignment operators
x = x / 5   
x /= 5

# Multiply the x value by 10 using assignment operator
 x = x * 10  
 x *= 10

# Get module of x on 3 using assignment operators
 x = x % 3  
 x %= 3

# Using python print the module of 11 to 4
 print( 11 % 4 )

# Print the exponent of 2,3
print( 2 ** 3)

# Divide 11 by 3 using python division
 11 / 3

## Can we divide 11 by 3 and get an integer number
"""" yes , we can
 $AS EX:  11 // 3 
# or 
x = 11 / 3
x = int (x)

# Check if 10 is bigger than 15 or not
  
# If 10 is not bigger than15 print x is smaller than 15
x = 10   
 if 10 > 15:
    print (10 is bigger than 15 )
 else:
    print("x is smaller than 15") 


## In which cases we will use all?
If we need all the conditions to be true 

# What is the differences between all , and
all ==> (When there are more than two conditions, they must be true.)
  and ==> ( When there are two conditions, they must be true.)


# What is the differences between any , or
 any ==> (When there are more than two conditions, at least one of them must be true.)
      or ==> (When there are two conditions, at least one of them must be true.)'''

# If we need all the conditions to be true we will use ….
''' all '''

#What is the differences between if , elif
 if ==>  ( It can be used once in a conditional sentence.and it finds one condition that is True, it stops and doesn't evaluate the rest  )
elif ==>( It can be used more than once in a conditional sentence.when the conditions not pass and true.mutually exclusive conditions . )


# What is the differences between elif else
''' elif ==> (It can be used more than once in a conditional sentence.when the conditions not pass and true.mutually exclusive conditions . )
    else ==> (It can be used once in a conditional sentence. is used in the last case of all in the if statement.)
'''

# Can we use more than one elif
''' ya, of course.'''

# Can we use more than one else
''' no , that will cause a problem .'''

#write s simple ternary operator
  name = "Amira" 
  print ("Hola Seniorta") if name == "Amira"  else print ("who you are")

#in elif , python will check all the conditions no matter what ?

'''no''' 

#in elif we use else for ... ?

'''for the last condition when all conditions are false'''

#if we have this list [2,4,6,8,10] :

A = [2,4,6,8,10]

# check to see if 4 in this list or not
if 4 in A :
    print(True)
else:
    print(False)

# check to see if 4 and 6 in this list on not
if 4 and 6 in A :
    print(True)
else:
    print(False)

# check to see if 3 or 6 in this list
if 3 or 6 in A:
    print(True)
else:
    print(False)
    
# check to see if 2 , 4 and 5 in this list
if 2 and 4 and 5 in A :
    print(True)
else:
    print(False)

                                                                                                                    **********
                                                                               %%%%%%%%% finito task 2 %%%%%%%%%
