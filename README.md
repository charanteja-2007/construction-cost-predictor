# AI Construction Cost & Material Predictor

A machine learning-based web application that estimates the **total construction cost, cement requirement, and steel requirement** based on basic building specifications.

The application is built using **Python, Streamlit, and Scikit-learn** and is deployed as an interactive web application.

## Live Demo

[Construction Cost & Material Predictor](https://construction-cost-predictor.streamlit.app/)

## Project Overview

Estimating construction costs and material requirements during the initial planning stage can be challenging because several factors influence the overall requirement.

This project uses machine learning models to provide quick estimates based on:

* Built-up area
* Number of floors
* Structure type
* Location tier
* Material grade

The application predicts three important outputs:

1. Estimated total construction cost
2. Estimated cement requirement
3. Estimated steel requirement

## Features

### Construction Cost Prediction

Estimates the total construction cost based on the building specifications entered by the user.

### Cement Requirement Prediction

Predicts the approximate amount of cement required in bags.

### Steel Requirement Prediction

Predicts the approximate quantity of steel required in kilograms.

### Cost per Square Foot

The application also calculates the estimated construction cost per square foot.

### Simple Web Interface

The application provides an easy-to-use interface where users can enter building details and receive predictions instantly.

## Input Parameters

The application requires the following information:

| Parameter        | Description                                        |
| ---------------- | -------------------------------------------------- |
| Built-up Area    | Total built-up area of the building in square feet |
| Number of Floors | Number of floors in the building                   |
| Structure Type   | Type of structural system                          |
| Location Tier    | Location category used by the trained model        |
| Material Grade   | Selected material grade                            |

## Output

After entering the required information, the application provides:

| Output               | Unit              |
| -------------------- | ----------------- |
| Estimated Total Cost | Indian Rupees (₹) |
| Cement Required      | Bags              |
| Steel Required       | Kilograms (kg)    |
| Cost per Square Foot | ₹/sqft            |

## Machine Learning Models

The project uses separate machine learning models for predicting different construction requirements.

* `cost_model.pkl` — Construction cost prediction
* `cement_model.pkl` — Cement requirement prediction
* `steel_model.pkl` — Steel requirement prediction

The models are loaded using `joblib` and cached using Streamlit's resource caching mechanism.

The application uses a **Random Forest Regressor** for prediction.

## Data Preprocessing

Categorical variables are converted into numerical values using Scikit-learn's label encoding.

The project includes the following encoders:

* `le_structure.pkl` — Structure type encoder
* `le_location.pkl` — Location tier encoder
* `le_grade.pkl` — Material grade encoder

The encoded features are passed to the respective machine learning models for prediction.

## Technology Stack

### Programming Language

* Python

### Libraries and Frameworks

* Streamlit
* Scikit-learn
* Pandas
* NumPy
* Joblib

### Machine Learning

* Random Forest Regressor
* Label Encoding

### Deployment

* Streamlit Community Cloud

## Project Structure

```text
construction-cost-predictor/
│
├── app.py
├── cost_model.pkl
├── cement_model.pkl
├── steel_model.pkl
├── le_structure.pkl
├── le_location.pkl
├── le_grade.pkl
├── requirements.txt
├── .gitignore
└── README.md
```

## How the Application Works

```text
User Input
    |
    v
Building Specifications
    |
    +-------------------------+
    |                         |
    v                         v
Categorical Encoding     Numerical Features
    |                         |
    +------------+------------+
                 |
                 v
        Machine Learning Models
                 |
       +---------+---------+
       |         |         |
       v         v         v
     Cost     Cement     Steel
   Prediction Prediction Prediction
       |         |         |
       +---------+---------+
                 |
                 v
          Results Displayed
```

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/construction-cost-predictor.git
```

Navigate to the project directory:

```bash
cd construction-cost-predictor
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

## Requirements

The project requires the following Python packages:

```text
streamlit
scikit-learn
joblib
pandas
numpy
```

These dependencies are also listed in `requirements.txt`.

## Example Workflow

1. Enter the built-up area of the building.
2. Enter the number of floors.
3. Select the structure type.
4. Select the location tier.
5. Select the material grade.
6. Click **Predict Cost & Materials**.
7. View the estimated construction cost, cement requirement, steel requirement, and cost per square foot.

## Important Note

The predictions generated by this application are **estimates** intended for preliminary planning and educational purposes.

Actual construction costs and material requirements can vary depending on factors such as:

* Local material prices
* Labour costs
* Structural design
* Foundation requirements
* Soil conditions
* Building specifications
* Market conditions
* Transportation costs
* Site conditions

The model should therefore not be considered a substitute for detailed structural design, quantity estimation, or professional construction cost estimation.

## Deployment

The application is deployed using Streamlit Community Cloud.

Live application:

https://construction-cost-predictor.streamlit.app/

## Future Improvements

Possible improvements for future versions include:

* Adding more construction parameters
* Using real-world construction datasets
* Improving model accuracy
* Adding regional material price variations
* Adding labour cost estimation
* Providing detailed material-wise cost breakdowns
* Adding foundation and structural cost estimation
* Adding graphical visualization of predicted quantities
* Adding downloadable estimation reports

