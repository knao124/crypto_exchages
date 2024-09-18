from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Fee:
    # 小数点の手数料率(%ではない)
    maker: Decimal
    # 小数点の手数料率(%ではない)
    taker: Decimal
