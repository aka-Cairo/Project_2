

[Link to Dataset](https://www.kaggle.com/datasets/rohit265/credit-card-eligibility-data-determining-factors/)

# Credit Card Eligibility Dataset Analysis

## Project Overview

This project aims to analyze and make predictions based on the **Credit Card Eligibility Dataset: Determining Factors**. The dataset is a comprehensive collection of variables aimed at understanding the factors that influence an individual's eligibility for a credit card. 

## Dataset Description

The dataset includes a wide range of demographic, financial, and personal attributes that are commonly considered by financial institutions when assessing an individual's suitability for credit. Each row represents a unique individual, identified by a unique ID, with associated attributes.
| Variable        | Description                                                                                                                                  |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| ID              | An identifier for each individual (customer).                                                                                                |
| Gender          | The gender of the individual.                                                                                                                |
| Own_car         | A binary feature indicating whether the individual owns a car.                                                                               |
| Own_property    | A binary feature indicating whether the individual owns a property.                                                                          |
| Work_phone      | A binary feature indicating whether the individual has a work phone.                                                                         |
| Phone           | A binary feature indicating whether the individual has a phone.                                                                              |
| Email           | A binary feature indicating whether the individual has provided an email address.                                                            |
| Unemployed      | A binary feature indicating whether the individual is unemployed.                                                                            |
| Num_children    | The number of children the individual has.                                                                                                   |
| Num_family      | The total number of family members.                                                                                                          |
| Account_length  | The length of the individual's account with a bank or financial institution.                                                                 |
| Total_income    | The total income of the individual.                                                                                                          |
| Age             | The age of the individual.                                                                                                                   |
| Years_employed  | The number of years the individual has been employed.                                                                                        |
| Income_type     | The type of income (e.g., employed, self-employed, etc.).                                                                                    |
| Education_type  | The education level of the individual.                                                                                                       |
| Family_status   | The family status of the individual.                                                                                                         |
| Housing_type    | The type of housing the individual lives in.                                                                                                 |
| Occupation_type | The type of occupation the individual is engaged in.                                                                                         |
| Target          | The target variable for the classification task, indicating whether the individual is eligible for a credit card or not (e.g., Yes/No, 1/0). |

### Key Features

- **Demographic Information**
  - Gender
  - Age

- **Financial Indicators**
  - Total Income
  - Employment Status

- **Personal Attributes**
  - Familial Status
  - Housing
  - Education
  - Occupation

## Objectives

The primary objectives of this project are to:
1. **Understand** the key factors that influence credit card eligibility.
2. **Analyze** the dataset to extract meaningful insights.
3. **Build Predictive Models** to determine the likelihood of an individual's eligibility for a credit card.

## Methodology

1. **Data Exploration and Preprocessing**
   - Load and inspect the dataset.
   - Handle missing values and outliers.
   - Encode categorical variables.
   - Normalize/standardize numerical features.

2. **Exploratory Data Analysis (EDA)**
   - Visualize the distribution of key features.
   - Identify correlations between variables.
   - Detect patterns and trends in the data.

3. **Model Building**
   - Split the data into training and testing sets.
   - Train various machine learning models (e.g., Logistic Regression, Decision Trees, Random Forest, SVM, etc.).
   - Evaluate model performance using appropriate metrics (e.g., accuracy, precision, recall, F1-score).

4. **Model Selection and Optimization**
   - Compare model performances.
   - Tune hyperparameters for the best model.
   - Validate the model on the testing set.

## Requirements

- Python 3.x
- Libraries:
  - pandas
  - numpy
  - matplotlib
  - seaborn
  - scikit-learn

## Usage

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/credit-card-eligibility-analysis.git
    cd credit-card-eligibility-analysis
    ```

2. Install the required libraries:
    ```sh
    pip install -r requirements.txt
    ```

3. Run the analysis:
    ```sh
    python main.py
    ```

## Contributors
Rajeev Daithankar
Jacqueline Columbro
Matthew Harper


## License
This project is licensed under the MIT License.

## Acknowledgements
We would like to thank Kaggle and the author, Rohit Sharma for providing the dataset used in this analysis: Credit Card Eligibility Data: Determining Factors
Understanding the Dynamics of Credit Card Eligibility: Insights from a Comprehensive Collection.