📈 Stock Price Forecasting Pipeline  

This project implements a fully automated data pipeline that retrieves real-time market data for any NASDAQ listed stock, processes it, and generates short-term price predictions using a regression model.  

The main objective is to demonstrate how to build a complete, production ready pipeline that integrates live API data, preprocessing, modeling, and visualization in a seamless flow suitable for professional data science environments.

---

📌 What does this app do?  
This project retrieves financial data from the **Alpha Vantage API**, processes and transforms the latest stock information, feeds it into a machine learning model, and returns price predictions for upcoming time intervals.  

Although the included setup predicts the next 60 minutes in 5 minute intervals, the pipeline is fully adaptable to other intervals and time frames supported by the API.

The results are displayed using a clean and interactive Streamlit dashboard.

---

📁 Data source  
- **Alpha Vantage API** ([https://www.alphavantage.co/](https://www.alphavantage.co/))  
No manual intervention is needed—the pipeline pulls live data automatically.

---

🧠 How does it work?  

The app was developed using:

- Python
- Scikit-learn (for machine learning)
- Streamlit (for the web interface)
- Pandas (for data processing)
- Plotly (for dynamic charts)

The pipeline steps are:

1. Retrieve real-time stock data from Alpha Vantage.
2. Clean, sort, and preprocess the data.
3. Generate features and prepare the model input.
4. Use a regression model to predict the stock's short-term behavior.
5. Export the predictions and display them in a web interface.

---

🚀 How to run the app locally  

**Requirements:** Python 3.8+ installed on your system.

**Step 1:** Clone this repository  
```bash
git clone https://github.com/your-username/stock-prediction-pipeline.git
cd stock-prediction-pipeline
```
### Step 2: Create and activate a virtual environment (optional but recommended)

#### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install dependencies
```bash
pip install -r Requirements.txt
```

### Step 4: Run the app
```bash
streamlit run Dashboard.py
```

Your browser will open a local server showing a dynamic price forecast for the selected stock.

---

## 🧪 Example use case

After executing the notebook and launching the app, you will see:

- A table with predicted prices at selected intervals (e.g., every 5 minutes)
- A line chart visualizing the expected trend
- The app supports any NASDAQ stock symbol available through Alpha Vantage

This pipeline can be adapted to different stocks, intervals, or models with minimal changes, and is suitable for real-time forecasting scenarios.

---

## 📁 Files in this project

- `Dashboard.py`: Main Streamlit application.
- `predictions.pkl`: Contains the predicted stock prices generated by the notebook. This file is automatically created after running the full pipeline and is used by the Streamlit app to display results.
- `stock-prediction-pipeline.ipynb`: Jupyter notebook used for data exploration, model training and evaluation.
- `Requirements.txt`: List of dependencies.
- `README.md`: You’re reading it!

---

## 👨‍💻 Author

Created with care and curiosity by Agustin Gorrin.  
This project is part of my data analytics and machine learning portfolio.

---

## 📫 Contact

Feel free to connect or reach out via:

- GitHub: [github.com/gus12green](https://github.com/gus12green)
- LinkedIn: [linkedin.com/in/agustín-gorrín-santana/](https://linkedin.com/in/agustín-gorrín-santana/)

---

## ⚠️ Disclaimers

- This app is **not for commercial use** and is purely educational and demonstrative.  
  I do **not profit** in any way from its use or from the underlying dataset.

- This app runs **entirely on your local machine**. No data is collected, transmitted or stored anywhere.  
