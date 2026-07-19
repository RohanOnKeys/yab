# Tabular Classifier

## Overview

The Tabular Classifier template generates PyTorch boilerplate for supervised learning on structured tabular datasets.

It is suitable for CSV datasets and other feature-based classification tasks.

---

## Use Cases

- Customer Churn Prediction
- Fraud Detection
- Credit Risk Analysis
- Medical Diagnosis
- General Tabular Classification

---

## Supported Abstractions

- Full
- Partial
- Raw

---

## Supported Models

- Feed Forward Neural Networks (MLP)
- Custom PyTorch Models

---

## User API

```python
trainer = yab.use(
    "tabular_classifier",
    type="full",
    input_features=20,
    num_classes=4
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

---

## Directory

```
tabular_classifier/
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