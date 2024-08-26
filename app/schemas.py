from typing import List
from pydantic import BaseModel


class UserListResponse(BaseModel):
    data: List[str]


class UserInfoData(BaseModel):
    customer_id: str
    phone_number: str
    code: str
    banks: List[str]


class UserInfoResponse(BaseModel):
    data: UserInfoData


class TransactionData(BaseModel):
    date: str
    type: str
    amount: int


class UserTransactionData(BaseModel):
    transactions: List[TransactionData]


class UserTransactionResponse(BaseModel):
    data: UserTransactionData