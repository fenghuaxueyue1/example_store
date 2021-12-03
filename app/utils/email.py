import yagmail

from app.config import Config

smtp = yagmail.SMTP(user=Config.SMTP_USER, password=Config.SMTP_PSWD, host=Config.SMTP_HOST)
