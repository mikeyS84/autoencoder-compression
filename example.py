"""
Run a quick shape‑check with random data.

Place this file in the same folder as autoencoder.py
and run: python example.py
"""

import torch
from autoencoder import Autoencoder

# two random 150×225 RGB images
dummy = torch.randn(2, 3, 150, 225)

model = Autoencoder()
out = model(dummy)

print("input  shape :", dummy.shape) # (2, 3, 150, 225)
print("output shape:", out.shape)    # should match input
