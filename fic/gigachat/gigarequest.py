from gigachat import GigaChat
import base64
import requests
import os
import datetime
from django.conf import settings
import ssl


# Пример использования сертификата в запросе
context = ssl.create_default_context()
context.verify_mode = ssl.CERT_REQUIRED  # или CERT_REQUIRED в зависимости от требований
context.check_hostname = False  # если требуется отключить проверку хоста
context.load_verify_locations()  # путь к вашему сертификату

url = 'https://gigachat.devices.sberbank.ru/api/v1/files'
file_path = "C:\\файлы\\сф\\скил фактория дьянга\\requirements.txt"
sertifikat = 'C:\\pitonprojekt\\hakaton_fic\\fic\\gigachat\\testsslcert\\sberca-test-ext.crt'
files = {
    'file': open(file_path, 'rb')
}
#print(files)
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

# tekst = """распознай поля ввода из этого текста и сделай из этого словарь json-
#     паспорт 4545033402 фамилия ыаваыпп имя ыапа отчество впрпрапр
#     """
# tekst = f"""как в https://gigachat.devices.sberbank.ru/api/v1/files отправить файл?"""
x = """
Савостиков Валерий Анатольевич 
stds58@gmail.com
python, django, docker
усидчив и любознателен
паспорт 34055692
Россия СПб можайская 37кв13
10.02.1981
учился в СкилФактории в 2024 году
9626955891
"""




def AIRequest(user_request):
    TOKEN_GIGACHAT = 'NTViNzk2ZTYtM2M1Mi00MGQxLWI4MGUtOTMwMjhhNGZhMDVhOjA3NTMwZWRiLWU0MDktNDFmZS04MzNiLWEyY2U1OTgxNDhlMg=='
    with GigaChat(credentials=TOKEN_GIGACHAT, scope="GIGACHAT_API_PERS", verify_ssl_certs=False) as giga:
        current_date = datetime.date.today().isoformat()
        tekst = f"""Выступи в роли помощника по заполнению формы html. 
        На основе предоставленного текста пользователя извлеки необходимые данные и вставь их в указанную форму в соответствующие поля. 
        Сегодня {current_date}.
        Если значение для поля не найдено, то значение поля оставь пустым.


        **поля для формы html**
        Ф.И.О.:
        Цель: 
        Общая информация о себе: 
        Возраст: 
        Семейное положение: 
        Адрес: 
        Телефон:   
        e-mail:  
        Образование:                         	
        год начала - год окончания: 
        Профессиональный опыт и навыки: 
        Дополнительная информация:
        Паспортные данные

        **Текст пользователя**
        {user_request}

        """
        response = giga.chat(tekst)
        return response.choices[0].message.content


#print(len(tekst))

