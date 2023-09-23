#!/usr/bin/env python
from pypresence import Presence

RPC = Presence("1081997908985008138")
RPC.connect()

RPC.clear()

RPC.update(state = "skbidi dom dom dom yes yes yes")
