# Text Classifier

## Overview

The Text Classifier template generates PyTorch boilerplate for supervised text classification tasks.

It supports Hugging Face Transformers and custom PyTorch NLP models.

---

## Use Cases

- Sentiment Analysis
- Spam Detection
- Topic Classification
- Intent Detection
- News Classification

---

## Supported Abstractions

- Full
- Partial
- Raw

---

## Supported Models

- BERT
- DistilBERT
- RoBERTa
- DeBERTa
- Custom Transformer Models

---

## User API

```python
trainer = yab.use(
    "text_classifier",
    type="full",
    num_classes=2
)
```

---

## Generated Components

- Tokenizer
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
text_classifier/
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