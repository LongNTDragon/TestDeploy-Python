import requests
import pdfkit
from util.exception_handler import exception_handler


@exception_handler
def section1_table_circle(data):
    for factor in [f"factor{x+1}" for x in range(6)]:
        value = data[factor]

        if value >= 80:
            data[f"{factor}_circle"] = ["●", "", "", ""]
        elif value >= 45:
            data[f"{factor}_circle"] = ["", "●", "", ""]
        elif value >= 35:
            data[f"{factor}_circle"] = ["", "", "●", ""]
        else:
            data[f"{factor}_circle"] = ["", "", "", "●"]


@exception_handler
def make_expert_02(base_url, options, path):
    data = {
        "header": "expert_02",
        "section1": {
            "factor1": 55,
            "factor2": 51,
            "factor3": 42,
            "factor4": 21,
            "factor5": 44,
            "factor6": 53
        },
        "section2": {
            "factor1": 1.25,
            "factor2": 0.85,
            "factor3": 1.12,
            "percentile": [82, 23, 81],     # need to modify
            "type": [1, 0, 0, 0]            # need to modify
        }
    }

    section1_table_circle(data["section1"])

    _ = requests.post(f"{base_url}submit_data", json=data)

    base_name = "expert_02"
    pdfkit.from_url(f"{base_url}{base_name}", f"{path}{base_name}.pdf",
                    options=options)


if __name__ == "__main__":
    print("This module is not intended to be run directly.")
