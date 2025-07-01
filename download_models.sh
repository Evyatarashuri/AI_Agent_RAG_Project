#!/bin/sh

ollama serve &

sleep 5

MODEL_DIR="/root/.ollama/models"

download_model() {
  MODEL_NAME=$1
  if [ ! -d "${MODEL_DIR}/${MODEL_NAME}" ]; then
    echo "Downloading model ${MODEL_NAME}..."
    ollama pull "${MODEL_NAME}"
  else
    echo "Model ${MODEL_NAME} already exists, skipping download."
  fi
}

download_model "llama2-7b"
download_model "nomic-embed-text"

wait
