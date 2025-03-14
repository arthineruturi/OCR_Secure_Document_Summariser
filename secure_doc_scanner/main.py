from fastapi import FastAPI
from api.routes import router

app = FastAPI(title="Secure Document Scanner API")

# Register the routes
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
