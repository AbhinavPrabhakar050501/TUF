# Q1) Generate element based on row and col
def generate_element(n,r):
    res = 1
    for i in range(r):
        res = res * (n-i)
        res = res//(i+1) 
    return res

# Q2) Generate row based on row
def generate_row(n):
    res = 1
    res_list = [1]
    for i in range(n):
        res = res * (n-i)
        res = res//(i+1)
        res_list.append(res)
    return res_list

def pascal_traingle(numRows):
    '''
    Q3) Generate full pascal traingle

    '''
    op_triangle = []
    for i in range(numRows):
        op_triangle.append(generate_row(i))
    return op_triangle

# Q4) Can try with DP array