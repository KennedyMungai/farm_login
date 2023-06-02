"""The main file for the backend"""
from fastapi import FastAPI


app = FastAPI(title="FARM Login Backend", description="Backend for the FARM Login", version="0.1.0")

@app.get(
    "/", 
    name='Root', 
    description="The root endpoint", 
    response_model=dict[str, str]
    )
async def root() -> dict[str, str]:
    """The root endpoint for the backend

    Returns:
        dict[str, str]: A simple message to show that the app is running
    """
    return {"message": "Hello World"}