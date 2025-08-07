from fastapi import FastAPI
from api.routers.text2image import Text2Image
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI(title="Text to Images API", version="1.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(Text2Image)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
