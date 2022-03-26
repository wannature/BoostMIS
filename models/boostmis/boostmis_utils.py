from itertools import count
import torch
import math
import torch.nn.functional as F
import numpy as np

from train_utils import ce_loss
count_temp=1

class Get_Scalar:
    def __init__(self, value):
        self.value = value

    def get_value(self, iter):
        return self.value

    def __call__(self, iter):
        return self.value


def consistency_loss(logits_s, logits_w, class_acc, p_target, p_model, name='ce',
                     T=1.0, a=0.9, b=0.05, p_cutoff=0.95, N_a=100, K=100, use_hard_labels=True, use_DA=False):
    assert name in ['ce', 'L2']
    logits_w = logits_w.detach()
    if name == 'L2':
        assert logits_w.size() == logits_s.size()
        return F.mse_loss(logits_s, logits_w, reduction='mean')

    else:
        assert Exception('Not Implemented consistency_loss')
