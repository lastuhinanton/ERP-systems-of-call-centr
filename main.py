
"""
---------------------------------------------
    __Global variables for other target__   |
---------------------------------------------

    index - special index for operators and interviewers
    client - all customer of Sosic-M
    projects_of_oper_money - operators's price of profiles
    projects_of_inter_money - interviewers's price of profiles
    projects_of_interviewers - projects of interviewers
    projects_of_operators - projects of operators
    operators - all operators
    interviewers - all interviewers
    employee - all employees
    employee_of_field - employee of field and their profiles on all projects
    employee_of_callcentr - employee of callcentr and their profiles on all projects
    all_year_salary - shows all giving salary of employee at the months
    month_now - shows which month now
    year_now - shows which year now
    archive_of_years - archive of giving salary in years

"""
index = 1000            # global variable for index of  usually and special operators
client = []
projects_of_oper_money = {}
projects_of_inter_money = {}
projects_of_operators = {}
projects_of_interviewers = {}
operators = {}
interviewers = {}
employees = {}
employee_of_field = {}
employee_of_callcentr = {}
all_year_salary = {'January': {}, 'February':{}, 'March':{}, 'April':{},
                    'May':{}, 'June':{}, 'July':{}, 'August':{},
                    'September':{}, 'October':{}, 'November':{}, 'December':{}}

archive_of_years = {}
all_people = []

"""
    iter_month - iterator for months
    Script-code down for changeing month and if it will be the full, then year changes on next
"""
month_now = 'January'                # For example 'January'
year_now = '2021'
iter_month = None

def all_months():
    for month in all_year_salary.keys():
        yield month


def year_iter():
    global iter_month
    iter_month = all_months()

def new_year():
    global year_now
    archive_of_years[year_now] = all_year_salary
    for month in all_year_salary:
        all_year_salary[month] = {}
    year_now = str(int(year_now) + 1)
    new_month()




def new_month():
    global month_now, year_now
    try:
        month_now = next(iter_month)
    except:
        print('I changed year on next! Happy new year!\n')
        year_iter()
        new_year()
        print(year_now)
        print(month_now)

year_iter()





class Customer:
    def __init__(self, customer):
        self.customer = customer
        self.name_number_projects = {}
        client.append(self.customer)

    def add_project(self, name, number, date_line, finance, one_profile, area):               # to add project of customer
        self.name_number_projects[name] = number, date_line, finance, one_profile
        if area in ('field', 'Field', 'Interviewers', 'interviewers'):
            if name not in projects_of_interviewers:
                projects_of_inter_money[name] = one_profile
                projects_of_interviewers[name] = name
                for person in employee_of_field:
                    profiles = employee_of_field[person]
                    if name not in profiles:
                        profiles[name] = 0
            else: print('Company already has your project')
        elif area in ('call-center', 'Call-center', 'Operators', 'operators', 'callcenter'):
            if name not in projects_of_operators:
                projects_of_oper_money[name] = one_profile
                projects_of_operators[name] = name
                for person in employee_of_callcentr:
                    profiles = employee_of_callcentr[person]
                    if name not in profiles:
                        profiles[name] = 0
            else: print('Company already has your project')


    def del_add_project_to_archive(self): pass



