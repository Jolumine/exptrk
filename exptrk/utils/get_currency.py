# Copyright 2023 by Leonard Becker
# All rights reserved.
# This file is part of the exptrk python project,
# and is released under the "MIT License Agreement". Please see the LICENSE
# file that should have been included as part of this package.

import json 

from exptrk.utils.read_index import read_index

def get_currency() -> str: 
    return (json.load(open(read_index("settings"), "r"))["currency"].split("/")[0], json.load(open(read_index("settings"), "r"))["currency"].split("/")[1])