# A test repo for docker-compose automated building for an API service

## Docker compose

Create a stack in portainer with docker-compose

```yaml
version: "3"
services:
    app:
        image: fastapi-test
        build: https://github.com/JonneSaloranta/fastapi-docker-test.git
        container_name: fastapi-test
        command: uvicorn main:app --host 0.0.0.0 --port 8000
        ports:
            - 8000:8000
        restart: unless-stopped
```
