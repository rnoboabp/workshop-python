import pydantic
from fastapi import FastAPI
from fastapi.params import Query
from starlette import status

from utils import statics_log, filter_log

app = FastAPI(
    title="Workshop API",
    version="1.0.0",
    description="Api doc",
    docs_url="/docs"
)


@app.get("/")
def read_root():
    print("revisiones")
    return {"Hello": "World"}


# SCHEMA
class ResponseDto(pydantic.BaseModel):
    category: str
    severity: int


responses_log = {
    # status.HTTP_404_NOT_FOUND, {"model": HTTPException},
    # status.HTTP_200_OK, {"model": ResponseDto}
}


@app.get("/logs/summary", status_code=status.HTTP_200_OK, description="Resumen total mensaje de logs.")
def get_summary_log():
    """
    # Operacion que filtra logs
    :return:
    """
    result = statics_log(file_path="resources/log.log")
    return result


from pydantic import BaseModel


class RequestDto(BaseModel):
    name: str
    description: str

    class Config:
        schema_extra = {
            "example": {
                "name": "Roberto",
                "description": "Team Python"
            }
        }


class ResponseBDto(BaseModel):
    message: str


@app.get("/logs/{type}")
def get_filter_log(type: str, category: str = Query(..., description="Filtro por categoria")):
    """

    :return:
    """
    response = filter_log(path="resources/log.log", request={"category": category})
    return response


@app.post("/demo", status_code=status.HTTP_201_CREATED, response_model=ResponseBDto)
def test_post(request_in: RequestDto):
    return ResponseBDto(message=f"Este es un mensaje {request_in.name}")
