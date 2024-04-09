import os

from core.make_expert_01 import make_expert_01
from core.make_expert_02 import make_expert_02
from core.make_expert_03 import make_expert_03
from core.make_expert_04 import make_expert_04
from core.make_expert_05 import make_expert_05
from core.make_parent_01 import make_parent_01
from core.make_parent_02 import make_parent_02
from core.make_parent_03 import make_parent_03
from core.make_parent_04 import make_parent_04
from core.make_parent_05 import make_parent_05
from core.make_parent_06 import make_parent_06
from core.make_parent_07 import make_parent_07
from core.make_parent_08 import make_parent_08
from core.make_parent_09 import make_parent_09

from util.exception_handler import exception_handler


@exception_handler
def make_expert_report():
    base_url = "http://127.0.0.1:8888/"

    options = {
        "page-width": "25.83in",
        "page-height": "36.54in",
        "margin-top": "0in",
        "margin-right": "0in",
        "margin-bottom": "0in",
        "margin-left": "0in",
        "encoding": "UTF-8",
        "custom-header": [
            ("Accept-Encoding", "gzip")
        ],
        "no-outline": None,
        "disable-smart-shrinking": True
    }

    report_path = os.path.join("report_tmp", "")
    # img_path = os.path.join("..", "static", "assets", "images", "")

    make_expert_01(base_url, options, report_path)
    make_expert_02(base_url, options, report_path)
    make_expert_03(base_url, options, report_path)
    make_expert_04(base_url, options, report_path)
    make_expert_05(base_url, options, report_path)
    make_parent_01(base_url, options, report_path)
    make_parent_02(base_url, options, report_path)
    make_parent_03(base_url, options, report_path)
    make_parent_04(base_url, options, report_path)
    make_parent_05(base_url, options, report_path)
    make_parent_06(base_url, options, report_path)
    make_parent_07(base_url, options, report_path)
    make_parent_08(base_url, options, report_path)
    make_parent_09(base_url, options, report_path)


if __name__ == "__main__":
    make_expert_report()
