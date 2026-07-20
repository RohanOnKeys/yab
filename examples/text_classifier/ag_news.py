"""
Example: Training a text classifier on AG News using YAB.

This example demonstrates how to use YAB to train a topic classifier
on the AG News dataset (4 categories).
"""

import yab

# Initialize the text classifier template
# AG News has 4 classes (World, Sports, Business, Sci/Tech)
model = yab.use("text_classifier", type="full",
                num_classes=4,
                model_name="distilbert-base-uncased",
                max_length=256,
                batch_size=32,
                epochs=4,
                lr=3e-5)

# Get the configured trainer
trainer = model.get_trainer()

# Start training
trainer.fit()
