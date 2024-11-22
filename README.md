### Predicting the Impact of Climate Change on Agricultural Productivity

This project focuses on predicting the impact of climate change on agricultural productivity using machine learning regression models. The goal is to analyze how climate-related variables and agricultural practices influence crop yields and provide insights for sustainable agriculture.

---

#### **Table of Contents**
1. [Project Overview](#project-overview)  
2. [Dataset Description](#dataset-description)  
3. [Major Steps in the Workflow](#major-steps-in-the-workflow)  
4. [Machine Learning Models](#machine-learning-models)  
5. [Model Evaluation and Results](#model-evaluation-and-results)  
6. [Conclusion](#conclusion)  
7. [How to Run the Code](#how-to-run-the-code)

---

### **Project Overview**
Agriculture is highly sensitive to climate change, and understanding the impact of various climate factors is essential for mitigating risks. This project predicts crop yield using climate and agricultural data, enabling better decision-making for adaptation strategies.

---

### **Dataset Description**
The dataset contains information about various climate and agricultural factors across countries and regions. Below are the columns included in the dataset:

- **Year:** Year of data collection  
- **Country:** Name of the country  
- **Region:** Geographic region within the country  
- **Crop_Type:** Type of crop grown (e.g., Wheat, Corn, etc.)  
- **Average_Temperature_C:** Average temperature (°C) during the crop season  
- **Total_Precipitation_mm:** Total rainfall (mm)  
- **CO2_Emissions_MT:** Carbon dioxide emissions (metric tons)  
- **Crop_Yield_MT_per_HA:** Crop yield (metric tons per hectare) (Target variable)  
- **Extreme_Weather_Events:** Frequency of extreme weather events  
- **Irrigation_Access_%:** Percentage of irrigation access  
- **Pesticide_Use_KG_per_HA:** Pesticide usage (kg per hectare)  
- **Fertilizer_Use_KG_per_HA:** Fertilizer usage (kg per hectare)  
- **Soil_Health_Index:** Soil quality index (0–100)  
- **Adaptation_Strategies:** Strategies implemented to adapt to climate change  
- **Economic_Impact_Million_USD:** Economic impact in USD (millions)

---

### **Major Steps in the Workflow**

1. **Dataset Selection**  
   - The dataset includes climate and agricultural parameters spanning multiple regions and time periods.

2. **Data Preprocessing**  
   - Handled missing values, encoded categorical variables (e.g., Country, Region, and Crop_Type), and normalized numerical features.

3. **Data Visualization**  
   - Explored relationships between climate factors and crop yield using heatmaps, scatterplots, and histograms.

4. **Feature Engineering**  
   - Selected key features affecting crop yield:  
     ```
     Features:
     'Average_Temperature_C', 'Total_Precipitation_mm', 'CO2_Emissions_MT', 
     'Extreme_Weather_Events', 'Pesticide_Use_KG_per_HA', 
     'Fertilizer_Use_KG_per_HA',
     ```
     - Target: `Crop_Yield_MT_per_HA`

5. **Model Selection**  
   - Implemented three regression models:
     - **Linear Regression**
     - **Gradient Boosting Regressor**
     - **Random Forest Regressor**

6. **Model Evaluation**  
   - Evaluated performance using metrics like:
     - Mean Absolute Error (MAE)
     - Mean Squared Error (MSE)
     - R² Score

---

### **Machine Learning Models**

- **Linear Regression**  
  A simple model to identify linear relationships between features and the target variable.

- **Random Forest Regressor**  
  An ensemble-based algorithm that combines multiple decision trees for robust predictions.

- **Gradient Boosting Regressor**  
  The best-performing model in this project. It iteratively optimizes the model to minimize errors, achieving high accuracy for crop yield prediction.

---

### **Model Evaluation and Results**

The best model, **Gradient Boosting Regressor**, achieved the highest accuracy. Below are the evaluation metrics for the models:


| **Model**                  | **MAE**       | **MSE**     | **R² Score** |
|----------------------------|---------------|-------------|--------------|
| Linear Regression          | 0.814320545   | 0.983519670 | 0.0681706    |
| Random Forest Regressor    | 0.7272096     | 0.7474276   | 0.29185449   |
| **Gradient Boosting**      | **0.71851841**| **0.7177450** | **0.3199771** |
| XGBoost Regressor          | 0.72828064    | 10.7523119 | 0.287226921       |

---

### **Conclusion**

This project demonstrates the potential of machine learning to predict crop yields based on climate and agricultural factors. The Gradient Boosting Regressor proved to be the most effective model, emphasizing the importance of ensemble methods in capturing complex relationships.

---

### **How to Run the Code**

1. **Clone the Repository**  
   ```
   git clone <repository_link>
   cd <repository_folder>
   ```

2. **Install Dependencies**  
   Ensure you have the necessary Python libraries installed:
   ```
   pip install -r requirements.txt
   ```

3. **Run the Streamlit App**  
   ```
   streamlit run app.py
   ```
   This will launch an interactive web app for predicting crop yield based on input features.

4. **Access the Jupyter Notebook**  
   Open the notebook for further analysis:
   ```
   jupyter notebook FINAL_GOMYCODE_Project_1.ipynb
   ```

---

### **Future Improvements**

- Incorporate additional climate variables like wind speed and solar radiation.  
- Extend the dataset to include more diverse regions and crops.  
- Implement deep learning models for more nuanced predictions.  
