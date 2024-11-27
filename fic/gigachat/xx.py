from gigachat import GigaChat

TOKEN_GIGACHAT = 'NTViNzk2ZTYtM2M1Mi00MGQxLWI4MGUtOTMwMjhhNGZhMDVhOjA3NTMwZWRiLWU0MDktNDFmZS04MzNiLWEyY2U1OTgxNDhlMg=='



with GigaChat(credentials=TOKEN_GIGACHAT, scope="GIGACHAT_API_PERS", verify_ssl_certs=False) as giga:
    response = giga.chat("""распознай поля ввода из этого текста и сделай из этого словарь json- 
    паспорт 4545033402 фамилия ыаваыпп имя ыапа отчество впрпрапр
    """)
    print(response.choices[0].message.content)




