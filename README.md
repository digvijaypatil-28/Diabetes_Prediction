# 🩺 Diabetes Predictor App

A simple web-based application built with **Flask** that predicts whether a person has diabetes based on several health parameters. The model is trained using a **Random Forest Classifier** and leverages machine learning to make predictions.

## 🔍 Project Overview

This application takes user input such as glucose level, blood pressure, BMI, age, etc., and predicts the likelihood of having diabetes. It uses a pre-trained model saved as a `.pkl` file and displays the prediction through a user-friendly web interface.

## 💡 Features

- 🎯 Predicts diabetes status using 8 health indicators
- 🧠 Uses a trained Random Forest machine learning model
- 💻 Built with Flask and rendered using HTML templates
- 📁 Simple and intuitive web interface

## 🚀 How It Works

1. User inputs health data in the form on the homepage.
2. Data is passed to the Flask backend.
3. Pre-trained machine learning model (`.pkl` file) makes the prediction.
4. The result is displayed on a new page (`result.html`).

## 🛠️ Tech Stack

| Technology     | Description                         |
|----------------|-------------------------------------|
| Python         | Backend Language                    |
| Flask          | Web Framework                       |
| HTML/CSS       | Frontend (via `index.html`)         |
| Pickle         | For loading the trained model       |
| NumPy          | For data formatting and processing  |


## 📊 Input Features

The model takes the following inputs:

- Pregnancies
- Glucose
- Blood Pressure
- Skin Thickness
- Insulin
- BMI (Body Mass Index)
- Diabetes Pedigree Function
- Age

🙌 Acknowledgements
Dataset from the Pima Indians Diabetes Database

Inspired by projects using ML for healthcare

