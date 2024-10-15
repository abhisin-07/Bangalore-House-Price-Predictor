Bangalore House Price Prediction
Description
This project is a machine learning model designed to predict house prices in Bangalore based on various features like location, number of bedrooms, area, and more. The model is built using sklearn and pandas for data preprocessing and modeling. The web interface is developed with Flask and HTML, allowing users to input house details and receive predictions.

Features
Predicts house prices based on input features such as location, size, and number of bedrooms.
Web-based interface using Flask and HTML for easy interaction.
Implements data preprocessing techniques like normalization and feature engineering.
Uses sklearn's regression models for prediction.
Installation
Clone this repository:

git clone https://github.com/yourusername/bangalore-house-price-prediction.git
cd bangalore-house-price-prediction
Create a virtual environment and activate it:
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required dependencies:


pip install -r requirements
requirments consists of:
1.pandas
2.numpy
3.pickle
4.sklearn
5.flask


Run the Flask app:
python app.py
Open your browser and go to http://127.0.0.1:5001/ to access the web interface.

Usage
Input house details such as location, total square footage, number of bedrooms, and bathrooms in the form.
Submit the form to get the predicted house price for Bangalore.
Example:

Location: Whitefield
Square Footage: 1500
Bedrooms: 3
Bathrooms: 2
Predicted House Price: ₹ 75,00,000

Project Structure
app.py: The Flask application that handles routing and interactions.
model.py: The machine learning model (trained using sklearn) and prediction logic.
templates/index.html: HTML files for the user interface.
Cleaned.csv: preprocessed Dataset
BangaloreDataset.csv=raw data taken from Kaggle.
Data Preprocessing
The raw data is cleaned and preprocessed using pandas. Some key steps include:

Handling missing values.
OneEncoding categorical features (like location).
Standard Scaling numerical features (like area).
Model
The model is trained using scikit-learn's Ridge Regression. we haven't checked our model with  regression models such as DecisionTreeRegressor and RandomForestRegressor it may perform well with those, but ridgeRegression was chosen due to its interpretability and performance on the dataset.

Contributing
Feel free to fork this repository and submit pull requests for any improvements or bug fixes. If you have suggestions for new features, open an issue!
