📰 News Sentiment Analysis

This project is a sentiment analysis model built using news headlines and descriptions to classify sentiment as positive, neutral, or negative. It uses various machine learning models, including XGBoost, Naive Bayes, Random Forest, Logistic Regression and SMOTE technique for handling class imbalance.

📌 Project Overview

Dataset: Kaggle News Sentiment Analysis Dataset

Goal: Classify the sentiment of news descriptions

Techniques Used:
🔹 NLP-Based Data Preprocessing & Feature Engineering
✅ Cleaned text (removed stopwords, punctuation, lemmatization)
✅ Applied TF-IDF (Term Frequency-Inverse Document Frequency) for text vectorization
✅ Used SMOTE (Synthetic Minority Over-sampling Technique) to balance the dataset
🔹 Model training & evaluation with multiple algorithms
🔹 Hyperparameter tuning

🛠 Step 4: Implementing NLP-Driven Machine Learning Models
🔹 Random Forest (Best accuracy: 92%) – Outperformed XGBoost in my case!
🔹 Logistic Regression (Accuracy: 90%) – A strong traditional model for text classification
🔹 XGBoost (Best accuracy: 93%) – Tuned using hyper-parameter optimization (Optuna)
🔹 Naïve Bayes (MultinomialNB) – Compared with XGBoost for baseline performance

## 🧠 Future Work

- Fine-tuning BERT for sentiment classification
- Adding visualizations to compare model performance
- Deploying the best-performing model via a web interface
