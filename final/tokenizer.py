Token_Info = ["Integer",    #0
"Boolean",                  #1
"Variable",                 #2
"Variable Assignment",      #3
"Addition Operator",        #4
"Subtraction Operator",     #5
"Print Function",           #6
"Open Parenthesis",         #7
"Close Parenthesis"         #8
]

def Tokenizer(python_code):
    f = open(python_code, 'r')
    Token_List = []
    #----------------------------------------------------------------
    #Implement here to return Token_List  
    #containing Tuples with Token Information
    
    # Token_List.append(("CS101", Token_Info[2])) # remove this line! It's just for an example
    def find_type(var):
        if var.isdigit():
            return Token_Info[0]
        elif var in ["False", "True"]:
            return Token_Info[1]
        elif var == "=":
            return Token_Info[3]
        elif var == "+":
            return Token_Info[4]
        elif var == "-":
            return Token_Info[5]
        elif var == "print":
            return Token_Info[6]
        elif var == "(":
            return Token_Info[7]
        elif var == ")":
            return Token_Info[8]
        else:
            if var[0].isdigit():
                return None
            for ch in var:
                if not ch.isalpha() and not ch.isdigit():
                    return None
            return Token_Info[2]

    for row in f.readlines():
        code = row.split()
        for elem in code:
            Token_List.append((elem, find_type(elem)))
    
    #-----------------------------------------------------------------
    return Token_List

def HowToUse_isalpha():
    print("alphabet".isalpha()) # True
    print("111".isalpha())      # False
    print("a1".isalpha())       # False
    print("(".isalpha())        # False

def HowToUse_isdigit():
    print("alphabet".isdigit()) # False
    print("111".isdigit())      # True
    print("a1".isdigit())       # False
    print("(".isdigit())        # False

if __name__ == "__main__":
    result = Tokenizer("examples/ex1.py") # You can modify this line to test another example
    
    #HowToUse_isalpha()        #You can use this line to see how to use isalpha()
    #HowToUse_isdigit()        #You can use this line to see how to use isdigit()

    # Below code prints out the result in the same way as the given “examples/ex1.py” file
    # It is recommended not to modify the below.
    print("[", end =" ")
    for tup in result[:-1]:
        print(str(tup)+",")
    print(result[-1])
    print("]")