import requests
import pdfkit
from util.exception_handler import exception_handler
from datetime import date


@exception_handler
def make_expert_04(base_url, options, path):
    data = {
        "header": "expert_04",
        "footer_left": date.today().strftime("%Y.%m.%d")
    }

    _ = requests.post(f"{base_url}submit_data", json=data)

    base_name = "expert_04"
    pdfkit.from_url(f"{base_url}{base_name}", f"{path}{base_name}.pdf",
                    options=options)


if __name__ == "__main__":
    print("This module is not intended to be run directly.")
