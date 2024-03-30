import requests
import pdfkit
from util.exception_handler import exception_handler
from datetime import date


@exception_handler
def make_expert_05(base_url, options, path):
    data = {
        "header": "expert_05",
        "footer_left": date.today().strftime("%Y.%m.%d"),
        "curriculum1":{
            "lesson1":{
                "name": "색깔 기억하기",
                "level": 1,
                "image": "remember_colors.png"
            },
            "lesson2":{
                "name": "동물소리 맞히기",
                "level": 2,
                "image": "guess_animal_sounds.png"
            },
            "lesson3":{
                "name": "과녘 맞추기",
                "level": 1,
                "image": "hit_target.png"
            }
        },
        "curriculum2":{
            "lesson1":{
                "name": "마법방울숲",
                "level": 2,
                "image": "magic_forest.png"
            },
            "lesson2":{
                "name": "보물창고",
                "level": 1,
                "image": "treasure.png"
            },
            "lesson3":{
                "name": "두더지 잡기",
                "level": 1,
                "image": "hit_mouse.png"
            }
        },
        "curriculum3":{
            "lesson1":{
                "name": "과녘 맞추기",
                "level": 3,
                "image": "hit_target.png"
            },
            "lesson2":{
                "name": "색깔 기억하기",
                "level": 2,
                "image": "remember_colors.png"
            },
            "lesson3":{
                "name": "마법방울숲",
                "level": 1,
                "image": "magic_forest.png"
            }
        }
    }

    _ = requests.post(f"{base_url}submit_data", json=data)

    base_name = "expert_05"
    pdfkit.from_url(f"{base_url}{base_name}", f"{path}{base_name}.pdf",
                    options=options)


if __name__ == "__main__":
    print("This module is not intended to be run directly.")
