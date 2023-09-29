def get_revenue(n: int, m: int, x: int) -> int:
    """Функция возвращает сумму, которую строительная компания сможет получить от продажи квартир.
    n - количество этажей;
    m - через сколько этажей цена возрастёт на $1000;
    x - цена квартиры на 1 этаже.
    """
    total = 0
    count = 0
    for i in range(n):
        total += x
        count += 1
        if count == m:
            x += 1000
            count = 0
    return total


n = 30
m = 10
x = 10000

print(get_revenue(n, m, x)) # 330000
