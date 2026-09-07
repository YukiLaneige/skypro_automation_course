month = 12


def month_to_season(month):
    if month == 12 or 1 <= month <= 2:
        return "Зима"
    if 3 <= month <= 5:
        return "Весна"
    if 6 <= month <= 8:
        return "Лето"
    if 9 <= month <= 11:
        return "Осень"


print(month_to_season(month))
