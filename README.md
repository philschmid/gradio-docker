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

1. clone space 
```bash
git lfs install
git clone https://huggingface.co/philschmid/space-naver-donut-cord
```

2. Add `server_name="0.0.0.0"` to launch command in `app.py`

3. run container and install packages
```bash
docker run -ti -v $(pwd)/space-naver-donut-cord:/repository -p 7860:7860 --entrypoint /bin/bash gradio-api:latest
```
```bash
pip install -r requirements.txt
```

4. run gradio app
```bash
python3 app.py
```

5. request

```bash
curl 'http://127.0.0.1:7860/api/predict/' \
  -H 'Content-Type: application/json' \
  --data-raw '{"data":["data:image/png;base64]}'

## Advanced: Deploy Gradio as Lambda Function

TODO:

