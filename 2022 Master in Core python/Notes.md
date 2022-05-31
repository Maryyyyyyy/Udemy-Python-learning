# **Master in Core Python Programming** 

## Day 1: Python as a language
> Python job market 
- Python different fields: AI, Data science, Data analytics, Machine learning, Web development, Imaging processing or face recognition, Video processing, game development. 
- Companies that used python: Google, Youtube, Intel, IBM, NASA, Pixar, Netflix, Facebook, Spotify, Reddit, Pinterest, Instagram, JP Morgan. 

## Day 2: Python downloading and installation
> Install python into the computer
- Difference between Python 2 and Python 3: Python 3 release in 2008, 6 years later. 
- Python 2: print "hello world"; Python 3: print("Hello World")
- Python 2: int a = 5/2 -> 2; Python 3: int a = 5/2 --> 2.5
- Python 2: raw_input(); Python 3: input()
- python 2: xrange: generate any number in the range; Python 3: use range
- Python 2: ASCI is used to store string; Python 3: UNIVODE is used to store string
- Python 2: Integer size up to 32 bit; Python 3: Unlimited
- How to check if Python is installed: Type "python" in cmd, will pop information related to python. 

## Day 3: Hello World Program
> IDE, Hellow world program
- IDE: Integrated Development Environment. 
- Hello world in cmd: print "hello world" (Python 2 installed)
- Hello world in plain text: open notepad, write print "hello world" in the file and save as hello_world.py, execute use python hello_world.py
- Hello world in Notepad ++: open notepad++, write print "hellow world" in the file and save as test.py, execute python test.py
- Hello world in VS code: create new file in vs code, name as hello_world.py. Write the same line inside and run the code inside vs code. 

## Day 4: Input and output in python
> Learning input and output function
- input(): get anything from user. Can put string inside the () to give direction to user. String will apear in the command. 
- Output: display anything to user, print(). 

