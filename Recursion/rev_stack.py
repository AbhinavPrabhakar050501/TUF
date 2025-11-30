def insert_at_bottom(stack,val):#last element from the other function is appended here.
    if not stack:
        stack.append(val)
        return
    
    top_val = stack.pop()
    insert_at_bottom(stack,val)
    stack.append(top_val)

def reverse_stack(stack):
    if not stack:
        return

    top = stack.pop() 
    reverse_stack(stack)

    # stack.insert(0,top)
    insert_at_bottom(stack,top)

if __name__ == "__main__":
    stack = [4,1,3,2]
    reverse_stack(stack)
    print(stack)