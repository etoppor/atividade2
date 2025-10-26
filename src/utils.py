def calculate_cart_total(items, discount=0.0, tax_rate=0.0):
    if not isinstance(items, list):
        raise TypeError("items deve ser uma lista")
    subtotal = 0.0
    for it in items:
        if it['price'] < 0 or it['qty'] < 0:
            raise ValueError("Valores não podem ser negativos")
        subtotal += it['price'] * it['qty']
    if not (0 <= discount < 1.0):
        raise ValueError("Desconto deve estar entre 0 e 1")
    if not (0 <= tax_rate < 1.0):
        raise ValueError("Taxa deve estar entre 0 e 1")
    total = subtotal * (1 - discount)
    total *= (1 + tax_rate)
    return round(total, 2)
