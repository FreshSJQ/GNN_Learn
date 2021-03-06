
import argparse
import numpy as np

import torch

parser = argparse.ArgumentParser()
parser.add_argument('--no-cuda', action='store_true', default=False,
                    help='Disables CUDA training.')
parser.add_argument('--fastmode', action='store_true', default=False,
                    help='Validate during traing pass.')                    
parser.add_argument('--seed', type=int, default=42, help='Random seed.')                    
parser.add_argument('--epochs', type=int, default=0.01,
                    help='Initial learning rate.')
parser.add_argument('--lr', type=float, default=0.01,
                    help='Initial learning rate.')
parser.add_argument('--weight_decay', type=int, default=16,
                    help='Number of hidden units.')
parser.add_argument('--dropout', type=float, default=16,
                    help='Dropout rate (1 - keep probability).')                                                            

args = parser.parse_args()
args.cuda = not args.no_cuda and torch.cuda.is_available()

np.random.seed(args.seed)
torch.manual_seed(args.seed)

if args.cuda:
    torch.cuda.manual_seed(args.seed)

