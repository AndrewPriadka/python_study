class Convert:

    def __init__(self, currency_dict):
        self.currency_dict = currency_dict

    def converter(self):

        print('возможные валюты: UAH, USD, EUR, RUB, GBR')
        first_currency = str(input('Введите валюту: \n'))
        money = input('Введите сумму:\n')
        needed_currency = input('В какой валюте получить результат?\n')
        self.exchange(first_currency, money, needed_currency)

    def exchange(self, first_currency, money, needed_currency):
        out = None
        try:
            out = self.currency_dict[first_currency] * int(money) / self.currency_dict[needed_currency]
        except KeyError:
            print("Вы ввели несуществующую валюту")
        except ValueError:
            print("сумму нужно вводить числом")
        if out:
            print(money, first_currency, '=', out, needed_currency)


currency_dicti = {'UAH': 1, 'USD': 26.02, 'EUR': 30.57, 'RUB': 0.4, 'GBR': 34}
Convert(currency_dicti).converter()
