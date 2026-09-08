from address import Address
from mailing import Mailing

to_address = Address('644000', 'Омск', 'Чокана Валиханова', '40', '13')
from_address = Address('101000', 'Москвабад', 'Последний переулок', '28', '10')


mailing = Mailing(to_address, from_address, '2000', 'RU123456789RU')

print(mailing)
