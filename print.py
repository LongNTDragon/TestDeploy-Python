import pdfkit
import PyPDF2
import requests

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

base_url = "http://127.0.0.1:8888/"

# page 1
base_name = "expert_01"

data = {
    "institution": "산학협력센터",
    "date": "24-02-15",
    "name": "정신기",
    "age": "만 30세",
    "gender": "남"
}

url = f"{base_url}{base_name}"
response = requests.post(url, json=data)

pdfkit.from_url(url, f"{base_name}.pdf", options=options)


# page 2
base_name = "expert_02"

data = {
    "section1": {
        "factor1": 55,
        "factor2": 51,
        "factor3": 42,
        "factor4": 21,
        "factor5": 44,
        "factor6": 53
    }
}

url = f"{base_url}{base_name}"
pdfkit.from_url(url, "expert_02.pdf", options=options)

# merge and save
file_handles = []

try:
    writer = PyPDF2.PdfFileWriter()

    for file_name in [f"expert_0{x+1:d}.pdf" for x in range(2)]:
        file = open(file_name, "rb")
        file_handles.append(file)

        reader = PyPDF2.PdfFileReader(file)
        writer.addPage(reader.getPage(0))

    with open("expert.pdf", "wb") as output_file:
        writer.write(output_file)

finally:
    for handle in file_handles:
        handle.close()
