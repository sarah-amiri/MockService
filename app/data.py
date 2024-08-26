from datetime import datetime

users = [
    '1234567891',
    '6017580124',
    '4828128514',
    '3336527181',
    '1516697189',
    '1865721913',
]

banks = [
    'melli',
    'mellat',
    'saderat',
    'tejarat',
]

users_detail = {
    '1234567891': {
        'customer_id': '1234567891',
        'phone_number': '09112227891',
        'code': 'f08edd05-eae7-4499-93fa-908e49f3306f',
        'banks': ['melli', 'mellat'],
    },
    '6017580124': {
        'customer_id': '6017580124',
        'phone_number': '09112220124',
        'code': 'a6d4a2e1-71ae-43c8-a8ac-e4888cf8ea4a',
        'banks': ['melli', 'saderat'],
    },
    '4828128514': {
        'customer_id': '4828128514',
        'phone_number': '09112228514',
        'code': '1b6e4d0d-cbf3-4a7b-8b92-8233b832ca17',
        'banks': ['melli', 'mellat', 'saderat', 'tejarat'],
    },
    '3336527181': {
        'customer_id': '3336527181',
        'phone_number': '09112227181',
        'code': '32a0368e-3658-4b27-ba8e-1a39957cdeac',
        'banks': ['melli'],
    },
    '1516697189': {
        'customer_id': '1516697189',
        'phone_number': '09112227189',
        'code': 'a937893d-bf4a-4d26-8bdf-2a65f211450f',
        'banks': ['saderat'],
    },
    '1865721913': {
        'customer_id': '1865721913',
        'phone_number': '09112221913',
        'code': '9b6ac30b-7675-444a-ac0c-89f70878fd08',
        'banks': ['melli', 'mellat', 'saderat'],
    },
}

banks_details = {
    '1234567891': {
        'melli': {
            'transactions': [
                {'date': datetime(2024, 8, 1, 11, 11, 10), 'type': 'deposit', 'amount': 1000},
                {'date': datetime(2024, 7, 29, 11, 10, 2), 'type': 'withdraw', 'amount': 11000},
                {'date': datetime(2024, 7, 1, 10, 21, 31), 'type': 'deposit', 'amount': 50000},
            ]
        },
        'mellat': {
            'transactions': [
                {'date': datetime(2024, 1, 8, 9, 13, 0), 'type': 'deposit', 'amount': 10000},
                {'date': datetime(2023, 11, 10, 8, 0, 5), 'type': 'deposit', 'amount': 50000},
            ]
        },
    },
    '6017580124': {
        'melli': {
            'transactions': [
                {'date': datetime(2024, 1, 1, 9, 13, 11), 'type': 'withdraw', 'amount': 9000},
                {'date': datetime(2024, 1, 1, 8, 10, 0), 'type': 'withdraw', 'amount': 9000},
                {'date': datetime(2024, 1, 1, 8, 1, 1), 'type': 'deposit', 'amount': 50000},
            ]
        },
        'saderat': {
            'transactions': [
                {'date': datetime(2023, 10, 13, 7, 30, 31), 'type': 'deposit', 'amount': 40000},
            ]
        },
    },
    '4828128514': {
        'melli': {
            'transactions': [
                {'date': datetime(2024, 7, 9, 9, 11, 0), 'type': 'withdraw', 'amount': 41900},
                {'date': datetime(2024, 7, 9, 8, 48, 1), 'type': 'deposit', 'amount': 50000},
            ]
        },
        'mellat': {
            'transactions': [
                {'date': datetime(2024, 3, 20, 8, 1, 1), 'type': 'deposit', 'amount': 5000},
            ]
        },
        'saderat': {
            'transactions': [
                {'date': datetime(2024, 8, 3, 9, 13, 11), 'type': 'withdraw', 'amount': 9000},
                {'date': datetime(2024, 8, 2, 8, 10, 0), 'type': 'deposit', 'amount': 9000},
                {'date': datetime(2024, 8, 1, 8, 1, 1), 'type': 'deposit', 'amount': 9000},
            ]
        },
        'tejarat': {
            'transactions': [
                {'date': datetime(2024, 8, 3, 10, 13, 11), 'type': 'withdraw', 'amount': 9000},
                {'date': datetime(2024, 8, 2, 10, 10, 0), 'type': 'withdraw', 'amount': 9000},
                {'date': datetime(2024, 8, 1, 10, 1, 1), 'type': 'deposit', 'amount': 27000},
            ]
        },
    },
    '3336527181': {
        'melli': {
            'transactions': [
                {'date': datetime(2024, 1, 1, 9, 15, 6), 'type': 'withdraw', 'amount': 9000},
                {'date': datetime(2024, 1, 1, 9, 13, 0), 'type': 'withdraw', 'amount': 9000},
                {'date': datetime(2024, 1, 1, 8, 10, 0), 'type': 'withdraw', 'amount': 9000},
                {'date': datetime(2024, 1, 1, 8, 1, 1), 'type': 'deposit', 'amount': 41000},
            ]
        },
    },
    '1516697189': {
        'saderat': {
            'transactions': [
                {'date': datetime(2024, 8, 4, 9, 1, 0), 'type': 'withdraw', 'amount': 11000},
                {'date': datetime(2024, 8, 3, 9, 13, 11), 'type': 'withdraw', 'amount': 9000},
                {'date': datetime(2024, 8, 2, 9, 10, 0), 'type': 'withdraw', 'amount': 9000},
                {'date': datetime(2024, 8, 1, 9, 1, 1), 'type': 'deposit', 'amount': 33000},
            ]
        },
    },
    '1865721913': {
        'melli': {
            'transactions': [
                {'date': datetime(2024, 7, 9, 11, 38, 35), 'type': 'deposit', 'amount': 11000},
            ]
        },
        'mellat': {
            'transactions': [
                {'date': datetime(2024, 6, 15, 12, 11, 1), 'type': 'deposit', 'amount': 5000},
            ]
        },
        'saderat': {
            'transactions': [
                {'date': datetime(2024, 8, 3, 13, 13, 36), 'type': 'withdraw', 'amount': 2200},
                {'date': datetime(2024, 8, 2, 12, 55, 22), 'type': 'deposit', 'amount': 3000},
                {'date': datetime(2024, 8, 1, 14, 17, 18), 'type': 'deposit', 'amount': 9000},
            ]
        },
    },
}
