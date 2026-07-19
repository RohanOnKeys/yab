# image_classifier

PyTorch CNN-based image classification template.

## Abstraction Levels

- **full** — complete end-to-end training script with data loading, model definition, training loop, evaluation, and checkpointing.
- **partial** — model class and training step as importable components; no inline data pipeline.
- **raw** — minimal skeleton: imports, class stub, and optional `__main__` block.

## Usage

```bash
yab generate image_classifier full --project-name cat_vs_dog --model-name ResNetClassifier
yab generate image_classifier partial --model-name ResNetClassifier
yab generate image_classifier raw --model-name ResNetClassifier
```

## Context Variables

| Variable | Type | Default | Description |
|---|---|---|---|
| `project_name` | str | `my_project` | Output script name |
| `model_name` | str | `MyModel` | Model class name |
| `num_classes` | int | `2` | Number of output classes |
| `learning_rate` | float | `0.001` | Optimizer learning rate |
| `batch_size` | int | `32` | Dataloader batch size |
| `num_epochs` | int | `10` | Training epochs |
| `device` | str | `cuda` | Compute device |
| `image_size` | int | `224` | Input image resolution |
| `in_channels` | int | `3` | Number of input channels |
