# problem
"""Print the number of times that the substring occurs in the given string. String traversal will take place from left to right only."""

# long method
def f(s, sub_s):
    count = 0
    len_sub_s = len(sub_s)
    if len(s) <= len_sub_s:
        return -1
    while len_sub_s < len(s) + 1 :
        if s[:len_sub_s] == sub_s:
            count += 1
        s = s[1:]
    return count

# one-line
olf = lambda s, sub_s: sum(1 if s[i:i+len(sub_s)] == sub_s else 0 for i in range(len(s)))

# test
s = "jajkhfjajajaja"
sub_s = 'jaja'
print(f(s, sub_s))  # 3
print(olf(s, sub_s))  # 3
