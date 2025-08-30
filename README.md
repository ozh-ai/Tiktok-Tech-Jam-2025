# Tiktok-Tech-Jam-2025
Track #1: Filtering the Noise: ML for trustworthy location reviews

## Project Overview

This project aims to assess the **quality and relevancy of Google location reviews** using a combination of **Machine Learning (XGBoost)** and **Natural Language Processing (TF-IDF features)**.
The system can detect:

* Spam or advertisements
* Irrelevant reviews
* Reviews from users who likely have not visited the location

A custom feature (`contains_link`) is also added to help identify reviews containing links, which are strong indicators of advertisements.

---

## File Structure

```
.
├── README.md
├── data/
│   └── reviews_labeled.csv   # Generated dataset for training/testing
|   └── Alaska.json           # Dataset for evaluation
├── main.ipynb                # Notebook to train, evaluate, and test the model
├── reviews_generator.py      # Script to generate labeled review data
```

---

## Setup Instructions

1. **Clone or download the repository**:

```bash
git clone <repository_url>
cd <repository_folder>
```

2. **Generate the test dataset**:

Run the `reviews_generator.py` script to create the dataset used to test the machine learning model:

```bash
python reviews_generator.py
```

This will generate `60000_reviews.csv` in the `data/` folder.

---

## How to Reproduce Results

1. Open the notebook (Use Jupyter Notebook / Google Colab):

```bash
jupyter notebook main.ipynb
```

2. Follow the notebook steps to:

   * Load the generated data from `data/reviews_labeled.csv`
   * Preprocess the reviews
   * Train the pipeline model (TF-IDF + text\_length + LinkDetector + XGBoost)
   * Evaluate performance using classification metrics (precision, recall, F1-score, confusion matrix)
   * Test on sample or external datasets

3. You can also add or test **new reviews** by creating a DataFrame with `text` and `text_length` and passing it through the trained pipeline.

---

## Notes

* The `LinkDetector` transformer automatically flags reviews containing URLs or domain names to improve advertisement detection.
* You can expand the dataset with new reviews to improve generalization on outside data.
* For reproducibility, random seeds are fixed in train/test split and XGBoost.

---

## Contact / References

* Author: *Ong Zheng Han*
* Contact: *zhenghanong@gmail.com*

