def rep_char(c, n):
    return c*n

def draw_line_string(msg1,msg2):
    n = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)
    print('-' * n)

for i in range(2):
    name= input('Input his/her name:')
    draw_line_string(msg1,msg2)
    msg1='Hello '+ name +'.'
    msg2='Welcome to Seoul.'
    print(msg1)
    print(msg2)
    draw_line_string(msg1,msg2)
