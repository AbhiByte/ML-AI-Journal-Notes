import torch

# x = torch.randn(3, requires_grad=True)
# print(x)

# # x.requires_grad_(False)
# # x.detach()
# # with torch.no_grad():

# with torch.no_grad():
#     y = x + 2

#     print(y)


weights = torch.ones(4, requires_grad=True)

for epoch in range(2):
    model_output = (weights*3).sum()

    model_output.backward()

    print(model_output.retain_grad()) 
