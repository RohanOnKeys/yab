"""
Example: Training a text classifier on IMDB sentiment using YAB.

This example demonstrates how to use YAB to train a sentiment classifier
on the IMDB movie review dataset.
"""

import yab

# Initialize the text classifier template
# IMDB sentiment analysis has 2 classes (positive/negative)
model = yab.use("text_classifier", type="full",
                num_classes=2,
                model_name="bert-base-uncased",
                max_length=512,
                batch_size=16,
                epochs=3,
                lr=2e-5)

# Get the configured trainer
trainer = model.get_trainer()

# Start training
trainer.fit()
