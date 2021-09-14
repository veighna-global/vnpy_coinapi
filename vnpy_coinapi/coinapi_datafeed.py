from datetime import datetime
from typing import Optional, List
import requests
import pytz
import json


from vnpy.trader.datafeed import BaseDatafeed
from vnpy.trader.setting import SETTINGS
from vnpy.trader.constant import Interval, Exchange
from vnpy.trader.object import BarData, TickData, HistoryRequest

INTERVAL_VT2CA = {
    Interval.MINUTE: "1MIN",
    Interval.HOUR: "1HRS",
    Interval.DAILY: "1DAY",
    Interval.TICK: 0
}

CHINA_TZ = pytz.timezone("Asia/Shanghai")
china_list = ["OKEX", "HUOBI", "BINANCE", "BYBIT", "DERIBIT", "FTX", "GATEIO"]
UTC_TZ = pytz.utc
utc_list = ["BITMEX", "BITFINEX", "COINBASE", "BITSTAMP"]


def to_ca_symbol(symbol, exchange):
    """将交易所代码转换为CoinAPI代码"""
    return f"{exchange.value}_{symbol}".upper()


class CoinapiDatafeed(BaseDatafeed):
    """CoinAPI数据服务接口"""
    def __init__(self):
        """"""
        self.res_api = "https://rest.coinapi.io"
        self.username: str = SETTINGS["datafeed.username"]
        self.password: str = SETTINGS["datafeed.password"]

    def query_bar_history(self, req: HistoryRequest) -> Optional[List[BarData]]:
        """查询k线数据"""
        symbol = req.symbol
        exchange = req.exchange
        interval = req.interval
        start = req.start
        end = req.end

        symbol_id = to_ca_symbol(symbol, exchange)
        period_id = INTERVAL_VT2CA[interval]
        time_start = datetime.strftime(start, "%Y-%m-%dT%H:%M:%S")
        time_end = datetime.strftime(end, "%Y-%m-%dT%H:%M:%S")

        tq_interval = INTERVAL_VT2CA.get(interval)
        if not tq_interval:
            return None

        url = self.res_api + f"/v1/ohlcv/{symbol_id}/history?"
        params = {
            "period_id": period_id,
            "time_start": time_start,
            "time_end": time_end
        }
        headers = {'X-CoinAPI-Key': self.password}
        response = requests.request(
            method="GET",
            url=url,
            params=params,
            headers=headers
        )

        if response.status_code != 200:
            return None

        text = json.loads(response.text)
        data: List[BarData] = []
        for i in text:
            dt = datetime.strptime(i["time_period_start"], "%Y-%m-%dT%H:%M:%S.%f0Z")
            if exchange.value in china_list:
                dt = CHINA_TZ.localize(dt)
            else:
                dt = UTC_TZ.localize(dt)
            bar = BarData(
                symbol=symbol,
                exchange=exchange,
                interval=interval,
                datetime=dt,
                open_price=i["price_open"],
                high_price=i["price_high"],
                low_price=i["price_low"],
                close_price=i["price_close"],
                volume=i["volume_traded"],
                gateway_name="CA",
            )
            data.append(bar)

        return data

    def query_tick_history(self, req: HistoryRequest) -> Optional[List[TickData]]:
        """"""
