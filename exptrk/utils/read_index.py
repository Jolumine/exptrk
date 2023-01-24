# Copyright 2023 by Leonard Becker
# All rights reserved.
# This file is part of the exptrk python project,
# and is released under the "MIT License Agreement". Please see the LICENSE
# file that should have been included as part of this package.

import json 
import os 


def read_index(index:str) -> str: 
    return json.load(open(os.path.join(os.getcwd(), "index.json"), "r"))[index]
        