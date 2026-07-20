"""
Example: Training a text classifier on a custom dataset using YAB.

This example shows how to use YAB with your own text dataset.
"""

import yab

# Initialize the text classifier template
# Adjust parameters based on your dataset
model = yab.use("text_classifier", type="full",
                num_classes=10,           # Number of classes in your dataset
                model_name="bert-base-uncased",
                max_length=128,           # Adjust based on your text length
                batch_size=16,
                epochs=5,
                lr=2e-5)

# Get the configured trainer
trainer = model.get_trainer()

# Start training
# In a real implementation, you would provide your dataset path
trainer.fit(data_path="path/to/your/text_data")
