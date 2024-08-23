# GCP : Big Query usages  

## Overview

This repository showcases my hands-on projects completed as part of the Google Cloud Professional Data Engineer certification. The projects demonstrate my proficiency in various GCP services, including BigQuery, Dataflow, BigQuery ML, and Vertex AI.

## Projects

### 1. Exploring a BigQuery Public Dataset

<img src="https://github.com/Sendo-A/cloud_analysis_projects/blob/main/gcp_analysis_ml_datasets/photos/bigquery_UI.png" alt="bigquery_ui" width="800">
<img src="https://github.com/Sendo-A/cloud_analysis_projects/blob/main/gcp_analysis_ml_datasets/photos/bigquery_querying.png" alt="bigquery_querying" width="800">

**Description:**  
In this project, I explored and analyzed a public dataset available in Google BigQuery. The goal was to understand the dataset's structure and gain insights through SQL queries.

**Key Highlights:**
- Querying public datasets using BigQuery
- Performing exploratory data analysis (EDA)
- Creating insightful visualizations

**Files:**
- `bigquery_exploration.sql`: SQL scripts used for querying the dataset
- `eda_report.ipynb`: Jupyter Notebook with EDA results and visualizations

### 2. Creating a Streaming Data Pipeline for a Real-Time Dashboard with Dataflow

<img src="https://github.com/Sendo-A/cloud_analysis_projects/blob/main/gcp_analysis_ml_datasets/photos/bigquery_piplane_data.png.png" alt="piplane_bigquery" width="800">


**Description:**  
This project involved setting up a streaming data pipeline using Google Dataflow to feed real-time data into a dashboard. The pipeline processes data streams and performs real-time transformations.

**Key Highlights:**
- Designing a Dataflow pipeline for real-time data processing
- Integrating with Google Cloud Pub/Sub for data ingestion
- Building a real-time dashboard to visualize streaming data

**Files:**
- `dataflow_pipeline.py`: Python script for the Dataflow pipeline
- `dashboard_config.json`: Configuration file for the real-time dashboard

### 3. Predicting Visitor Purchases with BigQuery ML


<img src="https://github.com/Sendo-A/cloud_analysis_projects/blob/main/gcp_analysis_ml_datasets/photos/big_query_ml.png" alt="ml_bigquery" width="800">


**Description:**  
In this project, I built a machine learning model using BigQuery ML to predict visitor purchases based on historical data. The project involved training and evaluating the model to generate actionable insights.

**Key Highlights:**
- Building and training a machine learning model in BigQuery ML
- Evaluating model performance and accuracy
- Generating predictions for visitor purchase behavior

**Files:**
- `bigquery_ml_model.sql`: SQL queries for training and evaluating the ML model
- `model_results_report.ipynb`: Jupyter Notebook with model evaluation results

### 4. Vertex AI Predicting Loan Risk with AutoML

<img src="https://github.com/Sendo-A/cloud_analysis_projects/blob/main/gcp_analysis_ml_datasets/photos/vertexai_model_evaluation.png" alt="vertexai" width="800">
<img src="https://github.com/Sendo-A/cloud_analysis_projects/blob/main/gcp_analysis_ml_datasets/photos/vertexai_confusion_matrix.png" alt="vertexai" width="800">
<img src="https://github.com/Sendo-A/cloud_analysis_projects/blob/main/gcp_analysis_ml_datasets/photos/vertexai_features_contribution.png" alt="vertexai" width="800">
<img src="https://github.com/Sendo-A/cloud_analysis_projects/blob/main/gcp_analysis_ml_datasets/photos/vertexai_deploying_testing.png" alt="vertexai" width="800">

**Description:**  
This project focused on using Vertex AI's AutoML capabilities to predict loan risk. The model was trained on historical loan data to assess the risk associated with new loan applications.

**Key Highlights:**
- Leveraging Vertex AI AutoML for model training
- Evaluating model performance and risk predictions
- Deploying the model for inference on new loan data

**Files:**
- `vertex_ai_automl_model.ipynb`: Jupyter Notebook detailing the AutoML model process
- `loan_risk_predictions.csv`: Sample predictions and evaluation results

## Getting Started

To explore or run the code in this repository, you will need:
- A Google Cloud Platform account
- Access to Google BigQuery, Dataflow, BigQuery ML, and Vertex AI services
- Required Python packages (e.g., `google-cloud`, `pandas`, `numpy`)

**Setup Instructions:**

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/repo_name.git
   cd gcp-certification-projects