class Person:
    """
        Main block for all program!
    """
    def __init__(self, name, surname, job, birthday, email=None, number=None, interest=None, hours=0, pay=0, bonus=0):
        self.name = name
        self.surname = surname
        self.job = job
        self.birthday = birthday
        self.email = email
        self.number = number
        self.interest = interest
        self.pay = pay
        self.bonus = bonus
        self.hours = hours

        if self.__class__.__name__ == 'Interviewers':
            interviewers[name] = job
            employee_of_field[name] = {}
            if projects_of_interviewers:
                profiles = employee_of_field[name]
                for project in projects_of_interviewers:
                    profiles[project] = 0

        elif self.__class__.__name__ == 'Usually_operators':
            operators[name] = job
            employee_of_callcentr[name] = {}
            if projects_of_operators:
                profiles = employee_of_callcentr[name]
                for project in projects_of_operators:
                    profiles[project] = 0
        elif self.__class__.__name__ == 'Special_operators':
            operators[name] = job
            employee_of_callcentr[name] = {}
            if projects_of_operators:
                profiles = employee_of_callcentr[name]
                for project in projects_of_operators:
                    profiles[project] = 0
        else:
            employees[name] = job
            all_people.append(self)

    def add_inf(self, email, number, interest):
        self.email = email
        self.number = number
        self.interest = interest

    def add_pay(self, pay):
        self.pay = pay

    def up_raise(self, sum):
        Person.add_pay(self, self.pay + sum)

    def add_bonus(self, bonus):
        self.bonus += bonus

    def all_info(self):
        print(f'\nEmployee: {self.name} {self.surname}\n'
              f'Work at the company {self.job}\n'
              f'Burns {self.birthday}\n'
              f'Email: {self.email}\n'
              f'Number: {self.number}\n'
              f'Interests: {self.interest}\n'
              f'Pay: {str(self.pay)}\n'
              f'Bonus: {str(self.bonus)}\n'
              f'Passport: {self.passport}\n'
              f'Address: {self.address}\n'
              f'Family: {self.family}')

    def finished_profiles(self, many, project):
        if self.name in employee_of_callcentr:
            if project in projects_of_operators:
                profile = employee_of_callcentr[self.name]
                profile[project] += many
        elif self.name in employee_of_field:
            if project in projects_of_interviewers:
                profile = employee_of_field[self.name]
                profile[project] += many


    def go_in(self):
        import datetime
        self.begin_work = datetime.datetime.now()

    def go_out(self):
        import datetime
        self.finished_work = datetime.datetime.now()
        time_day = self.finished_work - self.begin_work
        self.hours += round(time_day.seconds / 360, 2)

    def count_salary(self):
        salary = 0
        if self.name not in all_year_salary[month_now]:
            if self.name in employee_of_callcentr:
                profiles = employee_of_callcentr[self.name]
                for project in profiles:
                    salary += projects_of_oper_money[project] * profiles[project]
                    profiles[project] = 0
                salary = salary + (self.hours * self.pay) + self.bonus
                all_year_salary[month_now][self.name] = salary
            elif self.name in employee_of_field:
                profiles = employee_of_field[self.name]
                for project in profiles:
                    salary += projects_of_inter_money[project] * profiles[project]
                    profiles[project] = 0
                all_year_salary[month_now][self.name] = salary + self.bonus
            elif self.name in employees:
                all_year_salary[month_now][self.name] = (self.hours * self.pay) + self.bonus
        else:
            print('You try count salary to employee again...')


class CEO(Person):
    """
        CEO - Chief Executive Officer
    """
    def __init__(self, name, surname, birthday):
        Person.__init__(self, name, surname, 'CEO', birthday)

    def all_info(self):
        print(f'Lider: {self.name} {self.surname}\n'
              f'Working at the company {self.job}\n'
              f'Burns: {self.birthday}')


class EDirector(CEO):
    """
        ED - Executive Director
    """
    def __init__(self, name, surname, birthday):
        Person.__init__(self, name, surname, 'Executive Director', birthday)

class Field_surveys(Person, Customer):
    """
        Main block for field surveys
    """
    def __init__(self, name, surname, birthday, passport, address, family, job):
        Person.__init__(self, name, surname, job, birthday)
        self.passport = passport
        self.address = address
        self.family = family

class Callcentr(Person, Customer):
    """
        Main block for Call-centr
    """
    def __init__(self, name, surname, birthday, passport, address, family, job):
        Person.__init__(self, name, surname, job, birthday)
        self.passport = passport
        self.address = address
        self.family = family




class Administration_C(Callcentr):
    """
        Main block for all administration of Call-centr
    """
    pass


class Others_C(Callcentr):
    """
        Main block for employee is not including in administration and operators
    """
    pass


class Main_operators(Callcentr):
    """
        In this block has all operators
    """


class HR_m(Administration_C):
    """
        In this block has all employee of administration
    """
    def __init__(self, name, surname, birthday, passport, address, family):
        Callcentr.__init__(self, name, surname, birthday, passport, address, family, 'HR-manager')


class Shift_m(Administration_C):
    """
        In this block has all shift managers
    """
    def __init__(self, name, surname, birthday, passport, address, family):
        Callcentr.__init__(self, name, surname, birthday, passport, address, family, 'Shift-manager')


