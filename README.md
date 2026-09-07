# AI-Based Phishing and Spam Detection System

## 📌 Project Overview

The **AI-Based Phishing and Spam Detection System** is a machine learning project designed to identify unwanted and potentially harmful messages.

The system analyzes the text of a message and classifies it as either:

- **Spam** – unwanted or suspicious message
- **Ham** – legitimate message

## 🎯 Objectives

- Detect spam messages automatically using Machine Learning.
- Reduce the risk of users interacting with suspicious messages.
- Apply Natural Language Processing (NLP) techniques to text data.
- Build a simple and effective classification system.

## 🛠️ Technologies Used

- Python
- Pandas
- Scikit-learn
- Natural Language Processing (NLP)
- TF-IDF Vectorization
- Multinomial Naive Bayes
- Visual Studio Code
- Git & GitHub

## 📊 Dataset

The project uses the **SMS Spam Collection Dataset**, containing **5,572 SMS messages** classified as spam or ham.

## 🤖 Machine Learning Model

The system uses:

1. **TF-IDF Vectorization** – converts text messages into numerical features.
2. **Multinomial Naive Bayes** – classifies messages as spam or ham.

The model was trained using an **80:20 training-testing split**.

## 📈 Current Result

The current model achieved an accuracy of approximately:

**96.68%**

## 🧪 Sample Predictions

| Message Type | Prediction |
|---|---|
| iPhone prize message | Spam |
| Class notes message | Ham |
| Urgent cash prize message | Spam |

## 👥 Project Team

This project is being developed as a group project by Diploma CSE students.

## 📌 Project Status

**Progress Update 1**

Current work completed:

- Dataset collected and prepared
- Dataset loaded successfully
- Text preprocessing performed
- TF-IDF features created
- Multinomial Naive Bayes model trained
- Model tested successfully
- Accuracy achieved: **96.68%**
- Project uploaded to GitHub

## 🚀 Future Scope

- Develop a user-friendly web interface.
- Add phishing URL detection.
- Improve model performance using additional datasets.
- Provide real-time message classification.
- Deploy the system as a web application.