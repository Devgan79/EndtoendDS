<h2>End-to-End Data Science Project</h2><br>
🧠 Overview<br>

This project implements a complete end-to-end data science workflow, from data ingestion and processing to model training, evaluation, and deployment. It includes:<br>

✔ Version control with DVC<br>
✔ Data storage & notebook experimentation<br>
✔ Production Python modules under src/<br>
✔ A web or CLI interface via app.py / main.py<br>
✔ A Docker container for reproducible builds<br>


├── .dvc/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                      # DVC versioning for datasets & models<br>
├── Dataset/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                  # Raw and processed data storage<br>
├── Notebooks/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;               # Jupyter notebooks for experimentation & EDA<br>
├── catboost_info/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;           # CatBoost model metadata<br>
├── src/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                     # Python modules used by scripts<br>
├── Dockerfile&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;               # Instructions for containerizing the app<br>
├── app.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                   # App entry point (API or UI interface)<br>
├── main.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                  # Script for training / running the pipeline<br>
├── requirements.txt&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;         # Python dependencies<br>
├── setup.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                 # Package setup for installation<br>
├── template.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;              # Utility / template code<br>
└── readme.md&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                # (Original placeholder)<br>

<h2>Installation</h2><br>

<h3>Clone the repo</h3><br>

git clone https://github.com/Devgan79/EndtoendDS.git<br>
cd EndtoendDS<br>

<h2>Install packages </h2><br>
pip install -r requirements.txt<br>
