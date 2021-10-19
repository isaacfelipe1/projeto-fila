from typing import List

stack:List[str]=[]
try:
    stack.append('A')
    stack.append('B')
    stack.append('C')
    item=stack.pop()
    print(stack,item)
    item=stack.pop()
    print(stack,item)
    item=stack.pop()
    print(stack,item)
    item=stack.pop()
    print(stack,item)
except IndexError:
     print("Sua pilha está vazia")
for item in stack[::-1]:
    print(item)
print("\n Sua pilha :", stack)