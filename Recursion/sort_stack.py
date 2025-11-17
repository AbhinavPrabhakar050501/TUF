#recursive sorting stack algorithm
# need 2 functions one for sort
# and one for inserting at the correct position

def insert_stack(stack,element):
    if not stack or element > stack[-1]:
        stack.append(element)
        return

    top = stack.pop()
    insert_stack(stack,element)

    stack.append(top)

def sort_stack(stack):
    if not stack:
        return
    top = stack.pop()
    sort_stack(stack)
    insert_stack(stack,top)

if __name__ == "__main__":
    stack = [3,4,5,1]
    sort_stack(stack)
    print(stack)