import requests
import pdfkit
from util.exception_handler import exception_handler


@exception_handler
def make_parent_01(base_url, options, path):
    data = {
        "header": "parent_01",
        "institution": "심리상담센터",
        "date": "23-08-05",
        "name": "⃝⃝⃝",
        "age": "만 00세",
        "gender": "여"
    }


    _ = requests.post(f"{base_url}submit_data", json=data)

    base_name = "parent_01"
    pdfkit.from_url(f"{base_url}{base_name}", f"{path}{base_name}.pdf",
                    options=options)


if __name__ == "__main__":
    print("This module is not intended to be run directly.")