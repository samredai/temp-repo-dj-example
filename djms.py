"""DJ Materialization Service Example API"""

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

from typing import Dict, List

app = FastAPI()


class Node(BaseModel):
    name: str
    version: int
    maxage: int


class MaterializationRequest(BaseModel):
    nodes: List[Node]


class MaterializedTables(BaseModel):
    id: str
    created_at: int
    catalog: str
    schema_: str
    table: str


class MaterializationHistory(BaseModel):
    latest: str
    schedule: str
    tables: List[MaterializedTables]


@app.post(
    "/materializations/",
    status_code=200,
    response_model=Dict[str, Dict[str, MaterializationHistory]],
)
def get_materializations(
    data: MaterializationRequest,
) -> Dict[str, Dict[str, MaterializationHistory]]:

    return {
        "a.b.c.foo": {
            "2": MaterializationHistory.parse_obj(
                {
                    "latest": "128463db-74eb-4f25-9677-bb7516f07871",
                    "schedule": "daily",
                    "tables": [
                        {
                            "id": "128463db-74eb-4f25-9677-bb7516f07871",
                            "created_at": 1673923719,
                            "catalog": "product",
                            "schema_": "djms",
                            "table": "a_b_c_foo_1_1673923719",
                        },
                        {
                            "id": "c97c4c57-dad2-4d51-a9da-0b250f675325",
                            "created_at": 1673837317,
                            "catalog": "product",
                            "schema_": "djms",
                            "table": "a_b_c_foo_1_1673837317",
                        },
                        {
                            "id": "cfbdf313-1aab-4e10-b2ae-38b00e147afe",
                            "created_at": 1673750917,
                            "catalog": "product",
                            "schema_": "djms",
                            "table": "a_b_c_foo_1_1673750917",
                        },
                    ],
                }
            ),
            "1": MaterializationHistory.parse_obj(
                {
                    "latest": "7af04de3-71de-48a3-9e28-1ffd1eb7eb9a",
                    "schedule": "daily",
                    "tables": [
                        {
                            "id": "7af04de3-71de-48a3-9e28-1ffd1eb7eb9a",
                            "created_at": 1673587508,
                            "catalog": "product",
                            "schema_": "djms",
                            "table": "a_b_c_foo_1_1673587508",
                        },
                    ],
                }
            ),
        }
    }


def main(args=None):
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8001,
    )


if __name__ == "__main__":
    main()
