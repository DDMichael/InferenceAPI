from transformers import pipeline
# Initialize the zero-shot-classification pipeline
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli", device=0)

# Define the candidate labels
candidate_labels = ["Semantic Segmentation", "Object Detection", "OCR"]

# Classify a prompt
prompt = "Help me locate the elephant in this image."
result = classifier(prompt, candidate_labels)

# Output the predicted label
print(result)