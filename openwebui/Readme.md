# Open WebUI

- Open WebUI is a chat interface that can be used to rapidly prototype against LLMs. Read more at the [project's site](https://docs.openwebui.com/).

## Build Container

```sh

cd ./GutTheory/openwebui

docker build -t gt-openwebui . 

```

## Run Container

```sh

docker run -d -p 3001:8080 -v open-webui:/app/backend/data --name guttheory-openwebui-container --env-file ".env" --restart always gt-openwebui

```