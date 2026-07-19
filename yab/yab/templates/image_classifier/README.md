# Image Classifier

## Overview

The Image Classifier template generates PyTorch boilerplate for image classification tasks.

It is designed for datasets such as CIFAR-10, CIFAR-100, MNIST, FashionMNIST, ImageNet, and custom image datasets.

---

## Use Cases

- Image Classification
- CNN Training
- Transfer Learning
- Custom Vision Datasets

---

## Supported Abstractions

- Full
- Partial
- Raw

---

## Supported Models

- Custom CNN
- ResNet
- EfficientNet
- ConvNeXt
- Any PyTorch classification model

---

## User API

```python
trainer = yab.use(
    "image_classifier",
    type="full",
    num_classes=10
)
```

---

## Generated Components

- Model
- Trainer
- Training Loop
- Validation Loop
- Prediction
- Checkpointing
- Logging
- Main Function

---

## Directory

```
image_classifier/
├── metadata.yaml
├── README.md
├── full.py.j2
├── partial.py.j2
└── raw.py.j2
```

---

## Status

🚧 Under Development

## Roadmap

- [x] Template scaffold
- [ ] Metadata validation
- [ ] Jinja rendering
- [ ] `yab.use()` support
- [ ] `yab.write()` support
- [ ] Example projects
- [ ] Unit tests