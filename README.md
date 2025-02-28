Terrorism Prediction - Final Year Project
Overview
This project aims to predict the likelihood of terrorism-related events being suicide terrorist attacks. Using machine learning models such as LightGBM, this project analyzes historical terrorism data to identify patterns and predict future events. The project uses a combination of classification and time series analysis techniques to provide insights into terrorism trends across the globe.

Table of Contents
Project Structure
Installation
Usage
Model
Data
Future Improvements
Contributing
License
Project Structure
csharp
Copy
Edit
├── README.md
├── global-terrorism.csv
├── globalterrorismdb_0522dist.csv
├── gtd_clean_v2.csv
├── gtd_clean.csv
├── lightgbm_training/
│   ├── best_lightgbm_model.pkl
│   └── LightGBM.ipynb
├── data_clean/
│   ├── Data Cleaning.ipynb
│   └── globalterrorismdb_0522dist.csv
├── notebooks_and_datasets/
│   ├── terrorism-analysis_global.ipynb
│   └── terrorism-analysis.ipynb
├── time_series/
│   ├── time_series_1.ipynb
│   └── time_series_2.ipynb
├── gtc.py
├── requirements.txt
├── logo.jpeg
└── dataset-cover.jpeg
Installation
Clone this repository to your local machine:

bash
Copy
Edit
git clone https://github.com/yourusername/terrorism-prediction.git
Navigate to the project folder and create a virtual environment:

bash
Copy
Edit
cd terrorism-prediction
python3 -m venv venv
Activate the virtual environment:

For Windows:

Copy
Edit
venv\Scripts\activate
For macOS/Linux:

bash
Copy
Edit
source venv/bin/activate
Install the required dependencies:

Copy
Edit
pip install -r requirements.txt
Usage
Start the Streamlit App:

Run the following command to start the app in your local environment:

arduino
Copy
Edit
streamlit run gtc.py
Interact with the App:

Once the Streamlit app is running, you will be able to:

Filter terrorism-related events by various criteria (e.g., date, country, region, category).
View maps with markers for incidents.
Analyze the frequency and distribution of attacks using interactive pie charts.
Download the filtered data in CSV format.
View time series graphs for the number of deaths and injuries over time.
Model
The primary machine learning model used in this project is LightGBM, a gradient boosting framework that efficiently handles large datasets. The model predicts the probability of an event being a suicide terrorist attack.

Model Training
The model was trained using historical terrorism data, and it uses features like:

Casualties (deaths and injuries)
Country and region
Attack category
Perpetrator group
The model is saved as a .pkl file (best_lightgbm_model.pkl), which is loaded and used for prediction in the app.

Model Evaluation
Accuracy: 96% (based on the Area Under the Curve (AUC) metric)
Specificity: 86.5% (accurately classifying non-suicide attacks)
Data
The project uses several datasets related to global terrorism incidents. These datasets are cleaned and preprocessed to ensure that they are suitable for machine learning analysis.

globalterrorismdb_0522dist.csv: Original dataset containing global terrorism data.
gtd_clean_v2.csv: A cleaned version of the dataset.
gtd_clean.csv: Another cleaned version with a different data processing approach.
global-terrorism.csv: The final dataset used in the Streamlit app for interactive analysis.
Future Improvements
While this project provides a foundational prediction model and analysis tool, there are several areas for improvement and extension:

Model Refinement: Experiment with other models like XGBoost, Random Forest, or Neural Networks for better accuracy.
Additional Features: Incorporate more granular features, such as the exact type of weapon used in attacks or economic conditions.
Real-time Data Integration: Incorporate a mechanism to update predictions with live data.
Web Deployment: Deploy the Streamlit app on a public web server (e.g., Heroku, AWS, or Streamlit Sharing).
Contributing
We welcome contributions to this project! If you would like to contribute, please fork the repository and submit a pull request with your changes.

Steps to Contribute:
Fork this repository.
Create a new branch: git checkout -b feature-name
Commit your changes: git commit -am 'Add new feature'
Push to the branch: git push origin feature-name
Create a new Pull Request.
License
This project is licensed under the MIT License - see the LICENSE file for details.
