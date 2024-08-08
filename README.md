# banking-credit-risk-model
Credit Risk Prediction
Overview
This project provides a Streamlit web application to predict credit risk based on user input. The model used for prediction is a pre-trained Support Vector Machine (SVM) with a linear kernel.

Files
app.py: Streamlit application script.
credit_customers (DS).csv: Dataset used for model training.
SVM_LINEAR_BEST_MODEL.pkl: Pre-trained model file.
requirements.txt: List of required Python packages.
README.md: This documentation file.
How to Use the Application
Install Dependencies:
Make sure you have all required Python packages installed. You can install them using:

bash
Copy code
pip install -r requirements.txt
Run the Application:
Execute the Streamlit app by running the following command in your terminal:

bash
Copy code
streamlit run app.py
Access the Application:
Open your web browser and go to http://localhost:8502 to access the application.

Input Parameters:

Credit History: Select from the provided options.
Savings Status: Select from the provided options.
Job: Select from the provided options.
Get Prediction:
After selecting the input parameters, click the "Predict" button to get the prediction result. The application will display whether the credit risk is classified as 'Good' or 'Bad'.

View Model Metrics:
The application also shows the confusion matrix and classification report for the best model based on the test data.

Notes
Ensure the SVM_LINEAR_BEST_MODEL.pkl file is in the same directory as app.py for the application to work correctly.
If you encounter issues, verify that all dependencies are correctly installed and the dataset file is present.
Contact
For any questions or issues, please contact support@skillforge.in.