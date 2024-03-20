"""Automating futures trading."""
import os, time, ta, pandas as pd
from dotenv import load_dotenv
from binance.um_futures import UMFutures
from binance.error import ClientError

load_dotenv()

API_KEY = os.getenv('B_API')
SECRET_KEY = os.getenv('SECRET')

client = UMFutures(key=API_KEY, secret=SECRET_KEY)

# set config
tp = 0.01 # close market at 1% profit
sl = 0.01 # close market at 1% loss
volume = 50
leverage = 10
type = 'ISOLATED'

def get_balance_usdt():
    """Balance of the futures account."""
    try:
        response = client.balance(recvWindow=6000)
        print(response)
    except ClientError as error:
        print(
            "Found error. status: {}, error code: {}, error message: {}".format(
                error.status_code, error.error_code, error.error_message
            )
        )

get_balance_usdt()