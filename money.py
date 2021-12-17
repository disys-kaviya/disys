class moneytransfer

    def _init_(self,Email_ID,Phone_number,Name,Account_number):
       self.emailid=Email_ID
       self.mobile=Phone_number
       self.accountholdername=name
       self.Account=Account_number
    def open_gpay(self):

       print("*****step into moneytransfer*****")


    def email_verification(self):
       emailid=input("Enter the email id:")
       print("The email id is:"+emailid)
       if type(emailid) == str:
           if len(emailid)<= 15:
               print("email_id is verified")
           else:
               raise ValueError("The Email_id should not contain more than 30 values")
       else:
           raise TypeError("Invalid email-id")

    def mobile_verification(self):
            mobile=input("Enter the phone number:")
            print("The Phone number is:"+mobile)
            if (len(mobile)==10) :
                if (type(mobile) ==int):
                    print("phone-number verified")
                else:
                    raise TypeError("The phone-number should contain only integers")

    def name_verification(self):
        accountholdername=input("Enter the accountholdername:")
        print("accountholdername is:"+aacountholdername)
        if type(accountholdername)==str:
            if len(accountholdername)<= 20:
                print("name verified")
            else:
                raise ValueError("The name should contain lesser than or equal to 20 letters")
       else:
           raise TypeError("The name should contain letters only")
        
    def otp_verification(self,code,otp):
        if(otp==code):
            print("otp is verified")
        else:
            raise ValueError("The OTP you are entered is not correct")

    def Bank_verification(seLf):
        Account=input("Enter your account number:")
        print("Account number is:"+Account)
        if type(Account)==str:
            if(len(Account)==10):
                print("Bank aacount Verified")
            else:
                raise TypeError("The number should be equal to 10")
        else:
            raise TypeError("This is a invalid bank account number")



     def set_Pin(self,number):
         self.pin=number
         if (len(self.pin)==4):
             print("your pin is successfully created")
         else
            raise ValueError("Invalid pin_number")

     def Enter_your_pin(self,match,pin):
         self.match=match
         self.pinno=pin
         if self.match==self.pinno:
             print("user pin is matched")
             print("Transaction succesful")
         else:
             raise ValueError("pin not matched")
             print("Transaction failed")
        


            

        
