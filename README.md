# binanceus-python
A lightweight Python wrapper for the binance.us public API. 

Uses [binance-connector-python](https://github.com/binance/binance-connector-python) for API connectivity.

I am in no way affiliated with Binance or Binance US. Use this at your own risk.

## Quick Start
Clone the repository to your target directory.

Here's some example code to get started with:

```python
from websocket_bs.client import BsWebsocketClient

# start real-time ticker stream for symbol BTCUSD
symbol = 'BTCUSD'

ws = BsWebsocketClient()
ws.subscribe(symbol)
ws.start()

# print live ticker feed
while True:
    book_top = ws.book_top(symbol)
    bid = book_top[0]
    bid_qty = book_top[1]
    ask = book_top[2]
    ask_qty = book_top[3]
    print(f'BTC/USD SPOT orderbook_top: ({bid:0.4f}, {bid_qty})  ({ask:0.4f}, {ask_qty})')
```
