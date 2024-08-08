import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report

# Define a function to load and preprocess data
def load_data():
    df = pd.read_csv('credit_customers (DS).csv')
    le = LabelEncoder()
    categorical_cols = [
        'checking_status', 'credit_history', 'savings_status', 'employment', 
        'personal_status', 'other_parties', 'property_magnitude', 'other_payment_plans', 
        'housing', 'job', 'own_telephone', 'foreign_worker'
    ]
    for col in categorical_cols:
        df[col] = le.fit_transform(df[col])
    df = pd.get_dummies(df, columns=['purpose'])
    return df

# Load and preprocess data
df = load_data()

# Define a function to load the trained model
@st.cache_data
def load_model():
    return joblib.load('SVM_LINEAR_BEST_MODEL.pkl')

# Load the model
model = load_model()

# Define feature columns
feature_cols = ['credit_history', 'savings_status', 'job']

# Streamlit app layout
st.title("Credit Risk Prediction")

# User input section
st.sidebar.header("Input Parameters")
credit_history = st.sidebar.selectbox('Credit History', options=df['credit_history'].unique())
savings_status = st.sidebar.selectbox('Savings Status', options=df['savings_status'].unique())
job = st.sidebar.selectbox('Job', options=df['job'].unique())

# Create input data for prediction
input_data = pd.DataFrame({
    'credit_history': [credit_history],
    'savings_status': [savings_status],
    'job': [job]
})

# Preprocess input data to match training data
input_data = load_data().drop('class', axis=1).iloc[0].values.reshape(1, -1)

# Predict with the loaded model
if st.button('Predict'):
    prediction = model.predict(input_data)
    st.subheader("Prediction Result")
    st.write(f"Prediction: {'Good' if prediction[0] == 1 else 'Bad'}")

    # Display model metrics (assuming you want to show metrics for the best model only)
    y_test = load_data()['class'][:len(input_data)]  # Example, adjust as needed
    st.write("Confusion Matrix:")
    st.write(confusion_matrix(y_test, model.predict(input_data)))
    st.write("Classification Report:")
    st.write(classification_report(y_test, model.predict(input_data)))
