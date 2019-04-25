class Student(object):
    def get_name(self):
        return self.name

    def set_name(self, value):
        self.name = value


s = Student()
s.name = '123'
print(s.name)
print(s.get_name())
s.set_name('321')
print(s.get_name())
