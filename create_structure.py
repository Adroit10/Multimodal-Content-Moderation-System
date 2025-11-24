import os

BASE_DIR_NAME = r"F:\DATA SCIENCE\Projects\MultiModel Content Moderation"
folders = [
    f"{BASE_DIR_NAME}/data/raw",
    f"{BASE_DIR_NAME}/data/processed",
    f"{BASE_DIR_NAME}/data/images",
    f"{BASE_DIR_NAME}/models/checkpoints",
    f"{BASE_DIR_NAME}/models/final_model",
    f"{BASE_DIR_NAME}/notebooks",
    f"{BASE_DIR_NAME}/src",
    f"{BASE_DIR_NAME}/src/data",
    f"{BASE_DIR_NAME}/src/models",
    f"{BASE_DIR_NAME}/src/training",
    f"{BASE_DIR_NAME}/src/deployment",
    f"{BASE_DIR_NAME}/config",
]

files = {
    f"{BASE_DIR_NAME}/notebooks/01_EDA_and_Wrangling.ipynb":"",
    f"{BASE_DIR_NAME}/notebooks/02_Model_Prototyping.ipynb":"",
    f"{BASE_DIR_NAME}/notebooks/03_Final_Evaludation.ipynb":"",
    f"{BASE_DIR_NAME}/src/__init__.py":"",
    f"{BASE_DIR_NAME}/src/data/dataset.py":"# Dataset and Data loader classes\n",
    f"{BASE_DIR_NAME}/src/data/processing.py":"# Text cleaning and image transformation function\n",
    f"{BASE_DIR_NAME}/src/models/fusion.py":"# Fusion block (cross-attention/ multimodal)\n",
    f"{BASE_DIR_NAME}/src/training/train.py":"# Training script\n",
    f"{BASE_DIR_NAME}/src/training/metrics.py":"# Custom metrics and loss functions\n",
    f"{BASE_DIR_NAME}/src/deployment/app.py":"# Streamlit/Flask/Gradio\n",
    f"{BASE_DIR_NAME}/config/config.yaml":"# Configuration parameters\n",
    f"{BASE_DIR_NAME}/README.md":"# Multimodal Content Moderation System\n",
    f"{BASE_DIR_NAME}/.gitignore":"*.pyc\n__pycache__/\n.ipynb_checkpoints/\nmodels/checkpoints/\ndata/\n",
}

for fol in folders:
    os.makedirs(fol,exist_ok=True)

for file_path,content in files.items():
    with open(file_path,"w",encoding="utf-8") as f:
        f.write(content)
print("Project Structure created successfully")

