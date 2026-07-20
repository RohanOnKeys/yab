"""
Example: Training a tabular classifier on a custom dataset using YAB.

This example shows how to use YAB with your own tabular dataset.
"""

import yab

# Initialize the tabular classifier template
# Adjust parameters based on your dataset
model = yab.use("tabular_classifier", type="full",
                input_features=20,       # Number of features in your data
                num_classes=5,            # Number of classes in your dataset
                hidden_dims=[128, 64, 32],  # Custom hidden layer sizes
                batch_size=32,
                epochs=200,
                lr=0.0005)

# Get the configured trainer
trainer = model.get_trainer()

# Start training
# In a real implementation, you would provide your dataset path
trainer.fit(data_path="path/to/your/tabular_data")
