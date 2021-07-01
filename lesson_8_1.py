import re


def email_parse(email_addres):
    RE_email = re.compile(r'(?P<username>([\w]+))@(?P<domain>[^&]+\.\w+)', re.IGNORECASE)
    if not RE_email.match(email_addres):
        raise ValueError(f'wrong email: {email_addres}')
    print(RE_email.match(email_addres).groupdict())


for i in ['someone@geekbrains.ru', 'som&one@geekbraisru', 'someone@geekbrainsru']:
    try:
        email_parse(i)
    except ValueError as err:
        print(err)