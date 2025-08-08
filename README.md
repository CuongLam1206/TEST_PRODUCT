# GenImageAI
A system that generates high-quality images from natural language text prompts

## 📋 Overview

This project implements a full-stack application featuring:

- A FastAPI backend serving the text-to-image model for inference
- An HTML/CSS/JavaScript frontend for interactive prompt input and image display
- Integration with a translation module to support multilingual prompts
- GPU acceleration for fast image synthesis using Stable Diffusion XL
- Docker for containerization and easy deployment

## 💻 Usage

1. Setup Model Files

- Create a folder named weights inside the folder: E:\TEST_PRODUCT\backend\shared
- Download the model file from this Google Drive link: https://drive.google.com/file/d/1xrItYfDMEhbO3C2FTOrXF6e0nVHQleLc/view?usp=drive_link

- After downloading, place the model file inside the folder: E:\TEST_PRODUCT\backend\shared\weights.
- Next, create a .env file in your project root containing the following content:
        T2I__BASE_MODEL_ID='YOUR_BASE_MODEL_ID'
        T2I__LORA_WEIGHTS='shared/weights'

2. Once the application is running:

- Access the frontend at: http://localhost:8080/
- The backend API is available at: http://localhost:8000/docs
