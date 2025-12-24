import torch

x = torch.tensor(3.0, requires_grad=True)

# y = (2x + 1)³

# 단계별로 분해해보자

g = 2 * x + 1
z = g ** 3

z.backward()
print(f'x = {x.item()}')
print(f'g = 2x + 1 = {g.item()}')
print(f'z = g³ = {z.item()}')
print(f'dz/dx = {x.grad.item()}')

'''================================================='''

x = torch.tensor(3.0, requires_grad=True)

a = 2 * x  # = 2x
print(a.item())
b = a + 1  # = 2x + 1
print(b.item())
y = b ** 3  # = (2x + 1)³
print(y.item())

y.backward()

print(f'dy/dx = {x.grad.item()}')
