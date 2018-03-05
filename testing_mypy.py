class Person():

    def __init__(self, surname, firstname, age, job):
        self.surname = surname
        self.firstname = firstname
        self.age = age
        self.job = job

    def get_year_of_birth(self):
        return self.age - 2018


def display_doctors(persons):
    for person in persons:
        if person.job.lower()in['gp','dentist','cardiologist']:
            print(f'{person.surname} {person.name}')


mike = Person('Davis', 'Mike', '45', 'dentist')
john = Person('Roberts', 'John', 21, 'teacher')
lee = Person('Willams', 'Lee', 'gp', 56)

display_doctors(mike)
display_doctors([mike, john, 'lee'])