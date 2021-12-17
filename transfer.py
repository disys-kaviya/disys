import moneytransfer


kaviya=mobiletransfer.moneytransfer("kaviya12@gmail.com","9600706533","kaviya","40261789654")
kaviya.open_moneytransfer()
kaviya.email_verification()
kaviya.mobile_verification()
kaviya.name_verification()
kaviya.otp_verification(12013,12014)
kaviya.Bank_verification()
kaviya.set_pin("1203")
kaviya.Enter_your_Pin(4501,4501)


class Phone_pe(moneytransfer):
    def _init_(self,Email_ID,Phone_nukmber,Name,Account_number):


        super()._init_(Email_ID,Phone_number,Name,Account_number)

    def open_phonepe(self):
        print("phone pe")


dinu=Phone_pe("kaviya12@gmail.com","9600706533","dinu","9600706533")
dinu.open_phonepe()
dinu.mobile_verification()
dinu.name_verification()
dinu.otp_verification(45687,98745)
dinu.Bank_verification()
dinu.set_pin("4567")
dinu.Enter_your_Pin(6548,6548)
