# 🧠 SenioScan – Predicting Senior Citizens from Health Profiles


**SenioScan** is a machine learning-powered health application that predicts whether a person is a senior citizen (aged 65 or above) based on key health, lifestyle, and clinical features. It uses data from the **National Health and Nutrition Examination Survey (NHANES)** — a comprehensive U.S. public health dataset conducted by the **Centers for Disease Control and Prevention (CDC)**.

I originally built this project during **AI Planet’s NHANES Hackathon**, organized as part of the **Summer Analytics 2025** program by the **Consulting and Analytics Club, IIT Guwahati**.  
Later, I extended it into a full-fledged **Streamlit application** to demonstrate how hackathon models can be stretched into real-world, deployable solutions.

---

## 🔍 What is NHANES?

The **National Health and Nutrition Examination Survey (NHANES)** is a nationally representative health study by the CDC’s **National Center for Health Statistics**. It combines interviews, physical exams, and lab tests to assess the health and nutritional status of children and adults in the U.S. This project uses a clean subset (6,287 entries, 7 features) specifically curated to build an **age prediction model**.

---

## 🎯 Project Objective

To **predict whether an individual is a senior citizen (age 65+)** using key medical and lifestyle attributes.

---

## ⚙️ Model Building & Evaluation

I experimented with multiple classification algorithms to find the best performing model:

- ✅ Random Forest
- ✅ XGBoost
- ✅ CatBoost
- ✅ SVM (Support Vector Machine)
- ✅ AdaBoost

Each model was evaluated using **F1 score**, given the importance of balancing precision and recall in health data.

After comparison:
- **XGBoost** gave the best results.
- I **fine-tuned hyperparameters** (using GridSearchCV) to further improve model accuracy and performance.

---

## 📊 Features Used

- Body Mass Index (BMI)
- Alcohol consumption
- Smoking status
- Basic lab test values
- Reported physical activity
- Demographic indicators

---

## 🧪 Real-World Impact

As populations age globally, early identification of seniors based on health data helps in:
- Targeted medical interventions
- Public health strategy
- Personalized healthcare planning

This project simulates how healthcare systems or NGOs might screen individuals using quick and reliable health inputs.

---


