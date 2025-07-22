# Image Compression with a Convolutional Autoencoder
This repo shows how to compress 150 × 225 RGB images with a simple PyTorch autoencoder.

## Install

```
git clone https://github.com/mikeyS84/autoencoder-compression.git
cd autoencoder-compression
pip install -r requirements.txt
```

## Train on your data

```
python autoencoder.py --data data/
```

## Test a saved model

```
python autoencoder.py --data data/ --checkpoint model.pt --test
```

## Quick check

```
python example.py
```

Verifies the model runs and keeps the same input–output shape.
