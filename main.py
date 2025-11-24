from pyscript import display

def club_theater(e):
    club1 = {'Club Name' : 'Theater Club',
        'Description' : 'A place to connect with other aspiring actors to show off their acting skills.',
        'Meeting Time' : '3:00-5:00',
        'Location' : 'MM Hall',
        'Advisor' : 'Ms. Darbus',
        'Number of Members' : '20',
        'Category' : 'Non-Academic'
    }




keys = ['Club Name', 'Description', 'Meeting Time', 'Location', 'Advisor', 'Number of Members', 'Category']
values = ['Theater Club', 'A place to connect with other aspiring actors to show off their acting skills.', '3:00-5:00', 'MM Hall', 'Ms. Darbus', '20', 'Non-Academic' ]

club1 = dict(zip(keys, values)) # convert and combine
display(club1, target='output')

def club_science(e):
    club2 = {'Club Name' : 'Science Club',
            'Description' : 'In search of the greater good with science!',
            'Meeting Time' : '3:00-4:30',
            'Location' : 'Room 405',
            'Advisor' : 'Ms. Zabala',
            'Number of Members' : '25',
            'Category' : 'Academic'
    }

keys2 = ['Club Name', 'Description', 'Meeting Time', 'Location', 'Advisor', 'Number of Members', 'Category']
values2 = ['Science Club', 'In search of the greater good with science!', '3:00-4:30', 'Room 405', 'Ms. Zabala', '25', 'Academic' ]

club2 = dict(zip(keys2, values2)) # convert and combine
display(club2, target='output')

def club_glee(e):
    club3 = {'Club Name' : 'Glee Club',
            'Description' : 'A place where people can sing their hearts out.',
            'Meeting Time' : '3:00-4:30',
            'Location' : 'Music Room',
            'Advisor' : 'Ms. Loyola',
            'Number of Members' : '38',
            'Category' : 'Non-Academic'
    }

keys3 = ['Club Name', 'Description', 'Meeting Time', 'Location', 'Advisor', 'Number of Members', 'Category']
values3 = ['Glee Club', 'A place where people can sing their hearts out.', '3:00-4:30', 'Music Room', 'Ms. Loyola', '38', 'Non-Academic' ]

club3 = dict(zip(keys3, values3)) # convert and combine
display(club3, target='output')

def club_varsity(e):
    club4 = {'Club Name' : 'Varsity Basketball Club',
            'Description' : 'Where basketball fans and players strive to become the greatest.',
            'Meeting Time' : '3:00-5:00',
            'Location' : 'Quadrangle',
            'Advisor' : 'Mr. Gervacio',
            'Number of Members' : '30',
            'Category' : 'Non-Academic'
    }

keys4 = ['Club Name', 'Description', 'Meeting Time', 'Location', 'Advisor', 'Number of Members', 'Category']
values4 = ['Varsity Basketball Club', 'Where basketball fans and players strive to become the greatest.', '3:00-5:00', 'Quadrangle', 'Mr. Gervacio', '30', 'Non-Academic' ]

club4 = dict(zip(keys4, values4)) # convert and combine
display(club4, target='output')

