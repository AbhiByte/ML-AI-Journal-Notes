# Ok, now lets try using Pytorch
import torch.nn as nn
import torch.optim
import pandas as pd

# Import training set
df = pd.read_csv(r'Kaggle/Competitions/Titanic/data/train.csv')

class NeuralNet:
    def __init__(self):
        super(NeuralNet, self).__init__()
        self.fc1 = nn.Linear(5, 10) # 5 features? 10 neurons
        self.fc2 = nn.Linear(10, 1) # 1 output neuron

    
    def forward(self, x):
        pass




