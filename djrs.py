"""DJ Reflection Service Example API"""

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from enum import Enum

from typing import List

from enum import Enum

app = FastAPI()


class ColumnType(str, Enum):
    BYTES = "BYTES"
    STR = "STR"
    FLOAT = "FLOAT"
    INT = "INT"
    DECIMAL = "DECIMAL"
    BOOL = "BOOL"
    DATETIME = "DATETIME"
    DATE = "DATE"
    TIME = "TIME"
    TIMEDELTA = "TIMEDELTA"
    LIST = "LIST"
    DICT = "DICT"


class ReflectionRequest(BaseModel):
    engine: str
    catalog: str
    schema_: str
    table: str


class Column(BaseModel):
    name: str
    type: ColumnType


class TableSchema(BaseModel):
    __root__: List[Column]


@app.post(
    "/reflection/",
    status_code=200,
    response_model=TableSchema,
)
def get_table_schema(data: ReflectionRequest) -> TableSchema:
    # lookup table schema
    return [
        Column(**{"name": "foo", "type": "STR"}),
        Column(**{"name": "bar", "type": "INT"}),
        Column(**{"name": "baz", "type": "FLOAT"}),
    ]


def main(args=None):
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8003,
    )


if __name__ == "__main__":
    main()
