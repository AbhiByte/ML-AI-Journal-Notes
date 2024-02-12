import torch


x = torch.ones(2, 3, dtype=torch.float16)
print(x.dtype)
print(x.size())

y = torch.tensor([2.5, 0.1])
print(y)

y.add_(x)
print(y)

if torch.cuda.is_available():
    device = torch.device('cuda')
    x = torch.ones(5, device=device)
    
