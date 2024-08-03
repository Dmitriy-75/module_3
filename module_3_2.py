def send_email(message, recipient, *, sender="university.help@gmail.com"):
    in_dog = "@" in str(recipient) and "@" in sender
    spl_send = list(sender.split("."))
    spl_rec = list(recipient.split("."))
    list_url = ["com", "ru", "net"]
    check_url_send = spl_send[-1] in list_url
    check_url_rec = spl_rec[-1] in list_url
    if in_dog is False or check_url_send is False or check_url_rec is False:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")


send_email('Это сообщение для проверки связи', 'turbine@gmail.com')
send_email('Это сообщение для проверки связи', 'turbinegmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'falcon@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.stalker@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
