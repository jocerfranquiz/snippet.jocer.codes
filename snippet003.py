# problem
"""Given a string s and width w, wrap the string into a paragraph of width w."""

# long method
def f(s, w):
    blocks = len(s)//w
    if len(s)%w != 0:
        blocks += 1
    new_s = ''
    for i in range(blocks):
        new_s += f'\n{ s[i*w:(i+1)*w] }'
    return new_s[1:]

# one-line
olf = lambda s,w: '\n'.join( s[i*w:(i+1)*w] for i in range(len(s)//w + 1 if len(s)%w else len(s)//w) )

# with std lib
import textwrap

slf = lambda s,w: textwrap.fill(s,w)

# test
s = '0984n5ny0945yn0439ny0wegfiwgqawioeq'
w = 13

print(f'{f(s, w)}\n{olf(s, w)}\n{slf(s, w)}')  # 0984n5ny0945y\nn0439ny0wegfi\nwgqawioeq
