import json
import requests

def getLatLng(addr):
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + addr
    akey = {"Authorization": "KakaoAK 8e5af3120d641ea5e1e345ccbcf11709"}
    #get 방식으로 주소를 포함한 링크를 헤더와 넘기면 result에 json형식의 주소와 위도경도 내용들이 출력된다.
    result = json.loads(str(requests.get(url, headers=akey).text))
    status_code = requests.get(url, headers=akey).status_code
    if(status_code != 200):
        print(f"ERROR: Unable to call rest api, http_status_code: {status_code}")
        return 0
    
#	print(requests.get(url, headers=akey))
#	print(result)

    try:
        match_first = result['documents'][0]['address']
        lon = match_first['x']
        lat = match_first['y']
#       print(lon, lat)
#       print(match_first)

        return lon, lat
    except IndexError: # match값이 없을때
        return 0
    except TypeError: # match값이 2개이상일때
        return 0
