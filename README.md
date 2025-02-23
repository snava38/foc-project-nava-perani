# **NYC Trip Fare Analysis**

## **Introduction**
This project is part of the *Foundations of Computer Science* course in the **Master’s degree in Data Science**, under the supervision of **Professor Gianluca della Vedova**. The goal is to analyze taxi trips in **New York City** using data from the [NYC Trip Fare dataset](https://www.kaggle.com/datasets/diishasiing/revenue-for-cab-drivers). The analysis involves data cleaning, feature engineering, and extracting insights based on trip details, fare amounts, and passenger behaviors.

## **Objectives**
The analysis focuses on the following tasks:

### **Filtering and Cleaning:**
- Extract all trips with a **distance greater than 50 miles**.
- Identify and extract trips where **payment_type is missing**.
- Remove trips with **missing VendorID, passenger_count, store_and_fwd_flag, payment_type**, and store them in a separate dataset (`bad`).

### **Trip Statistics and Aggregations:**
- Compute the **number of trips** for each `(PULocationID, DOLocationID)` pair.
- Add a **trip duration column**, calculated from `tpep_pickup_datetime` and `tpep_dropoff_datetime`.
- Determine how many trips **started from each pickup location**.
- Cluster pickup times into **30-minute intervals** (e.g., *02:00 - 02:30*).

### **Fare and Payment Analysis:**
- Compute the **average number of passengers and fare amount per interval**.
- Compute the **average fare per payment type and time interval**.
- Identify the **interval with the highest average fare per payment type**.
- Identify the **interval with the highest tip-to-fare ratio per payment type**.
- Find the **pickup location with the highest average fare amount**.

### **Common Destinations Analysis:**
- Build a new dataset (`common`) that keeps, for each pickup location, only the **five most common dropoff locations**.
- Compare **fare averages between the original and common datasets** and compute relative differences.

### **Trip Chaining Analysis:**
- Identify **chains of trips**, where consecutive trips satisfy these conditions:
  1. They share the **same VendorID**.
  2. The **dropoff location of one trip is the pickup location of the next**.
  3. The **second trip starts after the first trip ends**.
  4. The **second trip starts within 2 minutes** of the previous dropoff.

Each trip chain is assigned a **chain ID** to facilitate further analysis.

## **Dataset**
The dataset can be downloaded from: [NYC Trip Fare Dataset](https://www.kaggle.com/api/v1/datasets/download/diishasiing/revenue-for-cab-drivers/)

## **Implementation**
The project is implemented in **Python**, using:
- **Pandas** for data manipulation
- **NumPy** for numerical operations
- **Matplotlib/Seaborn** for visualization
