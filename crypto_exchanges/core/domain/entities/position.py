from dataclasses import dataclass
from decimal import Decimal

from .symbol import Symbol


@dataclass
class Position:
    symbol: Symbol
    entry_price: Decimal
    size_with_sign: Decimal

    @property
    def volume_abs(self) -> Decimal:
        return abs(self.size_with_sign)