class Study_m(Administration_C):
    """
        This block for Manager of Study
    """
    def __init__(self, name, surname, birthday, passport, address, family):
        Callcentr.__init__(self, name, surname, birthday, passport, address, family, 'Manager of study')

class Assistant_m(Administration_C):
    """
        This block for assistant manager
    """
    def __init__(self, name, surname, birthday, passport, address, family):
        Callcentr.__init__(self, name, surname, birthday, passport, address, family, 'Assistant-manager')

class Head(Administration_C):
    """
        This block for head of call centr
    """
    def __init__(self, name, surname, birthday, passport, address, family):
        Callcentr.__init__(self, name, surname, birthday, passport, address, family, 'Head of Call-center')

class Call_m(Administration_C):
    """
        This block for call manager
    """
    def __init__(self, name, surname, birthday, passport, address, family):
        Callcentr.__init__(self, name, surname, birthday, passport, address, family, 'Call-manager')

class Cleaning_w(Others_C):
    """
        This block for cleaning woman
    """
    def __init__(self, name, surname, birthday, passport, address, family):
        Callcentr.__init__(self, name, surname, birthday, passport, address, family, 'Cleaning woman')


class Usually_operators(Main_operators):

    def __init__(self, name, surname, birthday, passport, address, family, profiles=0):
        Callcentr.__init__(self, name, surname, birthday, passport, address, family, 'Usually_operator')
        self.profiles = profiles
        global index
        self.index = index
        index += 1

class Special_operators(Main_operators):
    """
        This block for Special operators
    """
    def __init__(self, name, surname, birthday, passport, address, family, profiles=0):
        Callcentr.__init__(self, name, surname, birthday, passport, address, family, 'Special_operator')
        self.profile = profiles
        global index
        self.index = index
        index += 1



class Administration_F(Field_surveys):
    """
        Main block for administration of fiel surveys
    """
    pass

class Interviewers(Field_surveys):
    """
        This block for interviewers
    """
    def __init__(self, name, surname, birthday, passport, address, family, profiles=0):
        Field_surveys.__init__(self, name, surname, birthday, passport, address, family, 'Interviewer')
        self.profiles = profiles
        global index
        self.index = index
        index += 1



class Other_F(Field_surveys):
    """
        Block for people aren't including at administration and others
    """
    pass

class Office_M(Administration_F):
    """
        This block for office manager
    """
    def __init__(self, name, surname, birthday, passport, address, family):
        Field_surveys.__init__(self, name, surname, birthday, passport, address, family, 'Office-manager')

class Special_M(Administration_F):
    """
        This block for manager of special project
    """
    def __init__(self, name, surname, birthday, passport, address, family):
        Field_surveys.__init__(self, name, surname, birthday, passport, address, family, 'Special manager of projects')

class Project_M(Administration_F):
    """
        This block for manager of usually project
    """
    def __init__(self, name, surname, birthday, passport, address, family):
        Field_surveys.__init__(self, name, surname, birthday, passport, address, family, 'Manager of projects')

class Accountant(Other_F):
    """
        This block for accountant
    """
    def __init__(self, name, surname, birthday, passport, address, family):
        Field_surveys.__init__(self, name, surname, birthday, passport, address, family, 'Accountant')


#========================================================
"""
THAT PLACE FOR TEST 
"""
#========================================================

