"""
Example: Training an image classifier on a custom dataset using YAB.

This example shows how to use YAB with your own image dataset.
"""

import yab

# Initialize the image classifier template
# Adjust parameters based on your dataset
model = yab.use("image_classifier", type="full",
                num_classes=5,           # Number of classes in your dataset
                input_channels=3,        # 3 for RGB, 1 for grayscale
                batch_size=32,
                epochs=40,
                lr=0.0005)

# Get the configured trainer
trainer = model.get_trainer()

# Start training
# In a real implementation, you would provide your dataset path
trainer.fit(data_path="path/to/your/images")
