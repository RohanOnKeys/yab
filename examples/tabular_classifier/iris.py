"""
Example: Training a tabular classifier on Iris dataset using YAB.

This example demonstrates how to use YAB to train a classifier
on the classic Iris flower dataset.
"""

import yab

# Initialize the tabular classifier template
# Iris has 4 input features and 3 classes
model = yab.use("tabular_classifier", type="full",
                input_features=4,
                num_classes=3,
                hidden_dims=[64, 32],
                batch_size=16,
                epochs=100,
                lr=0.001)

# Get the configured trainer
trainer = model.get_trainer()

# Start training
trainer.fit()
