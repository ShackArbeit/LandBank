def risk_band(amount):
    if amount < 0:
        return ValueError('金額不可小於0')
    if amount < 10000:
        return 'Low'
    if 10000<amount<100000:
        return 'Medium'
    else:
        return 'Heigh'

result = risk_band(4444)
print(result)