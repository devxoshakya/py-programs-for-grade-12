
def push(stk,e):
    stk.append(e)
    top = len(stk)-1
def display(stk):
    if check_stack_isEmpty(stk):
        print("Stack is Empty")
    else:
        top = len(stk)-1
        print(stk[top],"-Top")
        for i in range(top-1,-1,-1):
            print(stk[i])
def pop_stack(stk):
    if check_stack_isEmpty(stk):
        return "UnderFlow"
    else:
        e = stk.pop()
        if len(stk)==0:
            top = None
        else:
            top = len(stk)-1
        return e
def peek(stk):
    if check_stack_isEmpty(stk):
        return "UnderFlow"
    else:
        top = len(stk)-1
        return stk[top]

str = str(input('Enter your string :'))
a = str[::-1]
print('Reverse of the above string is',a)

