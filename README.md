# vn.py框架的CoinAPI数据服务接口

<p align="center">
  <img src ="https://vnpy.oss-cn-shanghai.aliyuncs.com/vnpy-logo.png"/>
</p>

<p align="center">
    <img src ="https://img.shields.io/badge/version-1.0.0-blueviolet.svg"/>
    <img src ="https://img.shields.io/badge/platform-windows|linux|macos-yellow.svg"/>
    <img src ="https://img.shields.io/badge/python-3.7-blue.svg"/>
    <img src ="https://img.shields.io/github/license/vnpy/vnpy.svg?color=orange"/>
</p>

## 说明

基于CoinAPI开发，支持以下数字货币的K线数据：

* BITMEX
* OKEX
* HUOBI
* BITFINEX
* BINANCE
* BYBIT
* COINBASE
* DERIBIT
* GATEIO
* BITSTAMP
* FTX


注意：需要使用相应的数据服务权限，可以通过[该页面](https://www.coinapi.io)注册使用。


## 安装

安装需要基于2.6.0版本以上的[VN Studio](https://www.vnpy.com)。

直接使用pip命令：

```
pip install vnpy_coinapi
```


或者下载解压后在cmd中运行：

```
python setup.py install
```

## 使用

在VN Trader中配置时，需要填写以下字段信息：

| 字段名            | 值 |
|---------           |---- |
|datafeed.username   | API KEY|
|datafeed.password   | API KEY|
