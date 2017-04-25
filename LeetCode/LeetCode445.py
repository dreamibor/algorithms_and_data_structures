a = [4,5,8] # 458
b = [6,5,8,0]
# c = a + b
from collections import deque
stack_a = deque()
stack_b = deque()
result = deque()

def is_empty(queue):
    return queue == deque()

for i in a:
    stack_b.append(i)
print(stack_b)
for i in b:
    stack_a.append(i)
print(stack_a)

add_one_flag = 0
while not is_empty(stack_a) and not is_empty(stack_b):
    num = stack_a.pop() + stack_b.pop() + add_one_flag
    result.appendleft(num % 10)
    add_one_flag = 1 if num - 10  >= 0 else 0

stack_c = deque()
if not is_empty(stack_a):
    stack_c = stack_a
elif not is_empty(stack_b):
    stack_c = stack_b

while not is_empty(stack_c):
    num = stack_c.pop() + add_one_flag
    result.appendleft(num % 10)
    add_one_flag = 1 if num - 10  >= 0 else 0

if add_one_flag == 1:
    result.appendleft(1)

print(result)


    