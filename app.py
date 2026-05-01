import re
import subprocess
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from lessons import LESSONS

BASE = Path(__file__).parent
app = FastAPI()


@app.get("/api/lessons")
def get_lessons():
    return LESSONS


class RunRequest(BaseModel):
    code: str


@app.post("/api/run")
def run_code(req: RunRequest):
    try:
        result = subprocess.run(
            ["python3", "-c", req.code],
            capture_output=True,
            text=True,
            timeout=10,
        )
        stdout = _clean(result.stdout)
        stderr = _clean(result.stderr)
    except subprocess.TimeoutExpired:
        stdout = ""
        stderr = "Error: code timed out after 10 seconds"
    return {"stdout": stdout, "stderr": stderr}


def _clean(s: str) -> str:
    s = re.sub(r"\x1b\[[0-9;]*m", "", s)
    return s[:10000]


app.mount("/static", StaticFiles(directory=BASE / "static"), name="static")


@app.get("/{full_path:path}")
def serve_frontend(full_path: str):
    return FileResponse(BASE / "static" / "index.html")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
