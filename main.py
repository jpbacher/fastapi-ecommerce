from fastapi import FastAPI, status, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from pydantic import BaseModel
from typing import Optional


class Customer(BaseModel):
    customer_id: str
    country: str


class URLLink(BaseModel):
    url: str


class Invoice(BaseModel):
    invoice_no: str
    invoice_date: str
    customer: Optional(URLLink) = None









