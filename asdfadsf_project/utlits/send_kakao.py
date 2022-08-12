import requests
import json

#발행한 토큰 불러오기
with open("json/token.json","r") as kakao:
    tokens = json.load(kakao)

cnt = 0
def send_kakaoTalk():
    if cnt == 0:
        url="https://kapi.kakao.com/v2/api/talk/memo/default/send"

        headers={
            "Authorization" : "Bearer " + tokens["access_token"]
        }

        data = {
            'object_type': 'text',
            'text': '손가락 욕이 감지되었습니다.',
            'link': {
                'web_url': 'https://developers.kakao.com',
                'mobile_web_url': 'https://developers.kakao.com'
            },
            'button_title': '감지'
        }
        
        data = {'template_object': json.dumps(data)}
        response = requests.post(url, headers=headers, data=data)
        response.status_code
        cnt + 1
    else:
        pass