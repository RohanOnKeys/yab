"""
Example: Training an image classifier on CIFAR-10 using YAB.

This example demonstrates how to use YAB to train a classifier
on the CIFAR-10 dataset with minimal boilerplate.
"""

import yab

# Initialize the image classifier template
# CIFAR-10 has 10 classes and 3 color channels (RGB)
model = yab.use("image_classifier", type="full", 
                num_classes=10,
                input_channels=3,
                batch_size=128,
                epochs=50,
                lr=0.001)

# The trainer is automatically configured
# In a real implementation, this would handle:
# - Data loading and preprocessing
# - Model training loop
# - Validation and metrics
trainer = model.get_trainer()

# Start training
trainer.fit()
