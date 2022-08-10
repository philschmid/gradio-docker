# Simple Gradio Docker example

This repository contains a simple [gradio] docker example on showing how to use the API of [gradio](https://gradio.app/) with in a docker container. The Dockerfile is inspired by the [Hugging Face Container](https://github.com/philschmid/huggingface-container) and might be migrated their in the future.

## Get Started

1. build docker container
```bash
docker build -t gradio-api:latest -f docker/Dockerfile.cpu .
```

2. run docker container
```bash
docker run -ti -v $(pwd)/examples/hello_world.py:/repository/app.py -p 7860:7860 gradio-api:latest
```

3. send request

```bash
curl -X POST \
  --url http://localhost:7860/api/predict \
  -H 'Content-Type: application/json' \
  -d '{"data":["test"]}' 
```

## Advanced: Create a Container from a HF Space

TODO:

## Advanced: Deploy Gradio as Lambda Function

TODO: