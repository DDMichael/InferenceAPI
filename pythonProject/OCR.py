from transformers import pipeline

# Initialize the pipeline with TrOCR model
ocr_pipeline = pipeline("image-to-text", model="microsoft/trocr-base-handwritten", device=0)

# Load an image from a URL or from a local file
image_path = "OCRTest.png"  # Replace with your image path
# If you want to use a URL instead:
# from PIL import Image
# import requests
# image = Image.open(requests.get(image_path, stream=True).raw)

# Run the OCR pipeline on the image
result = ocr_pipeline(image_path)

# Output the recognized text
print("Recognized text:", result[0]['generated_text'])
