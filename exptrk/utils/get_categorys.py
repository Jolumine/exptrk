# Copyright 2023 by Leonard Becker
# All rights reserved.
# This file is part of the exptrk python project,
# and is released under the "MIT License Agreement". Please see the LICENSE
# file that should have been included as part of this package.

from exptrk.utils.read_index import read_index

import json 


def get_categorys() -> list[str]: 
    return json.load(open(read_index("user"), "r"))["Categorys"]