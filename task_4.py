class EmployeeSalary:
    hourly_payment = 400
    
    def __init__(self, name, hours=None, rest_days=None, email=None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email
        
    @classmethod
    def get_hours(cls, name, rest_days=None, email=None):
        if rest_days is not None:
            hours = (7 - rest_days) * 8
        else:
            hours = None
        return cls(name, hours, rest_days, email)
    
    @classmethod
    def get_email(cls, name, hours=None, rest_days=None):
        email = f"{name.replace(' ', '_').lower()}@email.com"
        return cls(name, hours, rest_days, email)
    
    @classmethod
    def set_hourly_payment(cls, value):
        cls.hourly_payment = value
        
    def salary(self):
        if self.hours is None:
            hours = self.get_hours(self.name, self.rest_days).hours
        else:
            hours = self.hours
        return hours * self.hourly_payment
