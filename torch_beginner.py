#!/usr/bin/python3

from __future__ import print_function
import torch

x = torch.tensor([]) # create a empty tensor
x = torch.rand(5,3, dtype=torch.double) # pass the matrix value and the type

y = torch.rand(5,3) # create a var and pass the matrix value 
print(x + y) # put together those 2 var and print it.

# print(torch.add(x, y)) # 2 syntax mode

print(x.size()) # the tensor size

