import smtplib
import ssl

from settings import EMAIL, EMAIL_PASSWORD


def send_email(subject, to_addr, from_addr, body_text):
    """
    Send an email
    """

    BODY = "\r\n".join((
        "From: %s" % from_addr,
        "To: %s" % to_addr,
        "Subject: %s" % subject,
        "",
        body_text
    ))

    smtpObj = smtplib.SMTP('smtp.mail.ru', 587)
    smtpObj.starttls(context=ssl.create_default_context())
    smtpObj.login(EMAIL, EMAIL_PASSWORD)
    smtpObj.sendmail(from_addr, [to_addr], BODY.format(body_text).encode('utf-8'))
    smtpObj.quit()


if __name__ == "__main__":
    subject = "Notification by Long Memory application"
    to_addr = "!""№;?:%:*"
    from_addr = "mehtievaa@mail.ru"
    body_text = "Уважаемый пользователь ты запретил сообщения от группы Long Memory"
    send_email(subject, to_addr, from_addr, body_text)
