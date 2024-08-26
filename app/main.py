import asyncio
import random

from fastapi import FastAPI, HTTPException
from starlette.status import HTTP_404_NOT_FOUND, HTTP_503_SERVICE_UNAVAILABLE

from . import data
from .schemas import (
    UserInfoResponse,
    UserListResponse,
    UserTransactionResponse,
)

app = FastAPI()


@app.get('/customers/', summary='get customers list', responses={200: {'model': UserListResponse}})
async def get_customers_list():
    return dict(data=data.users)


@app.get('/customers/{customer_id}/', summary='get customer detail', responses={200: {'model': UserInfoResponse}, 404: {}})
async def get_customers_detail(customer_id: str):
    if customer_id not in data.users_detail:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=f'{customer_id} not found')
    await asyncio.sleep(random.randint(0, 4))
    return dict(data=data.users_detail[customer_id])


@app.get(
    '/customers/{customer_id}/{bank_name}/transactions/',
    summary='get customer detail in a bank',
    responses={200: {'model': UserTransactionResponse}, 404: {}, 503: {}}
)
async def get_transactions_detail(customer_id: str, bank_name: str):
    await asyncio.sleep(random.randint(1, 10))
    if customer_id not in data.banks_details:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=f'{customer_id} not found')
    if bank_name not in data.banks_details[customer_id]:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=f'{bank_name} not found for {customer_id}')
    if random.choices([False, True], weights=[9, 1], k=1)[0]:
        raise HTTPException(status_code=HTTP_503_SERVICE_UNAVAILABLE, detail='service is not available')
    return dict(data=data.banks_details[customer_id][bank_name])
