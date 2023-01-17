"""DJ Query Service Example API"""

from fastapi import FastAPI
from pydantic import BaseModel, AnyHttpUrl
import uvicorn
from enum import Enum

from typing import Any, Tuple, Optional, List

app = FastAPI()

Row = Tuple[Any, ...]


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


class QueryState(str, Enum):
    UNKNOWN = "UNKNOWN"
    ACCEPTED = "ACCEPTED"
    SCHEDULED = "SCHEDULED"
    RUNNING = "RUNNING"
    FINISHED = "FINISHED"
    CANCELED = "CANCELED"
    FAILED = "FAILED"


class BaseQuery(BaseModel):
    engine: str


class QueryCreate(BaseQuery):
    submitted_query: str


class ColumnMetadata(BaseModel):
    name: str
    type: ColumnType


class StatementResults(BaseModel):
    sql: str
    columns: List[ColumnMetadata]
    rows: List[Row]
    row_count: int = 0


class QueryResults(BaseModel):
    __root__: List[StatementResults]


class QueryWithResults(BaseModel):
    id: str
    submitted_query: str
    executed_query: Optional[str] = None
    scheduled: Optional[int] = None
    started: Optional[int] = None
    finished: Optional[int] = None
    state: QueryState = QueryState.UNKNOWN
    progress: float = 0.0
    results: QueryResults
    next: Optional[AnyHttpUrl] = None
    previous: Optional[AnyHttpUrl] = None
    errors: List[str]


@app.get("/queries/{query_id}/", response_model=QueryWithResults)
def read_query(
    query_id: str,
    limit: int = 0,
    offset: int = 0,
) -> QueryWithResults:
    # look up query by ID
    return QueryWithResults()


@app.post("/queries/", status_code=200, response_model=QueryWithResults)
def submit_query(
    data: QueryCreate,
) -> QueryWithResults:
    # submit query
    return QueryWithResults()


def main(args=None):
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8002,
    )


if __name__ == "__main__":
    main()
