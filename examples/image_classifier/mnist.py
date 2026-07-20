"""
Example: Training an image classifier on MNIST using YAB.

This example demonstrates how to use YAB to train a classifier
on the MNIST handwritten digit dataset.
"""

import yab

# Initialize the image classifier template
# MNIST has 10 classes and 1 grayscale channel
model = yab.use("image_classifier", type="full",
                num_classes=10,
                input_channels=1,
                batch_size=64,
                epochs=30,
                lr=0.001)

# Get the configured trainer
trainer = model.get_trainer()

# Start training
trainer.fit()
