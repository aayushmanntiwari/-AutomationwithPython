from Functions import Add
from Functions import Sub
from Functions import Mult
from Functions import Div

value = int(input('''Which operation you want to perform in the spreesheet:
1.Addition 
2.Substraction 
3.Divison 
4.Multiplication
        '''))
if value == 1:
    Add.Add()
elif value == 2:
    Sub.Sub()
elif value == 3:
     Div.Div()
elif value == 4:
     Mult.Mult()
else:
    print("Wrong Input")
