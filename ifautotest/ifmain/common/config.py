# coding: utf-8

import copy
import time
from ifautotest.ifmain.common import common_lib


class URL_DEV:
    JJB_URL = "jjbapi.dev.julanling.com"
    DGD_URL = "dgdapi.dev.julanling.com"
    DGQ_URL = "dgqapi.dev.julanling.com"
    CDP_URL = "jcbdh5.dev.julanling.com"


class URL_PRE:
    JJB_URL = "jjbapi.pre.julanling.com"
    DGD_URL = "dgdapi.pre.julanling.com"
    DGQ_URL = "dgqapi.pre.julanling.com"
    CDP_URL = "jcbdh5.pre.julanling.com"


class URL_RES:
    JJB_URL = "jjbapi.julanling.com"
    DGD_URL = "dgdapi.julanling.com"
    DGQ_URL = "dgqapi.julanling.com"
    CDP_URL = "jcbdh5.julanling.com"

Environment = "RES"

if Environment == "PRE":
    URL = URL_PRE
elif Environment == "RES":
    URL = URL_RES
else:
    URL = URL_DEV


if __name__ == "__main__":
    import time
    for n in range(5):
        time.sleep(1)
        print(common_lib.get_common_header())
