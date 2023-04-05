from pydantic import BaseModel


class Pair(BaseModel):

    symbol: str


class CryptoPairs(BaseModel):

    symbols: list[Pair]
