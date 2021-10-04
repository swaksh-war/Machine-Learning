import torch

x = torch.tensor([1,2,3,4])
w = torch.tensor([3,4,5,6])
b = torch.tensor([6,7,8,9])

y = x * w + b 
print(y)