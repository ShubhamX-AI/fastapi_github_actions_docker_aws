from fastapi import FastAPI
from fastapi.responses import JSONResponse
from api_test import test_api


# Create an instance of FastAPI
app = FastAPI()

# Define a route
@app.get("/")
def read_root():
    return {"The owner is Shubham Halder"}


@app.post("/api_call_test")
def test_api_call(message: str):
    
    try:
        # Call the Gemini API
        response = test_api(message)
        return JSONResponse(content={"response": response}, status_code=200)
    
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)