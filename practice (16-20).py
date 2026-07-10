#problem no.16
num1,num2 = int(input("Enter num2:")), int(input("Enter num1:"))
print("before swapping num1:",num1,"num2:",num2)
print("after swapping num1:",num2,"num2:",num1)

#sortcut.
num1 = num1+num2
num2 = num1-num2
num1 = num1-num2
print("num1:",num1, "num2:",num2)

#problem no.17
int_value = int(input("your intezer value:"))
print("orginal value:",int_value,"| type:",type(int_value))

float_value = float(int_value)
print("float value:",float_value,"| type:",type(float_value))

#problem no. 18
float_value = float(input("your float value:"))
print("orginal value:",float_value,"|type:",type(float_value))
int_value = int(float_value)
print("int value:",int_value, "| type:",type(int_value))

#problem no. 19
str_num = input("your string number:")
print("orginal value:",str_num,"| type:",type(str_num))
int_num = int(str_num)
print("intezer value:",int_num,"| type:",type(int_num))

#sortcut.
int_value = int(input("your string number:"))
print("intezer value:",int_value,"| type:",type(int_value))

#problem no. 20
name = "opu Gosh."
age = 17
hight = 5.4
I_am_student = True
print("Name:",type(name), "Age:",type(age), "Hight:",type(hight), "who:",type(I_am_student)) 

