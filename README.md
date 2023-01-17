# Temp Example Repo

Make sure pydantic, fastapi, and uvicorn are installed.

Start the Materialization Service (http://localhost:8001)
```py
python3 djms.py
```

Start the Query Service (http://localhost:8002)
```py
python3 djqs.py
```

Start the Reflection Service (http://localhost:8003)
```py
python3 djrs.py
```

Download the OpenAPI specs
```sh
curl -o openapi.djms.json http://localhost:8001/openapi.json
curl -o openapi.djqs.json http://localhost:8002/openapi.json
curl -o openapi.djrs.json http://localhost:8003/openapi.json
```
