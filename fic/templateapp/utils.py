from gigachat import GigaChat
import datetime


def AIRequest(user_request):
    TOKEN_GIGACHAT = 'NTViNzk2ZTYtM2M1Mi00MGQxLWI4MGUtOTMwMjhhNGZhMDVhOjA3NTMwZWRiLWU0MDktNDFmZS04MzNiLWEyY2U1OTgxNDhlMg=='
    with GigaChat(credentials=TOKEN_GIGACHAT, scope="GIGACHAT_API_PERS", verify_ssl_certs=False) as giga:
        current_date = datetime.date.today().strftime("%d.%m.%Y")
        print('current_date ',current_date)
        tekst = f"""Выступи в роли помощника по заполнению формы html. 
        1. На основе предоставленного текста пользователя извлеки необходимые данные и вставь их в указанную форму в соответствующие поля. 
        2. Если значение для поля не найдено, то значение поля оставь пустым.
        3. Сегодня {current_date}.


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
        result = response.choices[0].message.content.replace("```html","").replace("```","")
        return result



