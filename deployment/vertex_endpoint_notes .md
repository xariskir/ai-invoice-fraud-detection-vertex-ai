# Vertex AI Endpoint Deployment

## Deployment Steps

1. Upload trained model artifact to Cloud Storage.
2. Register model in Vertex AI Model Registry.
3. Deploy model to Vertex AI Endpoint.
4. Assign machine type (n1-standard-4).
5. Enable online predictions.

## Prediction Flow

Client Request → Cloud Run API → Vertex Endpoint → Response Returned

## Monitoring

- Endpoint traffic monitored via Vertex AI console
- Prediction logs stored in BigQuery

## Scaling

Automatic scaling enabled to handle prediction traffic spikes.
