import torch
import torch.nn as nn
import torch.nn.functional as F

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        
        self.conv1 = nn.Conv2d(1, 32, 3, 1)
        
        self.conv2 = nn.Conv2d(32, 64, 3, 1)
        
        self.drop_out1 = nn.Dropout2d(0.25)
        self.drop_out2 = nn.Dropout2d(0.5)
        
        self.fc1 = nn.Linear(9216, 128)
        self.fc2 = nn.Linear(128, 10)
        

NN = Net()
print(NN)        
        
        