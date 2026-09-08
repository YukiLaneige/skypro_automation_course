from smartphone import Smartphone

catalog = [Smartphone('Apple', 'iPhone 15', '88005553535'),
           Smartphone('Samsung', 'Galaxy S24', '88001001001'),
           Smartphone('Xiaomi', 'Redmi Note 13', '88002006040'),
           ]
for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}")