# kristina = Usually_operators('Kristina Sosnova', 'Sergeevna', '31.07.01', '13081038', 'Lenina 42', '--')
# anton = Interviewers('Anton Lastuhin', 'Sergeevich', '31.07.01', '13081038', 'Lenina 42', '--')
# masha = Interviewers('Masha Ivanova', 'Ivanovna', '27.07.97', '3134 124312', 'Lenina 42', '--')
# irina = Cleaning_w('Irina Ivanova', 'Ivanovna', '27.07.97', '3134 124312', 'Lenina 42', '--')
# denis = Shift_m('Denis Karsakov', 'Ivanovna', '27.07.97', '3134 124312', 'Lenina 42', '--')
# angelika = Study_m('Angelika Yakovleva', 'Ivanovna', '27.07.97', '3134 124312', 'Lenina 42', '--')
# olga = Assistant_m('Olga Torina', 'Ivanovna', '27.07.97', '3134 124312', 'Lenina 42', '--')
# tatyana = Head('Tatyana Pushnova', 'Ivanovna', '27.07.97', '3134 124312', 'Lenina 42', '--')
# maria = Call_m('Maria Kolashnikova', 'Ivanovna', '27.07.97', '3134 124312', 'Lenina 42', '--')
# rita = Office_M('Rita Ivanova', 'Ivanovna', '27.07.97', '3134 124312', 'Lenina 42', '--')
# natalya = Special_M('Natalya Novikova', 'Ivanovna', '27.07.97', '3134 124312', 'Lenina 42', '--')
# eleonora = Project_M('Eleonora Koshevnikova', 'Ivanovna', '27.07.97', '3134 124312', 'Lenina 42', '--')
# olecya = Accountant('Olecya Erlagina', 'Ivanovna', '27.07.97', '3134 124312', 'Lenina 42', '--')
vsiom = Customer('Vsiom')
vsiom.add_project('KRATOS', 1000, '27.01.2021', '1000$', 97, 'callcenter')
vsiom.add_project('NPS_January', 1000, '27.01.2021', '1000$', 75, 'Field')

#========================================================




person_of_usually_operators = []
person_of_special_operators = []
person_of_interviewers = []
person_of_hr_manager = []
person_of_cleaning_woman = []
person_of_shift_manager = []
person_of_study_manager = []
person_of_assistant_manager = []
person_of_head_callcentr = []
person_of_call_manager = []
person_of_office_manager = []
person_of_special_manager = []
person_of_project_manager = []
person_of_accountant = []


info_for_in = {'Anton Lastuhin': {'login': 'antonlastuhin', 'password': 'elora'},
               'Angelika Yakovleva': {'login': 'angelikayak', 'password': 'mark2010'}}

def start_in():

    login = input('Enter your login...\t')
    password = input('Enter your password...\t')
    for person in info_for_in:
        tmp = info_for_in[person]
        log, pas = tmp['login'], tmp['password']
        if log == login:
            if pas == password:
                print(f'\nHello, {person}!')
                return person
            else:
                print('\nYou entered wrong login or password. Please, try again...\n')
                return start_in()
    else:
        print('\nYour entered wrong login or password. Please, try again...\n')
        return start_in()


number_of_function = {'1':'" Add employee "', '2':'" Watch information about employee "',
                  '3':'" Add information about person (email, number, interest) "', '4':'" Add pay to employee "',
                  '5':'" Add bonus to employee "', '6':'" Up raise "', '7':'" Enter time when employee go in to job "',
                  '8':'" Enter time when employee go out from job "', '9':'" Enter success profiles of day for employee "',
                  '10':'" Count salary of all employees "'}

def number_of_action():
    """
    That function return number. Next function defines number that know what it will do 
    """
    first_request = input(f'\nMr. {name_start}, do you wanna watch what can that program do?\t')
    print()

    def third_request():
        """
        That function return number
        """
            print('\n1.\tAdd employee\n'
                  '2.\tWatch information about employee\n'
                  '3.\tAdd information about person (email, number, interest)\n'
                  '4.\tAdd pay to employee\n'
                  '5.\tAdd bonus to employee\n'
                  '6.\tUp raise\n'
                  '7.\tEnter time when employee go in to job\n'
                  '8.\tEnter time when employee go out from job\n'
                  '9.\tEnter success profiles of day for employee\n'
                  '10.\tCount salary of all employees\n')

            number_tmp =  input('What do you wanna do? Enter number of your request...\t')           
            if number_tmp in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'):                       
                return number_tmp                                                                      #If user entered right number function returns number
            else:
                print(f'\nYou entered wrong request, {name_start}\n'                                    # and if not than function do request on the enter repeatly  
                    'Please, repeat your request again, only choose "Yes" or "No"\n')                   # to the " third_request() " function
                return third_request()

    if first_request in ('Yes', 'yes', 'YES', 'YEs', 'YeS', 'yeS'):
        return third_request()
                

    elif first_request in ('No', 'no', 'NO', 'nO'):
        def second_request():
            question = input('Do you know numbers funсtions of that program?\t')

            if question in ('Yes', 'yes', 'YES', 'YEs', 'YeS', 'yeS'):
                return input('What do you wanna do? Enter number of your request...\t')                # returns number from 1 to 10, but if number isn't 
            elif question in ('No', 'no', 'NO', 'nO'):                                                 #    from 1 to 10 or it's not number than script sends  
                 return question                                                                       #    on checking
            else:
                print(f'\nYou entered wrong request, {name_start}\n'
                    'Please, repeat your request again, only choose "Yes" or "No"\n')
                return second_request()
                

        tmp = second_request()
        if tmp in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'):                                 # here checking request user's number 
            return tmp                                                                                 # if user gived answer no on question if know program's function
        elif tmp in ('No', 'no', 'NO', 'nO'):
            return number_of_action()
        else:
            print(f'\n{name_start}, you entered wrong number\n'
                    'Please, repeat your number from 1 to 10\n')
            return third_request()



    else:
        print(f'\n{name_start}, you entered wrong request\n'                                          # if user entered wrong request than he or she returns
            'Please, repeat your request again, only choose "Yes" or "No"\n')                         # on " number_of_action " function
        return number_of_action()           


