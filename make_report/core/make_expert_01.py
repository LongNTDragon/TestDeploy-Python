import requests
import pdfkit
from util.exception_handler import exception_handler


@exception_handler
def make_expert_01(base_url, options, path):
    data = {
        "header": "expert_01",
        "institution": "산학협력센터",
        "date": "24-02-15",
        "name": "정신기",
        "age": "만 30세",
        "gender": "남"
    }

    _ = requests.post(f"{base_url}submit_data", json=data)

    base_name = "expert_01"
    pdfkit.from_url(f"{base_url}{base_name}", f"{path}{base_name}.pdf",
                    options=options)


if __name__ == "__main__":
    print("This module is not intended to be run directly.")
