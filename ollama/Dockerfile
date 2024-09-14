FROM ollama/ollama:latest

#build argument to set LLM that you want ollama to run
ARG OLLAMA_MODEL_NAME=llama3.1:8b

#ollama service runs on port 11434
EXPOSE 11434

#start the ollama service & sleep 5 seconds && after sleeping run the model
RUN ollama serve & sleep 5 && ollama run $OLLAMA_MODEL_NAME