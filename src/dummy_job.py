#dummy job for slurm
import time
import torch

a = torch.ones(100000).cuda()
while True:
    a = torch.add(a,a)
    print (a)
    time.sleep(1)
