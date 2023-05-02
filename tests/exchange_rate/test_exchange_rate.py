import http

import pytest
from httpx import AsyncClient

from models.exchange_rate import ExchangeRate
from tests.utils.decorator import set_db


@pytest.mark.anyio
@set_db("exchange_rate")
class TestExchangeRate:
    async def test_create_exchange_rate(self, client: AsyncClient):
        # Given: ExchangeRate data
        exchange_rate1 = ExchangeRate(
            apply_date="2022-10-04",
            apply_time="16:00:00",
            agency_id="081",
            currency="USD",
            notice_seq=1,
            cash_sell_rate=1211.840,
            cash_buy_rate=1170.160,
            tt_sell_rate=1202.600,
            tt_buy_rate=1179.400,
            trade_stan_rate=1191.000,
            pre_trade_stan_rate=1191.000,
            us_ex_rate=1.000,
            frc_sell_rate=1178.770,
            tra_buy_rate=0.000,
        )
        exchange_rate2 = ExchangeRate(
            apply_date="2022-10-04",
            apply_time="16:00:00",
            agency_id="081",
            currency="USD",
            notice_seq=2,
            cash_sell_rate=1211.840,
            cash_buy_rate=1170.160,
            tt_sell_rate=1202.600,
            tt_buy_rate=1179.400,
            trade_stan_rate=1191.000,
            pre_trade_stan_rate=1191.000,
            us_ex_rate=1.000,
            frc_sell_rate=1178.770,
            tra_buy_rate=0.000,
        )
        # When: Try to create 2 new data and then get created data
        await exchange_rate1.save()
        await exchange_rate2.save()
        response = await client.get("/exchange/rate/2022-10-04/16:00:00/081/USD")
        # Then: http response is 200, 2 new created data returned and the
        # transaction will rollback.
        assert response.status_code == http.HTTPStatus.OK
        assert len(response.json()) == 2

    async def test_rollback_executed(self, client: AsyncClient):
        # Given: transaction rollback from test_create_exchange_rate function
        # When: Try to get rollback data
        response = await client.get("/exchange/rate/2022-10-04/16:00:00/081/USD")
        # Then: https response is 200 but nothing returned.
        assert response.status_code == http.HTTPStatus.OK
        assert len(response.json()) == 0
