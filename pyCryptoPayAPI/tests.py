import inspect, datetime
import asyncio
from time import sleep
try:
    from pyCryptoPayAPI import pyCryptoPayAPI, pyCryptoPayException
except:
    from api import pyCryptoPayAPI, pyCryptoPayException

test_api_token = "52586:AA2DKQyUAnZFELNOihEqjlfact0XsxoUmGy"

async def run_and_print(f):
    try:
        sleep(1)
        print()
        print(inspect.getsourcelines(f)[0][0].strip())
        res = await f()
        print(res)
        return res
    except pyCryptoPayException as pe:
        if pe.code in [-2]:
            print("API call failed. Code: {}, Message: {}".format(pe.code, pe.message))
        else:
            raise pe
    except Exception as e:
        raise e
    return None

async def test_api_functions():
    client = pyCryptoPayAPI(api_token=test_api_token, print_errors=True)
    await run_and_print(lambda: client.get_me())
    await run_and_print(lambda: client.get_balance())
    await run_and_print(lambda: client.get_exchange_rates())
    await run_and_print(lambda: client.get_currencies())
    await run_and_print(lambda: client.get_invoices(
        "TON",
        status="active",
        offset=0,
        count=10
    ))
    await run_and_print(lambda: client.create_invoice(
        1,
        "TON",
        description="Test at {}".format(datetime.datetime.now()),
        hidden_message="Hidden in test",
        paid_btn_name="viewItem",
        paid_btn_url="https://help.crypt.bot/crypto-pay-api",
        payload="Payload in test",
        allow_comments=True,
        allow_anonymous=True,
        expires_in=None
    ))
    await run_and_print(lambda: client.create_invoice(
        1,
        description="Test at {}".format(datetime.datetime.now()),
        hidden_message="Hidden in test",
        paid_btn_name="viewItem",
        paid_btn_url="https://help.crypt.bot/crypto-pay-api",
        payload="Payload in test",
        allow_comments=True,
        allow_anonymous=True,
        expires_in=None,
        currency_type="fiat",
        fiat="BTC"
    ))

asyncio.run(test_api_functions())