## Day 5: Important concepts in python
> Python 2/3 difference, Comments, statement, Terminator, Indentation
- Python 2/3 difference: print difference; int difference; raw_input and input(); xrange and range; 
- In python 2, 5/2 ->2; In python 3, 5/2 ->2.5. 
- comments in python: Single line comment (#); Multiple line comment ("""aaa""""); 
- Program: a set of instruction that provided to computer;
- Statement: a complete action in the program; Separate the statement using semicolon ';' on single line
- Separator in python: semicolon. No need for separator in python, but in C++, need separator. 
- Indentation: need proper space to keep code in specific block. 

## Day 6: Variables in python
> What is a variable? 
- Variable can change during program execution; 
- Variable is the identifier, you need to declare and initiate. 
> Decalaration and initialization of variable in python
- Decalaration: write name of variable without providing a value. 
- Initialization: after declaration, we need to provide a value to declared variable. In python, no need for decalaration; In C++, need decalaration. 
> What is expression? 
- Expression: collection of operator and operand. 
- Operator: symbol that perform an operation, like +, - ...
- Operand: things which operation is performed 
> Undefined variable in python
- Variable that you did not declare or initialized. 
> Types of variables
- Global: Variable that is declared outside of any specific block of code; 
- local: Variable that is declared inside a specific block of code. 

## Day 7: Reserved words and escape sequence
> Escape sequence in python
- Special characters that used for specific tasks
- **\n**: want a new line 
```{
print("hello \n world")
will output: 
hello
world
```
- with escape sequence, they will be in the same line
- Other escape sequence: 
![escape sequence](Picture%20from%20lecture/Escape%20sequence.png)
- \ will display the things after. 
> Reserved words in python
- special words that have special meaning
- if: make condition
- for: run for loop
- range: generate sequence of number
- int: show integer type of number
- reserved words cannot be used as variable name. 

## Day 8: Data types in python part 1
> Data types in python
- Have to inform a complier or interpreter about data type
- Categorized different data type in different class
- Text-based, numbers, date, boolean. 

> Mutable and immutable data type
- **Mutable**: change or modify value of mutable data type value after creation, eg: *list, dictionary*
- **Immutable**: cannot change or modifty after creation, eg: *int, float, decimal, bool, string, tuple and range*
- [Mutable and immutable data type](Python%20exercise/Day%208%20Data%20types/mutable.py)

> Sequence and non-sequence data type in python
- **Sequence**: in which items are organized in well form and have their own index number, eg: list, tuple,string
- **Non-sequence**: not arranged in well form and does not have own index number, eg: set, dictionary
- [Sequence data type](Python%20exercise/Day%208%20Data%20types/Sequence.py)
- Non-sequence data type cannot have duplicate data, sequence data type can have duplicate data. 

> Categories of data types in python
- text-based data type
- numeric data type
- sequence data type
- mapping data type
- set data types
- boolean data type
- binary data type

## Day 9: Data types in python part 2
> Text-based data types
- String: collection of number, alphabetic in single or double quotation
- eg: "How are you?" 
- without assgining to a variable, """ will be considered as a comment 

> Number data types
- int: show whole number 
- float: fraction number, point number, e power number
- Complex: number in the form of x+yj (x: real number, yj: imaginary part), eg 3+3i 
- [Number data type](Python%20exercise/Day%208%20Data%20types/Number.py)

> List sequence data types
- list: sequence data type in which different data type elements may reside 
- element inside the list have their own index number
- **Mutable** data type 

> Tuple sequence data types
- Tuple: different type of data type may reside
- Element inside have their own index number
- **Immutable** data type 

> Range sequence data types
- range(start,stop,step): eg, range(1,11,1), generate number from 1 to 10
- range(5): will give value start from 0-4. 

> String sequence data types
- Empty string in boolean will give FALSE 
- Categorized in sequence data type
```
str="Hello"
str[1] # will give us result 'e'
```

>Dictionary sequence data type
- To access dictionary: 
```
My_data = {‘name’:’Faisal Zamir’, ‘age’:23, ’city’:’Paharpur’}
My_data['age'] # give us access to age
```

## Day 14 Type conversion in Python 
> Type method to find type of data
- Type() is used to find type of data in python

> Type conversion
- Type conversion is called type casting, can be implicit and explicit

> Implicit and Explicit
- Implicit type conversion: one data type is converted to another data type automatically when needed, eg add integer with float will always return float. 
- Explicit type conversion: one data type is converted to another data type by user, eg:
  ```
    c = 43
    print("Mary" + str(c))
    ```

## Day 16: Operator in Python
> What is operator? 
- Operator is the symbol which perform a operations on operand
- For example: a+b, + is the operator, a and b are the operands

## Day 17: Arithmetic operator
- For example: +: addition; -: subtraction; /: division; *: multiplication; %: Modulus.
- [Arithmetic example 1](python%20exercise/Day%2017%20Arithmetic%20operator/Arithmetic%20example%201.py)
- [Arithmetic example 2](Python%20exercise/Day%2017%20Arithmetic%20operator/Arithmetic%20exercise%202.py)

## Day 18: Relational operator
- Relational operator or comparison operator: to compare two value or to find a relation between two values
- To check equality: ==
- To check not equality: != 
- Greater than: >
- Greater than or equal to: >=
- Less than: <
- Less than or equal to: <=
- [Relational example 1](Python%20exercise/Day%2018%20Relational%20operator/Relational%20example%201.py)
- [Relational example 2](Python%20exercise/Day%2018%20Relational%20operator/Relational%20example%202.py)

## Day 20: Assignment operator
- "=" is the assignment operator. It is used to assign a value to a variable
- Compound operator: addition assignment operator: +=, a+=b is same as a = a+b; subtraction assignment operator: -=, a-=b is same as a = a-b
- a*=b is same as a = a*b; a%=b is same as a = a%b
- [Assignment example 1](Python%20exercise/Day%2020%20Assignment%20operator/Assignment%20exercise%201.py)
- [Assignment example 2](Python%20exercise/Day%2020%20Assignment%20operator/Assignment%20exercise%202.py)

## Day 21: Logic operator
- It returns boolean value, True or False
- and(&&) operator: return true only when every expression are true 
- or(||) operator: if one expression is true, return true; else return false 
- not(!) operator
- False and false = false
- false and true = false
- true and false = false
- true and true = true
- [Assignment example 1](Python%20exercise/Day%2021%20Logical%20operator/Assignment%20example%201.py)
- [Assignment example 2](Python%20exercise/Day%2021%20Logical%20operator/Assignment%20example%202.py)

## Day 22: Membership operator
- in: usually used in for loop, in check whether the variable or constant in a sequence. Return true if the number is in the sequence. 
- not in: opposite of in. 
- [Assignment example 1](Python%20exercise/Day%2022%20Membership%20operator/Membership%20operator%20exercise%201.py)
- [Assignment example 2](Python%20exercise/Day%2022%20Membership%20operator/Membership%20operator%20exercise%202.py)

## Day 23: Operator in python
- is: to check variables on both side of operator, same object or not. 
  ```
  print(x is y)
  # It will return true if x and y have same identity
  ```
- We can find their identities using id method: print(id(x)) that will return a number
-[Assignment example 1](Python%20exercise/Day%2023%20operator/Operator%20exercise%201.py)

## Day 24: Python operator precedence
- PEMDAS: parentheses, exponentiation, multiplication, division, addition and subtraction. 
- [Assignment example 1](Python%20exercise/Day%2024%20Python%20operator%20precedence/Precedence%20exercise%201.py)
- [Assignment example 2](Python%20exercise/Day%2024%20Python%20operator%20precedence/Precedence%20exercise%202.py)
- [Assignment example 3](Python%20exercise/Day%2024%20Python%20operator%20precedence/Precedence%20exercise%203.py)

## Day 27: Python exercise
- [Problem 1](Python%20exercise/Day%2027%20exercise/Problem%201.py)
- [Problem 2](Python%20exercise/Day%2027%20exercise/Problem%202.py)
- [Problem 3](Python%20exercise/Day%2027%20exercise/Problem%203.py)
- [Problem 4](Python%20exercise/Day%2027%20exercise/Problem%204.py)
- [Problem 5](Python%20exercise/Day%2027%20exercise/Problem%205.py)

## Day 28: Decision making structure in Python
> What is decision making structure
- The structure in which we provide a condition, on the basis of the condition, a statement or set of statement is execute. 
- if statement
- if...else statement
- Nest if statement
- if elif else statement
> if statement
- It takes a condition, if condition is true, then it execute a statement or set of statement
- If condition is false, no thing to display 
- [Problem 1](Python%20exercise/Day%2028%20If%20statement/Exercise%201)
- [Problem 2](Python%20exercise/Day%2028%20If%20statement/Exercise%202)

## Day 29: If else statement
- If condition is false, it will run else statement to display a false like statement or set of statement
- [Problem 1](Python%20exercise/Day%2029%20If%20else%20statement/Problem%201.py)
- [Problem 2](Python%20exercise/Day%2029%20If%20else%20statement/Problem%202.py)

## Day 30: Nested if statement
- Nested if is if statement inside another if statement block
  ```
  if(condition 1):
    if (condition 2):
      statement or set of statement
  ```
- Will execute if condition 1 is true and then condition 2 is true. 
- [Problem 1](Python%20exercise/Day%2030%20Nested%20if%20statement/Problem%201.py)
- [Problem 2](Python%20exercise/Day%2030%20Nested%20if%20statement/Problem%202.py)

## Day 31: Elif statement
- elif is used between if and else block
- elif is equal to else if
- Elif is used when we have to make multiple condition after if statement
  ```
  if (boolean expression/condition):
    statement
  elif(boolean expression/condition):
    statement
  else:
    statement
  ```
- [Problem 1](Python%20exercise/Day%2031%20Elif%20statement/Exercise%201.py)
- [Problem 2](Python%20exercise/Day%2031%20Elif%20statement/Exercise%202.py)

## Day 32: If statement practice
- [Problem 1](Python%20exercise/Day%2032%20If%20practice/Exercise%201.py)
- [Problem 2](Python%20exercise/Day%2032%20If%20practice/Exercise%202.py)
- [Problem 3](Python%20exercise/Day%2032%20If%20practice/Exercise%203.py)
- [Problem 4](Python%20exercise/Day%2032%20If%20practice/Exercise%204.py)
- [Problem 5](Python%20exercise/Day%2032%20If%20practice/Exercise%205.py)