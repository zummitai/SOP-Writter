from main import api
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from http import HTTPStatus
import uvicorn

# Development use
app = FastAPI( title="SOP Letter Writting",
    description="This is the basic of SOP Writing",
    version="0.0.1",)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Build the BaseModel Structure for Parameters
class GetDetails(BaseModel):
    Univeristy_Name:str
    Field_Name:str
    Experience:str
    Univeristy_level:str

# ENDPOINT for our Function
@app.post('/input_param')
def details(str:GetDetails):
    response = api(str.Univeristy_Name, str.Field_Name, str.Experience, str.Univeristy_level)
    print(response)
    return {"result":response}

# Uvicorn Server Structure to run the API
if __name__ == '__main__':
    uvicorn.run("app:app",reload=True)