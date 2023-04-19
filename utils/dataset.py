import pandas as pd
import numpy as np
import torch

class Dataset():
    def __init__(self, data_path):
        self.path = data_path
        #if dataset is csv, using pandas:
        self.data = pd.read_csv(self.path)
    
    def __getitem__(self, index):
        data = (np.array([self.data.iloc[index , 1 :]]))
        label = (np.array(self.data.iloc[index , 0]))
        return torch.reshape(torch.from_numpy(data).float(),(28,28)).unsqueeze_(0), torch.from_numpy(label)
    
    def __len__(self):
        return len(self.data)
    
