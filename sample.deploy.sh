gcloud builds submit \
  --tag gcr.io/$GOOGLE_CLOUD_PROJECT/flask-mount

gcloud run deploy flask-mount \
    --image gcr.io/$GOOGLE_CLOUD_PROJECT/flask-mount \
    --execution-environment gen2 \
    --allow-unauthenticated \
    --update-env-vars BUCKET=bucket_name