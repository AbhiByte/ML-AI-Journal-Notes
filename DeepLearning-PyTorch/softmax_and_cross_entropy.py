import torch
import torch.nn as nn
import numpy as np

def softmax(x):
    return np.exp(x) / np.sum(np.exp(x), axis=0)

X = np.array([2.0, 1.0, 0.1])
outputs = softmax(X)
print('softmax output', outputs)

x = torch.tensor([2.0, 1.0, 0.1])
outputs = torch.softmax(x, dim=0)
print('torch softmax', outputs)

def cross_entropy(actual, predicted):
    loss = -np.sum(actual * np.log(predicted))
    return loss

Y = np.array([1, 0, 0])
Y_sm_good = np.array([0.7, 0.2, 0.1])
Y_sm_bad = np.array([0.08, 0.7, 0.5])
loss_good = cross_entropy(Y, Y_sm_good)
loss_bad = cross_entropy(Y, Y_sm_bad)
print(f"good loss numpy: {loss_good}")
print(f"bad loss numpy: {loss_bad}")

loss = nn.CrossEntropyLoss()
Y = torch.tensor([0.0]) # correct class label
Y_pred_good = torch.tensor([2.0]) # no softmax
Y_pred_bad = torch.tensor([0.4])

l1 = loss(Y_pred_good, Y)
l2 = loss(Y_pred_good, Y)
print(f"l1: {l1.item()}, l2: {l2.item()}")

# Mulitclass example
class MultiClassNN(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(MultiClassNN, self).__init__()
        self.linear1 = nn.Linear(input_size, hidden_size)    
        self.relu = nn.ReLU()
        self.linear2 = nn.Linear(hidden_size, num_classes)
        self.sigmoid = nn.Sigmoid()

    
    def forward(self, x):
        out = self.linear1(x)
        out = self.relu(out)
        out = self.linear2(out)
        out = self.sigmoid(out)
        # no softmax at end
        return out
    

model = MultiClassNN(input_size=28*28, hidden_size=5, num_classes=3)
criterion = nn.CrossEntropyLoss() # applies softmax


