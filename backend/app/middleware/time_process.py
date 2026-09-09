import time
from logger import logger
from fastapi import FastAPI, Request

app = FastAPI()


async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    logger.info("process time: %s", round(process_time, 2))
    response.headers["X-Process-Time"] = str(process_time)
    return response
