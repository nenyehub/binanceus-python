from binance.spot import Spot
from typing import Optional

class BsClient(Spot):
    def __init__(self,
                 api_key: Optional[str] = None,
                 api_secret: Optional[str] = None,
                 base_url: Optional[str] = "https://api.binance.us"):
        super().__init__(base_url=base_url, key=api_key, secret=api_secret)