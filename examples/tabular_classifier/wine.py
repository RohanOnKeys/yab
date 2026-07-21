"""
Example: Training a tabular classifier on Wine dataset using YAB.

This example demonstrates how to use YAB to train a classifier
on the Wine dataset for wine type classification.
"""

import yab

# Initialize the tabular classifier template
# Wine dataset has 13 input features and 3 classes
model = yab.use("tabular_classifier", type="full",
                input_features=13,
                num_classes=3,
                hidden_dims=[128, 64],
                batch_size=16,
                epochs=150,
                lr=0.001)

# Get the configured trainer
trainer = model.get_trainer()

# Start training
trainer.fit()
