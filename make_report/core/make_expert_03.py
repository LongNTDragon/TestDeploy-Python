import requests
import pdfkit
from util.exception_handler import exception_handler
from datetime import date


@exception_handler
def make_expert_03(base_url, options, path):
    data = {
        "header": "expert_03",
        "footer_left": date.today().strftime("%Y.%m.%d"),
        "section1":{
            "distraction_type": "주의산만 지속형",
            "z_score": 1.615,
            "variance": 1.615,
            "average": 1.315,
            "type":[1, 0, 0, 0]
        }
    }

    _ = requests.post(f"{base_url}submit_data", json=data)

    base_name = "expert_03"
    pdfkit.from_url(f"{base_url}{base_name}", f"{path}{base_name}.pdf",
                    options=options)


if __name__ == "__main__":
    print("This module is not intended to be run directly.")