def main_actions(number):
    def req_add_employee():
        x = None
        def enter_employee():
            nonlocal x
            persons = {'1':'Special operator', '2':'Usually operator', '3':'Interviewer', '4':'HR manager', '5':'Cleaning woman', '6':'Shift manager',
                  '7':'Study manager', '8':'Assistant manager', '9':'Head of call-centr', '10':'Call manager', '11':'Office manager',
                  '12':'Special manager', '13':'Project manager'}
            for i, person in enumerate(persons.values(), start=1):
                print(f'{i}. {person}')
            request = input('\nEnter number of who you wanna add...\t')
            answer = input(f'\nAre you sure wanna enter {persons[request]}?\t')
            if answer in ('Yes', 'yes', 'YES', 'YEs', 'YeS', 'yeS'):
                name = input('Enter name with lastname...\t')
                surname = input('Enter surname...\t')
                birthday = input('Enter birthday...\t')
                passport = input('Enter number of passport...\t')
                address = input('Enter address...\t')
                family = input('Enter status of family...\t')

                if request == '1':
                    x = Special_operators(name, surname, birthday, passport, address, family)
                    person_of_special_operators.append(x)
                elif request == '2':
                    x = Usually_operators(name, surname, birthday, passport, address, family)
                    person_of_usually_operators.append(x)
                elif request == '3':
                    x = Interviewers(name, surname, birthday, passport, address, family)
                    person_of_interviewers.append(x)
                elif request == '4':
                    x = HR_m(name, surname, birthday, passport, address, family)
                    person_of_hr_manager.append(x)
                elif request == '5':
                    x = Cleaning_w(name, surname, birthday, passport, address, family)
                    person_of_cleaning_woman.append(x)
                elif request == '6':
                    x = Shift_m(name, surname, birthday, passport, address, family)
                    person_of_shift_manager.append(x)
                elif request == '7':
                    x = Study_m(name, surname, birthday, passport, address, family)
                    person_of_study_manager.append(x)
                elif request == '8':
                    x = Assistant_m(name, surname, birthday, passport, address, family)
                    person_of_assistant_manager.append(x)
                elif request == '9':
                    x = Head(name, surname, birthday, passport, address, family)
                    person_of_head_callcentr.append(x)
                elif request == '10':
                    x = Call_m(name, surname, birthday, passport, address, family)
                    person_of_call_manager.append(x)
                elif request == '11':
                    x = Office_M(name, surname, birthday, passport, address, family)
                    person_of_office_manager.append(x)
                elif request == '12':
                    x = Special_M(name, surname, birthday, passport, address, family)
                    person_of_special_manager.append(x)
                elif request == '13':
                    x = Project_M(name, surname, birthday, passport, address, family)
                    person_of_project_manager.append(x)
                elif request == '14':
                    x = Accountant(name, surname, birthday, passport, address, family)
                    person_of_accountant.append(x)
                all_people.append(x)

            request = input('\nDo you wanna add employee again?\t')
            if request in ('Yes', 'yes', 'YES', 'YEs', 'YeS', 'yeS'):
                enter_employee()
            elif request in ('No', 'no', 'NO', 'nO'):
                print('Good work, Creater!')


        enter_employee()

    def req_watch_inf_ab_emp():

        def watch_inf():
            print([x.name for x in all_people])
            request_name = input('Enter name...\t')

            if request_name in [x.name for x in all_people]:
                for person in all_people:
                    if person.name == request_name:
                        person.all_info()
            else:
                print(f'{request_name} is not working. Try again...')
                watch_inf()

            again = input('\nDo you wanna watch information about person again?\t')
            if again in ('Yes', 'yes', 'YES', 'YEs', 'YeS', 'yeS'):
                watch_inf()
            elif again in ('No', 'no', 'NO', 'nO'):
                print('Good job, Creater!')

        watch_inf()


    def req_add_inf_ab_per():

        def add_inf_ab():

            name = input('Enter name...\t')
            if name in [x.name for x in all_people]:
                for person in all_people:
                    if person.name == name:
                        email = input('Enter email...')
                        number = input('Enter number...')
                        interest = input('Enter interest...')
                        person.add_inf(email, number, interest)
            else:
                print(f'{name} is not working. Try again...')
                add_inf_ab()

            again = input('Do you wanna add information about employee again?')
            if again in ('Yes', 'yes', 'YES', 'YEs', 'YeS', 'yeS'):
                add_inf_ab()
            elif again in ('No', 'no', 'NO', 'nO'):
                print('Good job, Creater!')

        if operators:
            print('All operators:')
            for i, operator in enumerate(operators, start=1):
                print(f'{i}. {operator}')

        if interviewers:
            print('All interviewers:')
            for i, interviewer in enumerate(interviewers, start=1):
                print(f'{i}. {interviewer}')

        if employees:
            print('All employees:')
            for i, person in enumerate(employee, start=1):
                print(f'{i}. {person}')

        if not operators and not interviewers and not employees:
            print('Thate')
        else:
            add_inf_ab()

        


    def req_add_pay_to_emp():
        def add_pay():
            print([x.name for x in all_people])
            request_name = input('Enter name...\t')
            if request_name in [x.name for x in all_people]:
                for person in all_people:
                    if request_name == person.name:
                        pay = int(input(f'Enter how much pay you want to add to {person.name}'))
                        person.add_pay(pay)
                    else:
                        print(f'{request_name} is not working. Try again...')
                        add_pay()
            again = input('Do you wanna add pay to person again?\t')
            if again in ('Yes', 'yes', 'YES', 'YEs', 'YeS', 'yeS'):
                add_pay()
            elif again in ('No', 'no', 'NO', 'nO'):
                print('Good job, Creater!')

        add_pay()


    def req_add_bonus_to_emp():
        def add_bonus():
            print([x.name for x in all_people])
            request_name = input('Enter name...\t')
            if request_name in [x.name for x in all_people]:
                for person in all_people:
                    if request_name == person.name:
                        bonus = int(input(f'Enter what kind bonus you want to add to {person.name}'))
                        person.add_bonus(bonus)
                    else:
                        print(f'{request_name} is not working. Try again...')
                        add_bonus()
            again = input('Do you wanna add pay to person again?\t')
            if again in ('Yes', 'yes', 'YES', 'YEs', 'YeS', 'yeS'):
                add_bonus()
            elif again in ('No', 'no', 'NO', 'nO'):
                print('Good job, Creater!')

        add_bonus()


    def req_up_raise():
        def up_raise():
            print([x.name for x in all_people])
            request_name = input('Enter name...\t')
            if request_name in [x.name for x in all_people]:
                for person in all_people:
                    if request_name == person.name:
                        up_salary = int(input(f'Enter how much you want to add up-raise to {person.name}'))
                        person.up_raise(up_salary)
                    else:
                        print(f'{request_name} is not working. Try again...')
                        up_raise()
            again = input('Do you wanna add up-raise to person again?\t')
            if again in ('Yes', 'yes', 'YES', 'YEs', 'YeS', 'yeS'):
                up_raise()
            elif again in ('No', 'no', 'NO', 'nO'):
                print('Good job, Creater!')

        up_raise()


    def req_emp_go_in():
        def emp_go_in():
            print([x.name for x in all_people])
            request_name = input('Enter name...\t')
            if request_name in [x.name for x in all_people]:
                for person in all_people:
                    if request_name == person.name:
                        person.go_in()
                    else:
                        print(f'{request_name} is not working. Try again...')
                        emp_go_in()
            again = input('Do you start shift of employee again?\t')
            if again in ('Yes', 'yes', 'YES', 'YEs', 'YeS', 'yeS'):
                emp_go_in()
            elif again in ('No', 'no', 'NO', 'nO'):
                print('Good job, Creater!')

        emp_go_in()


    def req_emp_go_out():
        def emp_go_out():
            print([x.name for x in all_people])
            request_name = input('Enter name...\t')
            if request_name in [x.name for x in all_people]:
                for person in all_people:
                    if request_name == person.name:
                        person.go_out()
                    else:
                        print(f'{request_name} is not working. Try again...')
                        emp_go_out()
            again = input('Do you start shift of employee again?\t')
            if again in ('Yes', 'yes', 'YES', 'YEs', 'YeS', 'yeS'):
                emp_go_out()
            elif again in ('No', 'no', 'NO', 'nO'):
                print('Good job, Creater!')

        emp_go_out()


    def req_suc_prof_of_emp():
        def emp_finished_profiles():
            print('\nAll operators:')
            for i, person in enumerate(operators, start=1):
                print(f'{i}. {person}')
            print('\nAll projects of operators:')
            for i, project in enumerate(projects_of_operators, start=1):
                print(f'{i}. {project}')

            print('\n\nAll interviewers:')
            for i, person in enumerate(interviewers, start=1):
                print(f'{i}. {person}')
            print('\nAll projects of interviewers:')
            for i, project in enumerate(projects_of_interviewers, start=1):
                print(f'{i}. {project}')


            request_name = input('Enter name...\t')
            if request_name in [x.name for x in all_people]:
                for person in all_people:
                    if request_name == person.name:
                        many = int(input('Enter how many profiles...'))
                        project = input('Enter project...')
                        try:
                            person.finished_profiles(many, project)
                        except:
                            print('You enter wrong project. Try again...')
                            emp_finished_profiles()
                    else:
                        print(f'{request_name} is not working. Try again...')
                        emp_finished_profiles()
            again = input('Do you start shift of employee again?\t')
            if again in ('Yes', 'yes', 'YES', 'YEs', 'YeS', 'yeS'):
                emp_finished_profiles()
            elif again in ('No', 'no', 'NO', 'nO'):
                print('Good job, Creater!')

        emp_finished_profiles()

    def req_count_salary():
        def count_sal():
            for person in all_people:
                person.count_salary()
            print(all_year_salary)
            new_month()

        count_sal()


    req = input(f'\nAre you sure you want to do that function {number_of_function[number]}?\t')
    if req in ('Yes', 'yes', 'YES', 'YEs', 'YeS', 'yeS'):
        if number == '1':
            req_add_employee()

        elif number == '2':
            req_watch_inf_ab_emp()

        elif number == '3':
            req_add_inf_ab_per()

        elif number == '4':
            req_add_pay_to_emp()

        elif number == '5':
            req_add_bonus_to_emp()

        elif number == '6':
            req_up_raise()

        elif number == '7':
            req_emp_go_in()

        elif number == '8':
            req_emp_go_out()

        elif number == '9':
            req_suc_prof_of_emp()

        elif number == '10':
            req_count_salary()
    elif req in ('No', 'no', 'NO', 'nO'):
        number = number_of_action()
        main_actions(number)

    request_again = input('\nDo you wanna do something again?\t')
    if request_again in ('Yes', 'yes', 'YES', 'YEs', 'YeS', 'yeS'):
        number = number_of_action()
        main_actions(number)
    elif request_again in ('No', 'no', 'NO', 'nO'):
        request_again = input(f'Do you wanna go out, {name_start}?\t')
        if request_again in ('Yes', 'yes', 'YES', 'YEs', 'YeS', 'yeS'):
            print('\nYour are cool, Creater!')
        elif request_again in ('No', 'no', 'NO', 'nO'):
            number = number_of_action()
            main_actions(number)


if __name__ == '__main__':
    name_start = start_in()
    number = number_of_action()
    main_actions(number)










