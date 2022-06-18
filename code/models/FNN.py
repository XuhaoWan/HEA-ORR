   #!/usr/bin/env python
# -*- coding:utf-8 -*-
#author: xhwan


import torch
from torch import nn
import torch.nn.functional as F
import torch.utils.data as Data
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import numpy as np
from torchvision import datasets, transforms
from torch.nn import init
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import r2_score
from sklearn.neural_network import MLPRegressor
from sklearn import preprocessing

dataset = np.loadtxt('dataset.csv',  delimiter=',', dtype="float")

dataset_label = np.loadtxt('dataset_label.csv', delimiter=",", dtype="float")



x = dataset


ss = MinMaxScaler()
x = ss.fit_transform(x)
y = dataset_label

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1)


x_train = torch.from_numpy(x_train).type(torch.FloatTensor)
y_train = torch.from_numpy(y_train).type(torch.FloatTensor)
x_test = torch.from_numpy(x_test).type(torch.FloatTensor)
y_test = torch.from_numpy(y_test).type(torch.FloatTensor)
y_test = torch.unsqueeze(y_test, 1)
y_train = torch.unsqueeze(y_train, 1)



BATCH_SIZE = 15
LR = 0.05
EPOCH = 50


torch_data = Data.TensorDataset(x_train, y_train)
loader = Data.DataLoader(dataset=torch_data, batch_size=BATCH_SIZE, shuffle=True)


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.hidden = nn.Linear(90, 64)
        self.predict = nn.Linear(64, 1)

    def forward(self, x):
        x = F.relu(self.hidden(x))
        x = self.predict(x)
        return x



def weights_init(m):
    if isinstance(m, nn.Linear):
        init.kaiming_normal(m.weight.data)


adam_net = Net()

opt_adam = torch.optim.Adam(adam_net.parameters(), lr=LR)
loss_func = nn.MSELoss()


all_loss = {}


for epoch in range(EPOCH):
    print('epoch', epoch)
    for step, (b_x, b_y) in enumerate(loader):
        print('step', step)
        pre = adam_net(b_x)
        loss = loss_func(pre, b_y)
        opt_adam.zero_grad()
        loss.backward()
        opt_adam.step()
        all_loss[epoch+1] = loss
        
        
print(all_loss)
print(loss)



yt = y_train.numpy()
yp = adam_net(x_train)
yp = yp.detach().numpy()
rmse = np.sqrt(mse(yt, yp))
r2 = r2_score(yt, yp)
yt1 = y_test.numpy()
yp1 = adam_net(x_test)
yp1 = yp1.detach().numpy()
rmset = np.sqrt(mse(yt1, yp1))
r2t = r2_score(yt1, yp1)


print(rmse)
print(r2)
print(rmset)
print(r2t)
