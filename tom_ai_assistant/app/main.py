from fastapi import FastAPI
from app.api.routes import chat
import uvicorn

app = FastAPI(
    title="Tom AI Assistant",
    description="AI assistant for cherry tomato cultivation",
    version="1.0.0"
)

# Include routers
app.include_router(chat.router, prefix="/api", tags=["chat"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 