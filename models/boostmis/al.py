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

# def vus(args, model,features):
#         vat_loss = VATLoss(xi=args.xi, eps=args.eps, ip=args.ip)
#         lds, lds_each = vat_loss(model, features)
#         lds_each = lds_each.view(-1)
#         _, querry_indices = torch.topk(lds_each, int(args.K))
#         querry_indices = querry_indices.cpu()
#         return querry_indices

# def bus(args, model,features):
#     M = int(args.M)  
#     d = features.shape[1]
#     res = faiss.StandardGpuResources()
#     flat_config = faiss.GpuIndexFlatConfig()
#     flat_config.device = int(torch.cuda.device_count()) - 1
#     index = faiss.GpuIndexFlatIP(res,d,flat_config)   # build the index
#     temp_vector = copy.deepcopy(x).numpy()
#     normalize_L2(temp_vector)
#     index.add(temp_vector) 
#     N = temp_vector.shape[0]
#     Nidx = index.ntotal
#     c = time.time()
#     D, I = index.search(temp_vector, M)
#     D = D[:,1:] 
#     I = I[:,1:]
#     row_idx = np.arange(N)
#     row_idx_rep = np.tile(row_idx,(M-1,1)).T
#     r = sparse.csr_matrix((D.flatten('F'), (row_idx_rep.flatten('F'), I.flatten('F'))), shape=(N, N))
#     r = r + r.T
#     r[r>0] = 1
#     del temp_vector 
#     excout = model(features)
#     excout = F.softmax(excout, dim=1)
#     excout = excout.cpu()
#     excout = excout.detach().numpy()
#     predicted = excout.max(1)
#     entropy_list = -excout * np.log(excout)
#     entropy_list = np.add.reduce(entropy_list, axis=1) 
#     entropy_list=entropy_list.numpy().tolist()
#     entropy_list = [i * r[i] for i in entropy_list] 
#     balanced_list_0=[]
#     balanced_list_1=[]
#     for i in range(len(predicted)):
#         if predicted[i]==0:
#             balanced_list_0.append(entropy_list[i])
#         if predicted[i]==1:
#             balanced_list_1.append(entropy_list[i])
    
#     entropy_list_0=torch.Tensor(balanced_list_0)
#     entropy_list_0 = torch.FloatTensor(balanced_list_0)
#     entropy_list_1=torch.Tensor(balanced_list_1)
#     entropy_list_1 = torch.FloatTensor(balanced_list_1)
#     K=args.K//args.num_classes
#     _, querry_indices_en_0 = torch.topk(entropy_list_0, int(args.K))
#     _, querry_indices_en_1 = torch.topk(entropy_list_1, int(args.K))
#     sampled_indices=list(querry_indices_en_0)+list(querry_indices_en_1)
#     return sampled_indices

