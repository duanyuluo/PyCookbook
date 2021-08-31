#encoding=utf-8

from tools import *

i = new_intro("variables")

i.intro_chapter(
'''
# This is a comments, 
# it will be NOT execute after symbol # to the end of line

"""
This is a comment block.
You can type any text and any lines between the trible symbol "
"""
''')

i.section("define a variables without any TYPE declarement")
a = 10      # a is int type
b = "10"    # b is string type
b = '10'    # same above
c = 10.0    # c is float type

i.section("use type() to get variable type")
print("a = 10", probe_var(a))
print("b = '10'", probe_var(b))
print("c = 10.0", probe_var(c))

i.section("python is a Case-Sensitive language")
i.intro("so, 'a' and 'A' are two different variables")
i.intro("A = 20  this code can not modify the variable 'a' value")
A = 20
print("a =", a, " and A =", A)

i.section("casting some type to other type")
print("str(10)", probe_var(str(a)))
print("int('10')", probe_var(int(b)))

i.section("clearly recorgnize the different between string type and int type")
print("10 != '10'", probe_var(a == b))
print("str(10) == '10'", probe_var(str(a) == b))
print("10 + 10 = ", probe_var(a + a))
print("'10' + '10' = ", probe_var(b + b))
print("10 * 10 = ", probe_var(a * a))
print("'10' * 10 = ", probe_var(b * a))

i.section("A variable name can only contain alpha-numeric characters and underscores")
i.intro("(A-z, 0-9, and _ ) and NOT start with number and underscores")
i.intro("three popular name style:")
i.intro("1. Camel Case")
strName = "MicroFountain"
i.intro("2. Pascal Case <-- this is my Class's favarite style")
StrName = "MicroFountain"
i.intro("3. Snake Case <-- this is my Variable and Function's favarite style")
str_name = "MicroFountain"

# assign mutiple values
x, y, z = 10, "10", 10.0
print("x=", probe_var(x))
print("y=", probe_var(y))
print("z=", probe_var(z))

# and above code equal below (unpack collection assign)
x, y, z = (10, "10", 10.0)  # unpack tuple
x, y, z = [10, "10", 10.0]  # unpack array

# global variable and local variable
x = "awesome"   # global variable, you can look as '_global_x'

def func():
    x = "fantastic" # local variable, you can look as '_local_func_x'
    print(x)
    global y
    y = "20"        # global keyword, you can look as '_global_y'

# so, _global_x and _local_func_x are two different variables
print("local variable x =", func())      # use _local_func_x
print("global variable x =", x)          # use _global_x
print("global variable y=", y)           # use _global_y, so is '20', not '10'