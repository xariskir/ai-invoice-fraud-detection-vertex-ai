# System Flow Description

This project follows a production-style ML pipeline:

1. Invoice data is uploaded to Google Cloud Storage.
2. Vertex AI Custom Training job trains an XGBoost fraud detection model.
3. The trained model is registered in Vertex AI Model Registry.
4. The model is deployed to a Vertex AI Endpoint.
5. A Cloud Run API sends prediction requests to the endpoint.
6. Prediction results are stored in BigQuery.
7. Looker Studio dashboard visualizes fraud risk metrics in real time.

This architecture enables scalable fraud detection and business monitoring.
