class phonecontact:

    def __int__(self,name,num,rel):
        self.contactname=name
        self.contactnumber=num
        self.contactrelation=rel


    def view_contact(self):
        print("*****my contact details******")

    def contactname_verification(self):
        contactname=input("Enter the contactname:")
        print("contactname is:"+contactname)
        if type(contactname)== str:
            if len(contactname)<= 15:
                print("contactname verified")
            else:
                raise ValueError("contactname should contain <=15 letters")

        else:
            raise TypeError("contactname should not contain any symbols")

    def contactnumber_verification(self):
         contactnumber=input("Enter the number:")
         print("contactnumber is:"+contactnumber)
         if type(contactnumber)== int:
             if (len(contactnumber)== 10):
                 print("contactnumber verified")
         else:
             raise TypeError("number should not contain any symbols and relation")


    def contactrelation_verification(self):
        contactrelation=input("Enter the relation:")
        print("relation typer is:"+contactnumber)
        if type(self.relation) == str:
            if len(self.relation) <=10:
                print("relation uptaded")
            else:
                raise ValueErorr("Letter should not exist 10")
        else:
            raise TypeError("Relation should contain 10 letters only")

kaviya=phonecontact("kaviya",9600706533,"friend")
kaviya.view_contact()
kaviya.contactname_verification()
kaviya.contactnumber_verification()
kaviya.contactrelation_verification()
               
