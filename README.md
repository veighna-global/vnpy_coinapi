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

在vn.py中使用CoinAPI时，需要在全局配置中填写以下字段信息：

|名称|含义|必填|举例|
|---------|----|---|---|
|datafeed.name|名称|是|coinapi|
|datafeed.username|用户名|否|key|
|datafeed.password|密码|是|1131329-896E-4FD2-9F-85DF1E8|
