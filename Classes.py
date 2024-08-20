class Tweet:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        
    def testing(self):
        return f"Hello {self.fname}"

firstn = "Larry"
lastn = "Holmes"

employee = Tweet(firstn, lastn)

print(employee.testing())



class dress_code:
    def __init__(self,pants_color, pants_type, shirt_color, shirt_type,shoes_type):
     self.pants_color = pants_color
     self.pants_type = pants_type
     self.shirt_color = shirt_color
     self.shirt_type = shirt_type
     self.shoes_type = shoes_type

    def WCS_dress_code(self):
     return f"The 2024 School dress code is: {self.pants_color} {self.pants_type} pants, {self.shirt_color} {self.shirt_type} shirt and {self.shoes_type} shoes"



pants_clr = "Tan"
pants_typ = "Kacki"
shirt_clr = "Red"
shirt_typ = "Polo"
shoe_typ = "Close Toe"

school_policy = dress_code(pants_clr,pants_typ,shirt_clr,shirt_typ,shoe_typ)

print(school_policy.WCS_dress_code())