# 🚀 Terrorism Prediction - Final Year Project

## 📌 Overview

This project aims to predict the likelihood of terrorism-related events being suicide terrorist attacks. Using machine learning models such as **LightGBM**, it analyzes historical terrorism data to identify patterns and predict future events. The project integrates **classification** and **time series analysis** techniques to provide insights into global terrorism trends.

---

## 📖 Table of Contents

- [📁 Project Structure](#-project-structure)
- [🛠 Installation](#-installation)
- [🚀 Usage](#-usage)
- [🧠 Model](#-model)
- [📊 Data](#-data)
- [📈 Future Improvements](#-future-improvements)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)

---

## 📁 Project Structure

```
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
```

---

## 🛠 Installation

### 🔹 Clone the Repository

```bash
git clone https://github.com/yourusername/terrorism-prediction.git
cd terrorism-prediction
```

### 🔹 Create a Virtual Environment

```bash
python3 -m venv venv
```

### 🔹 Activate the Virtual Environment

**For Windows:**

```bash
venv\Scripts\activate
```

**For macOS/Linux:**

```bash
source venv/bin/activate
```

### 🔹 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

### 🔹 Start the Streamlit App

```bash
streamlit run gtc.py
```

### 🔹 Features

- **Filter** terrorism-related events by **date, country, region, and attack category**.
- **Interactive Map** with markers representing incidents.
- **Download Filtered Data** in CSV format.
- **View Time Series Graphs** for attack frequency, deaths, and injuries.

---

## 🧠 Model

### 🔹 Primary Model: **LightGBM**

- A gradient boosting framework that efficiently handles large datasets.
- Predicts whether an event is a **suicide terrorist attack**.

### 🔹 Model Training

The model is trained using historical terrorism data with features such as:

- **Casualties (deaths and injuries)**
- **Country and region**
- **Attack category**
- **Perpetrator group**

### 🔹 Model Performance

- **Accuracy**: **83%**
- **Specificity**: **86.5%** (correctly classifies non-suicide attacks)

---

## 📊 Data

### 🔹 Datasets Used

| Dataset                          | Description                                        |
| -------------------------------- | -------------------------------------------------- |
| `globalterrorismdb_0522dist.csv` | Original dataset with global terrorism incidents.  |
| `gtd_clean_v2.csv`               | Preprocessed and cleaned version of the dataset.   |
| `gtd_clean.csv`                  | Another cleaned version with a different approach. |
| `global-terrorism.csv`           | Final dataset used in the Streamlit app.           |

---

## 📈 Future Improvements

🚀 **Potential Enhancements:**

- 🔹 **Model Refinement:** Experiment with **XGBoost**, **Random Forest**, or **Neural Networks**.
- 🔹 **Additional Features:** Incorporate detailed features such as **weapon type and economic conditions**.
- 🔹 **Real-time Data Integration:** Connect the model to **live data sources** for up-to-date predictions.
- 🔹 **Web Deployment:** Deploy on **Heroku, AWS, or Streamlit Cloud**.

---

## 🤝 Contributing

We welcome contributions to improve this project! 🚀

### 🔹 Steps to Contribute:

1. **Fork** this repository.
2. **Create a new branch:**
   ```bash
   git checkout -b feature-name
   ```
3. **Commit your changes:**
   ```bash
   git commit -am 'Add new feature'
   ```
4. **Push to the branch:**
   ```bash
   git push origin feature-name
   ```
5. **Create a Pull Request!** 🎉

---

## 📜 License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.

---

🔗 **Project Maintainer:** Abu-Bakar khilji
📧 **Contact:** [armaan1900@outlook.com](mailto\:your.email@example.com)

