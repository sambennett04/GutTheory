# Ollama

- Ollama is an LLM hosting framework that exposes LLMs over REST. Read more at the [project's site](https://ollama.com/).

## Build Container

- Change the value of the build argument OLLAMA_MODEL_NAME to deploy a different LLM. 
- You can find a list of all available LLMs at the project's site linked above.

```sh

cd ./GutTheory/ollama

docker build --build-arg OLLAMA_MODEL_NAME=llama3.1:8b -t gt-ollama  .

```

## Run Container

```sh

docker run -d -v ollama:/root/.ollama --name gt-ollama-container -p 11434:11434 --env-file .env gt-ollama

```