
class Doctor:
    #__slots__ = ['tab_number', 
    #             'last_name', 
    #             'first_name', 
    #             'patronymic', 
    #             'speciality', 
    #             'work_experience', #in hours
    #             'work_hours',      
    #             'office', 
    #             'phone',
    #             '__dict__']
    field_names = ['tab_number', 'last_name', 'first_name', 'patronymic', 'speciality', 'work_experience',
                   'work_hours', 'office', 'phone']

    specialities = ['Doctor-geneticist', 'Psychiatrist', 'Phlebologist', 'Nephrologist', 'Hepatologist',
                    'Homeopath and herbal therapist', 'Children\'s Doctors']

    def __init__(self, **args):
        self.__dict__.update(args)

    def __str__(self):
        return str(self.__dict__)
