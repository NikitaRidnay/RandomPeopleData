from faker import Faker

Data = Faker('ru_RU')

count = int(input('Сколько людей сгенерировать? '))
filename = input('Введите имя файла для сохранения данных: ')

with open(filename, 'a') as f:
    for i in range(count):
        f.write('-\n')
        f.write(Data.name() + '\n')
        f.write(Data.phone_number() + '\n')
        f.write(Data.email() + '\n')
        f.write(Data.address() + '\n')
        f.write(Data.job() + '\n')
        f.write(str(Data.date_between(start_date='-60y', end_date='-16y')) + '\n')
        f.write('Карта:')
        f.write('Number:\n')
        f.write(Data.credit_card_number()+'\n')
        f.write('Date:\n')
        f.write(Data.credit_card_expire()+'\n')
        f.write('CVV\n')
        f.write(Data.credit_card_security_code()+'\n')
        f.write('-\n')