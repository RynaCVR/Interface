
import os
import time


def _kill_gpid(gpid):
    try:
        os.killpg(gpid, 9)
        time.sleep(1)
        return 12001
    except:
        return 12002


def my_main(gpid):
    return_code = _kill_gpid(gpid)
    return return_code
