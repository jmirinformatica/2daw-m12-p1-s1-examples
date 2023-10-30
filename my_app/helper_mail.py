import smtplib, ssl

class MailManager:

    def init_app(self, app):
        # agafo els paràmetres de configuració
        self.sender_addr = app.config.get('MAIL_SENDER_ADDR')
        self.sender_password = app.config.get('MAIL_SENDER_PASSWORD')
        self.smtp_server = app.config.get('MAIL_SMTP_SERVER')
        self.smtp_port = app.config.get('MAIL_SMTP_PORT')

        print(f"self.sender_addr: {self.sender_addr}")
        print(f"self.sender_password: {self.sender_password}")
        print(f"self.smtp_server: {self.smtp_server}")
        print(f"self.smtp_port: {self.smtp_port}")

        # els missatges de contacte s'envien a aquesta adreça
        self.contact_addr = app.config.get('CONTACT_ADDR')

    # https://realpython.com/python-send-email/#option-2-using-starttls
    def send_contact_msg(self, msg):
        context = ssl.create_default_context()
        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(self.sender_addr, self.sender_password)
            server.sendmail(self.sender_addr, self.contact_addr, msg)
