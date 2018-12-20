"""
Copyright  2016-2019 Maël Azimi <m.a@moul.re>

Silkaj is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Silkaj is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with Silkaj. If not, see <https://www.gnu.org/licenses/>.
"""

from datetime import datetime
from sys import exit

from silkaj.constants import G1_SYMBOL, GTEST_SYMBOL
from silkaj.blockchain_tools import BlockchainParams


def convert_time(timestamp, kind):
    ts = int(timestamp)
    date = "%Y-%m-%d"
    hour = "%H:%M"
    second = ":%S"
    if kind == "all":
        pattern = date + " " + hour + second
    elif kind == "date":
        pattern = date
    elif kind == "hour":
        pattern = hour
        if ts >= 3600:
            pattern += second
    return datetime.fromtimestamp(ts).strftime(pattern)


class CurrencySymbol(object):
    __instance = None

    def __new__(cls):
        if CurrencySymbol.__instance is None:
            CurrencySymbol.__instance = object.__new__(cls)
        return CurrencySymbol.__instance

    def __init__(self):
        currency = get_currency()
        if currency == "g1":
            self.symbol = G1_SYMBOL
        elif currency == "g1-test":
            self.symbol = GTEST_SYMBOL

    async def get_params():
        currency = await BlockchainParams().params["currency"]


def message_exit(message):
    print(message)
    exit(1)
