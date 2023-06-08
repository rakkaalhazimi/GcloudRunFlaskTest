gcloud builds submit \
  --tag gcr.io/$GOOGLE_CLOUD_PROJECT/flask-mount

gcloud run deploy filesystem-app --source . \
    --image gcr.io/$GOOGLE_CLOUD_PROJECT/flask-mount \
    --execution-environment gen2 \
    --allow-unauthenticated \
    --service-account fs-identity \
    --update-env-vars BUCKET=bucket_name