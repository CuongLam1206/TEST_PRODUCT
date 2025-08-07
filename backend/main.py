from fastapi import FastAPI
from api.routers.text2image import Text2Image

app = FastAPI(title="Text to Images API", version="1.0.0")

app.include_router(Text2Image)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
