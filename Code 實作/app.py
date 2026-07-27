import csv
from collections import defaultdict

def sum_csv(path):
    totals = defaultdict(float)
    with open(path,'r',encoding='utf-8',newline='') as file:
        reader = csv.DictReader(file)
        required = {'account','amount'}
        if not required.issubset(reader.filename or []):
            raise ValueError('缺少必要欄位')
        if not 
