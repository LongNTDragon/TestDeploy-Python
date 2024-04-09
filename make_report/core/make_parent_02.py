import requests
import pdfkit
from util.exception_handler import exception_handler
from datetime import date

@exception_handler



@exception_handler
def make_parent_02(base_url, options, path):
    data = {
        "header": "parent_02",
        "test_date": date.today().strftime("%Y-%m-%d"),
        "name": "⃝",
        "sex": "여",
        "age": 0,
        
        "result":[0, 0, 1, 0],
        "HippBrainCheck":[
            "· HippBrainCheck은 VR 게임을 통해 주의력, 집중력, 사회성을 측정하는 건강기능소프트웨어입니다.",
            "· VR 미션의 다양한 상황 속에서 아동의 움직임, 반응, 음성 데이터를 수집하고, 이를 토대로 AI가 아동의 주요 행동패턴을분석해 6가지 영역별로 결과를 제시합니다.",
            "· 미국정신의학협회(APA)에서 제시한 DSM-5에 근거하여, 국내외 전문 의료진이 함께 설계한 신뢰도 높은 서비스입니다."
        ],
        "HippBrainCheck2":[
            "·  VR을 이용하여 진행되어 검사에 대한 거부감이 낮습니다. ",
            "·  아동에 대한 심층적인 이해를 할 수 있습니다. 생활에서 어떻게 적응과 부적응을 보이는지, 어떤 모습을 보일 수 있는지 알 수 있습니다. 이러한 정보는 평소 이해되지 않았던 아동의 행동을 이해할 수 있게 도와 갈등이 감소하고 정서적 지지를 촉진하여 긍정적 관계 형성에 기여할 수 있습니다. ",
            "·  일상생활에서 할 수 있는 개입 방향성에 대한 정보를 제공함으로써 발전과 개선을 위해 어떤 노력을 해야 하는지를 알 수 있습니다.",
            "·  학령기 전반(만6세~8세)에는 비교적 높은 집중력이 필요하지 않아 아동의 문제점을 알아차리기 쉽지 않습니다. HippBrainCheck을 이용하여 문제가 나타나기 전에 예방할 수 있도록 돕습니다."
        ],

        "curriculum1":{
            "lesson1":{
                "title": "공을 옮겨요",
                "desc": "튜브에 담긴 공을 정해진 통에 넣습니다. 옮기기 어려운 공을 반복적으로 옮겨 담는게임을 합니다.",
                "image": "hit_mouse.png"
            },
            "lesson2":{
                "title": "숫자를 정리해요",
                "desc": "숫자를 색깔과 순서에 맞게 차례대로 정리합니다. 처음에는 친구(캐릭터)와 함께 협동하여 정리해보고, 그 이후에는스스로 정리해봅니다.",
                "image": "hit_mouse.png"
            },
            "lesson3":{
                "title": "학교에 갈 준비를 해요",
                "desc": "방을 돌아다니며 필요한 준비물들을 찾아 모두 가방 안에 넣습니다. 일정시간 안에 책가방을 챙기는 게임을 합니다.",
                "image": "hit_mouse.png"
            }
        },
        "curriculum2":{
            "lesson1":{
                "title": "하루를 계획해요",
                "desc": "할 일을 미리 계획하여 시간표를 짭니다. 하루의 일과를 설계해봅니다.",
                "image": "hit_mouse.png"
            },
            "lesson2":{
                "title": "선물을 포장해요",
                "desc": "로봇 공장 안에서 컨베이어 벨트 위에 있는로봇들을 제시된 규칙에 따라 상자에 포장합니다.",
                "image": "hit_mouse.png"
            },
            "lesson3":{
                "title": "숫자를 맞춰요",
                "desc": "숫자를 색깔과 순서에 맞게 차례대로 정리합니다. 처음에는 친구(캐릭터)와 함께 협동하여 정리해보고, 그 이후에는스스로 정리해봅니다.",
                "image": "hit_mouse.png"
            }
        }
    }

    # section1_table_circle(data["section1"])

    _ = requests.post(f"{base_url}submit_data", json=data)

    base_name = "parent_02"
    pdfkit.from_url(f"{base_url}{base_name}", f"{path}{base_name}.pdf",
                    options=options)


if __name__ == "__main__":
    print("This module is not intended to be run directly.")
