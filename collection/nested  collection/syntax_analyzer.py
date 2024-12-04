user_input=input("Enter Brackets:")#{}

bracket_pair={"{":"}","(":")","[":"]","<":">"}

symbol_stack=[]

top=-1

is_valid=True

for symbol in user_input:#{}

    if symbol in bracket_pair:

        top+=1

        symbol_stack.append(symbol)

    elif top==-1:

        is_valid=False

    elif symbol==bracket_pair.get(symbol_stack[top]):

        symbol_stack.pop()

        top-=1

    else:

        is_valid=False

if top!=-1:

    is_valid=False

print(is_valid)