
## Disaster Tweet Sentiment Analysis

### Overview
This project involves creating a classification model to predict the sentiment of disaster-related tweets. The goal is to classify tweets as either positive (1) or negative (0). The project includes a data science pipeline for preprocessing and modeling, and a web application for users to interact with the model.

### Files
- `data_science_pipeline.py`: Script for data preprocessing, model training, and evaluation.
- `disaster_tweets.csv`: Dataset used for model training.
- `trained_model.pkl`: Serialized model file.
- `app.py`: Web application script.
- `requirements.txt`: List of required Python packages.
- `README.md`: This documentation file.

## How to Setup

1. **Clone the Repository**

   Clone the repository to your local machine:

   ```bash
   git clone <your-repository-link>
   ```

2. **Navigate to the Project Directory**

   ```bash
   cd disaster-tweet-sentiment-analysis
   ```

3. **Install Dependencies**

   Ensure you have all required Python packages installed. You can install them using:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Data Science Pipeline**

   Execute the data science pipeline script to preprocess the data, train the model, and save the trained model:

   ```bash
   python data_science_pipeline.py
   ```

5. **Run the Application**

   Start the web application by running the following command:

   ```bash
   streamlit run app.py
   ```

6. **Access the Application**

   Open your web browser and go to [http://localhost:8501](http://localhost:8501) to access the application.

7. **Input Parameters**

   - **Tweet Text**: Enter the disaster-related tweet for sentiment analysis.

8. **Get Prediction**

   After entering the tweet text, click the "Predict" button to get the sentiment prediction. The application will display whether the sentiment is classified as 'Positive' or 'Negative'.

9. **View Model Metrics**

   The application also displays metrics including the confusion matrix and classification report for the best model based on the test data.

### Notes

- Ensure the `trained_model.pkl` file is in the same directory as `app.py` for the application to function correctly.
- If you encounter issues, verify that all dependencies are correctly installed and the dataset file is present.

### Contact

For any questions or issues, please contact [support@skillforge.in](mailto:support@skillforge.in).

---

Feel free to adjust any details according to your project specifics or personal preferences.
