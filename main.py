"""importing uvicorn """
import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv
from scripts.core.services.billing_service import item_router

app = FastAPI()

app.include_router(item_router)

if __name__ == "__main__":
    load_dotenv()
    uvicorn.run(app="main:app", port=8180, reload=True)
