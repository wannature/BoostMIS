import time
import os
import random
import numpy as np
import networkx as nx
import torch.nn.functional as F
import math
# Torch
from faiss import normalize_L2
import faiss
import torch
import numpy as np
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
import torch.optim.lr_scheduler as lr_scheduler
from adv import VATLoss
import copy
from scipy import sparse
# Torchvison
class al:
    def __init__(self, K=50, model=None):

        self.K = K
        self.model=None
def al_selection(self,args, model,un_loader=None):
    x = None
    y_l = None
    for img, label in un_loader:
        img = img.cuda()
        label = label.cuda()
        with torch.no_grad():
            _,_, feature_last = model(img)
            if y_l is not None:
                y_l = torch.cat((y_l, label),0)
                # print(y_l.shape)
            else:
                y_l = label

            if x is not None:
                x = torch.cat((x,feature_last),0)
                # print(x.shape)
            else:
                x=feature_last
    
    features = x.cpu()
    vus_ac=vus(args, model,features)
    bus_ac=bus(args, model,features)
    return  list(set(vus_ac).union(set(bus_ac)))

 def vus(args, model,features):
         vat_loss = VATLoss(xi=args.xi, eps=args.eps, ip=args.ip)
         lds, lds_each = vat_loss(model, features)
         lds_each = lds_each.view(-1)
         _, querry_indices = torch.topk(lds_each, int(args.K))
         querry_indices = querry_indices.cpu()
         return querry_indices


