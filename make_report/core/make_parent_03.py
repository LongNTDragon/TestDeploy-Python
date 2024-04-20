import requests
import pdfkit
from util.exception_handler import exception_handler
from datetime import date

@exception_handler
def section1_table_circle(data):
    for factor in [f"factor{x+1}" for x in range(6)]:
        value = data[factor]
        if value >= 80:
            data[f"{factor}_circle"] = ["", "", "✔", ""]
        elif value >= 45:
            data[f"{factor}_circle"] = ["", "", "✔", ""]
        elif value >= 35:
            data[f"{factor}_circle"] = ["", "✔ ", "", ""]
        else:
            data[f"{factor}_circle"] = ["✔", "", "", ""]

@exception_handler
def make_parent_03(base_url, options, path):
    data = {
        "header": "parent_03",
        "test_date": date.today().strftime("%Y-%m-%d"),
        "name": "⃝",
        "sex": "여",
        "age": 0,
        "result":[0, 0, 1, 0],
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
        },
        "Performance_evaluation":{
            "commonly":{
                "title":"주의집중력",
                "desc":"주의집중력이 좋을수록 과제 중에 급격한 움직임을 보이지 않고, 한 위치에서 꾸준히 한 가지 과제에 몰두하는 패턴을 보입니다. 반대로 주의력집중력이 낮은 경우 몸을 좌우로 흔들거나 안절부절 못하는 모습이 많이 나타나므로, 이러한 움직임 전체를 종합한 결과를 주의집중력의 지표로 볼 수 있습니다."
            },
            "commonly1":{
                "title":"작업기억력",
                "desc":"작업기억력이 좋을수록 과거의 경험이나 학습을 통해 획득한 정보를 저장하는 능력이 뛰어나며, 예전에 경험한 비슷한 문제에 직면했을 때 빠르게 문제를 해결하는 모습을 보여줍니다. 반대로 작업기억력이 낮을 경우 일상적인 정보 혹은 주요한 일정을 잊어버리며, 정도가 심할 경우 낮은 작업수행력으로 연결되기도 합니다."
            },
            "boundary1":{
                "title":"집행기능",
                "desc":"집행기능이 좋을수록 빠르고 정확하게 외부 상황을 판단하여 목표를 달성하기 위한 계획을 수립하고 행동합니다. 반대로 집행기능이 나쁠수록 목표 · 상황에 대한 분석력이 떨어지며, 수립한 계획을 행동으로 옮기기까지 많은 시간이 소요됩니다."
            },
            "inadequate":{
                "title":"언어기능",
                "desc":"행동조절력이 좋을수록 빠르고 정확하게 외부 상황을 판단하여 자신의 행동을 컨트롤합니다. 반대로 행동조절력이 나쁠수록 자제력이 낮아지며, 소수의 방해 자극에 취약하여 반응이 늦어집니다."
            },
            "boundary2":{
                "title":"사회성",
                "desc":"사회성이 좋을수록 다른 사람과 사교적이며 협동심이 강하고 친화력이 좋아서 사회에 잘 적응합니다. 반대로 사회성이 낮은 경우 타인과 협력하고자 하는 의지가 부족하고 상대방의 입장이나 생각을 고려하지 않는 경우가 많습니다."
            },
            "commonly2":{
                "title":"충동자제력",
                "desc":"충동자제력이 좋을수록 자신의 욕구를 지연시키면서 자신의 행동을 조절할 수 있습니다. 또한 자신의 행동을 조절할 수 있기 때문에, 상대방의 입장도 고려하거나 배려하는 등 적절한 사회적 관계를 통해 원만한 교우 관계를 형성할 수 있습니다. 반대로 충동자제력이 낮을 경우, 결과를 예상하지 못한 채 불쑥 행동하는 경향을 보입니다."
            }
            }
        }
        


    section1_table_circle(data["section1"])

    _ = requests.post(f"{base_url}submit_data", json=data)

    base_name = "parent_03"
    pdfkit.from_url(f"{base_url}{base_name}", f"{path}{base_name}.pdf",
                    options=options)


if __name__ == "__main__":
    print("This module is not intended to be run directly.")
