# Fraud Detection in Financial Transactions
![header2_ed.png](https://github.com/LexC/Fraud_Classifier/blob/main/assets/header2_ed.png)
## Overview

This project focuses on detecting fraudulent transactions within financial datasets by employing advanced data analysis and machine learning techniques. Fraud detection is crucial for businesses, particularly in sectors like e-commerce, banking, and fintech, where fraudulent activities can lead to significant financial losses and damage to customer trust. Detecting fraud is challenging due to the imbalanced nature of the data, where fraudulent transactions are rare but have a significant impact.

The goal of this project is to build robust fraud detection solutions applicable to real-world scenarios, enabling organizations to minimize financial losses while maintaining operational efficiency.

For the full analysis, including EDA, preprocessing, feature engineering, and model evaluation, please go to the **Jupyter notebook** available at **`src/processing/data_analysis.ipynb`**.

## Project Highlights

- **Advanced Data Handling**: Automated the process of importing and preparing large datasets for analysis, featuring an integration with a **PostgreSQL** database hosted in a **Docker** container.
- **Comprehensive Data Analysis**: Demonstrated expertise in understanding, exploring, and visualizing complex datasets. Utilized a wide range of techniques, including descriptive statistics, correlation analysis, and visual tools like histograms and heatmaps to uncover insights and guide the model-building process.
- **Machine Learning Expertise**: Implemented a LightGBM classifier to tackle fraud detection in highly imbalanced datasets, optimized through hyperparameter tuning and class weighting to improve the model's performance in identifying fraudulent transactions.
- **Business-Oriented Analysis**: Evaluated the financial impact of fraud detection by measuring the reduction in fraud rates and potential savings in high-value transactions. The solution focused on optimizing both operational efficiency and financial results.
- **Model Interpretability & Insights**: Showcased model performance using detailed metrics such as precision, recall, F1-score, and accuracy, with an emphasis on improving business outcomes through effective fraud detection strategies.

## Relevance to Data-Driven Roles

This project demonstrates proficiency in key areas sought after in data-driven roles, including:

- **Data Engineering**: Managing large datasets, working with relational databases (PostgreSQL), and using Docker to containerize environments.
- **Data Analysis**: Conducting exploratory data analysis (EDA), handling missing data, and identifying key patterns through statistical analysis and visualizations.
- **Machine Learning**: Implementing and optimizing machine learning algorithms to solve real-world problems.
- **Business Impact**: Translating technical insights into measurable business outcomes, such as reducing fraud rates and minimizing financial loss.

The skills demonstrated in this project are transferable to a wide range of industries where data-driven decisions and advanced analytics are essential.

## Method

The fraud classification process followed a comprehensive data science pipeline, from data loading and exploratory data analysis (EDA) to machine learning model training and evaluation. The project involved preprocessing steps to clean and transform data, feature engineering, and model selection to handle the imbalanced nature of the dataset. Visualizations were extensively used to communicate insights and performance metrics to both technical and non-technical audiences.

### Folder Structure

```bash
src/
├── data/
│   ├── data_csv2sql.py       # Script for importing CSV data to a PostgreSQL database
├── processing/
│   └── data_analysis.ipynb   # Jupyter notebook for analyzing fraud detection data and evaluating ML model
├── init.py                   # Marks this directory as a package
install_venv_conda.sh         # Shell script for setting up the development environment
requirements.txt              # Dependencies for the project
LICENSE                       # License for the project
README.md                     # Documentation for the project

```

### Methodology Breakdown

[IMAGE EXPLAINING THE METHOD PROCESS]

1. **Data Loading**: The raw data was imported into a PostgreSQL database using a custom Python script (`data_csv2sql.py`). This ensured that the data was structured and easily accessible for further analysis. The script dynamically created the database table schema based on the CSV file structure, optimized data insertion, and handled missing values. It also ensured data integrity by implementing transaction handling, which rolled back changes in case of an error.
2. **Exploratory Data Analysis (EDA)**: The dataset was thoroughly explored to identify patterns and trends in both fraudulent and non-fraudulent transactions. A range of visualizations such as histograms, correlation heatmaps, and line charts were used to reveal key insights that guided model development. Additionally, descriptive statistics and correlation analysis were applied to better understand the relationship between features and how they influenced fraud detection accuracy.
3. **Preprocessing and Feature Engineering**: The data was thoroughly cleaned and transformed for optimal modeling. Missing values were handled by imputing median values for numerical features, given their non-parametric distribution, and replacing `NULL` values with `False` for non-submitted documents, indicating that the documentation wasn’t provided. Categorical variables were encoded using a combination of one-hot and label encoding to ensure proper representation in the model. High cardinality features were either simplified or removed to prevent performance degradation and maintain processing efficiency. Numerical features were scaled to ensure consistency, improving model performance during training.
4. **Model Selection & Training**: Several machine learning algorithms, including LightGBM, XGBoost, and Easy Ensemble, were evaluated with a focus on handling imbalanced data. LightGBM was ultimately chosen for its superior performance, balancing computational efficiency and high accuracy.
5. **Hyperparameter Tuning**: A Randomized Search with cross-validation was used to fine-tune the hyperparameters of the LightGBM model. Key parameters such as learning rate, maximum depth, and number of estimators were optimized to maximize the model's performance on detecting minority classes, improving its effectiveness in identifying fraud.
6. **Evaluation and Visualization**: Model performance was evaluated using standard classification metrics such as accuracy, precision, recall, F1-score, and ROC-AUC. Visualizations such as ROC curves, confusion matrices, and precision-recall curves were used to provide an intuitive understanding of the model’s effectiveness, particularly in distinguishing between fraudulent and non-fraudulent transactions. These visualizations made the model’s strengths and areas for improvement clear for stakeholders.

## Results and Discussion

### Model Performance

After tuning the LightGBM model using Randomized Search, we achieved a best **ROC-AUC score of 0.78**, indicating that the model effectively differentiates between fraudulent and non-fraudulent transactions. Below are the key performance metrics obtained from evaluating the model on the test set:

- **ROC-AUC**: 0.78 — This metric shows that the model is well-suited for distinguishing between the two classes, providing a good overall performance measure for fraud detection in imbalanced data.
- **Log-Loss**: 9.0294 — While relatively high, this reflects the difficulty of accurately predicting probabilities in an imbalanced dataset.
- **Precision-Recall AUC**: 0.29 — This metric reveals the complexity of maintaining a balance between precision and recall in highly imbalanced datasets, which is common in fraud detection.
- **Classification Report**:
    - **Fraud (Class 1)**: Precision of 0.14, Recall of 0.66, and an F1-Score of 0.22, reflecting the challenge of accurately predicting the minority class (fraud).
    - **Non-Fraud (Class 0)**: Precision of 0.97 and Recall of 0.75, showing the model's strong performance in identifying non-fraudulent transactions.

The machine learning implementation successfully addressed the challenge of detecting fraud in an imbalanced dataset. Techniques such as class weighting, hyperparameter tuning, and cross-validation played key roles in optimizing the model's performance. LightGBM emerged as the best-performing classifier, balancing computational efficiency with high accuracy.

While the model performed well, there is room for improvement, particularly in reducing false positives and enhancing precision for fraudulent transactions. Future work could explore advanced tools like SHAP for feature interpretability and consider additional tuning to further improve recall for fraud detection. This could help enhance the model’s overall performance, particularly in handling edge cases.

### Business Impact

- **Approval Rate**: 73%
- **Initial Fraud Rate**: 5%
- **Final Fraud Rate**: 2%
- **Fraud Detection Rate**: 66%
- **Money Saved**: 82% (approximately $73,054 saved out of $88,889 in total potential fraud loss)

At the beginning of the analyses, I identified that approximately 96% of transactions under $200 account for 90% of all fraud cases, as we can see in the next image.

![img1.png](https://github.com/LexC/Fraud_Classifier/blob/main/assets/img1.png)

This indicates that the vast majority of fraudulent activity occurs in lower-priced purchases. However, these 4% of fraud transactions accounts for 56% of the total financial losses. This indicates that even though fraud is more frequent in lower-priced sales, the financial impact of fraud in higher-priced transactions is significantly larger. 

After implementing the tuned model, the fraud rate dropped from 5% to 2%, successfully mitigating risk and protected revenue streams. More over, The model’s ability to identify high-value fraudulent transactions was particularly impactful, as these cases contribute significantly to potential financial losses. This is evidenced by having a 82% of profit into a fraud detection rate of 66% and by the image bellow.

![img2.png](https://github.com/LexC/Fraud_Classifier/blob/main/assets/img2.png)

### Final Considerations

The combination of strong performance metrics and favorable financial outcomes underscores the strategic importance of this fraud detection model. By reducing fraud rates and protecting revenue streams, the model demonstrates its capacity to drive profitability while minimizing financial risk. With further improvements, particularly in feature interpretability and recall, this model offers a scalable and effective solution for fraud detection in real-world applications.

This project highlights the power of machine learning in tackling critical business problems like fraud detection, showcasing how well-tuned models can optimize operations and deliver measurable business value.

