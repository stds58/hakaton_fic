import requests
import json


url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"
TOKEN_GIGACHAT = 'NTViNzk2ZTYtM2M1Mi00MGQxLWI4MGUtOTMwMjhhNGZhMDVhOjA3NTMwZWRiLWU0MDktNDFmZS04MzNiLWEyY2U1OTgxNDhlMg=='



def get_token():
    url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
    payload = 'scope=GIGACHAT_API_PERS'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'RqUID': '<ВАШ Client Secret>',
        'Authorization': 'Basic <ВАШИ Данные Авторизации>'
    }
    response = requests.request("POST", url, headers=headers, data=payload, verify='chain.pem')
    return response.json()


def get_answer(text, access_token):
    payload = json.dumps({
        # есть еще GigaChat-Pro (50к бесплатных) и GigaChat-Plus (платный)
        "model": "GigaChat",
        "messages": [
            {
                "role": "user",
                "content": text  # ваш запрос
            }
        ],
        "temperature": 1,
        "top_p": 0.1,
        "n": 1,
        "stream": False,
        "max_tokens": 512,  # максимальное кол-во использованных токенов
        "repetition_penalty": 1
    })

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'Bearer {TOKEN_GIGACHAT}'  # токен доступа
    }

    response = requests.request(
        "POST", url, headers=headers, data=payload, verify='chain.pem')
    return response.json()


def get_img():  # получение изображения по fileId
    url = f"https://gigachat.devices.sberbank.ru/api/v1/files"
    file_path = "C:\\файлы\\сф\\скил фактория дьянга\\requirements.txt"
    sertifikat_path = 'C:\\pitonprojekt\\hakaton_fic\\fic\\gigachat\\testsslcert\\SberCA Test Int.cer'
    sertifikat = open(sertifikat_path, 'rb')
    files = {
        'file': open(file_path, 'rb')
    }
    payload = {}
    headers = {
        'Accept': 'application/pdf',
        'Authorization': f'Bearer {TOKEN_GIGACHAT}'
    }
    response = requests.request("GET", url, headers=headers, files=files, verify=sertifikat_path)
    return response.content


x = get_img()
print(x)


