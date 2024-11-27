from gigachat import GigaChat
import base64
import requests

TOKEN_GIGACHAT = 'NTViNzk2ZTYtM2M1Mi00MGQxLWI4MGUtOTMwMjhhNGZhMDVhOjA3NTMwZWRiLWU0MDktNDFmZS04MzNiLWEyY2U1OTgxNDhlMg=='

url = 'https://gigachat.devices.sberbank.ru/api/v1/files'
file_path = "C:\\файлы\\сф\\скил фактория дьянга\\requirements.txt"
files = {
    'file': open(file_path, 'rb')
}

# with GigaChat(
#     base_url="https://gigachat.devices.sberbank.ru/api/v1",
#     ca_bundle_file="ca.pem",  # chain_pem.txt
#     cert_file="\tls.pem",  # published_pem.txt
#     key_file="tls.key",
#     key_file_password="123456",
# ) as giga:
#     response = requests.post(url, files=files)
#     print(response.status_code)



# if response.status_code == 200:
#     print("Файл успешно отправлен.")
# else:
#     print("Ошибка при отправке файла.")

tekst = """распознай поля ввода из этого текста и сделай из этого словарь json- 
    паспорт 4545033402 фамилия ыаваыпп имя ыапа отчество впрпрапр
    """
tekst = f"""как в https://gigachat.devices.sberbank.ru/api/v1/files отправить файл?"""
tekst = """Max retries exceeded with url: /api/v1/files (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain (_ssl.c:1006)')"""



with GigaChat(credentials=TOKEN_GIGACHAT, scope="GIGACHAT_API_PERS", verify_ssl_certs=False) as giga:
    # response = requests.post(url, files=files)
    # print(response.status_code)
    response = giga.chat(tekst)
    print(response.choices[0].message.content)




