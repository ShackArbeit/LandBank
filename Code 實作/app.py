def parse_rows(lines):
    valid = []
    errors = []
    for line_no, line in enumerate(lines, start=1):
        print('No:',line_no)
        print('Line:',line)
        parts = [part.strip() for part in line.split(',')]
        print('Parts:',parts)
        if len(parts) != 2:
            errors.append('第{}行：欄位數錯誤'.format(line_no))
            continue
        account, raw_amount = parts
        if not account:
            errors.append('第{}行：帳戶為空'.format(line_no))
            continue
        try:
            amount = float(raw_amount)
        except ValueError:
            errors.append('第{}行：金額錯誤'.format(line_no))
            continue
        valid.append((account, amount))
    return valid, errors

test_lines = [
    "user1, 500.5",       # 1. 正常資料 (前後有空白)
    "user2",              # 2. 欄位數錯誤 (缺少逗號)
    "user3, 100, 備註",   # 3. 欄位數錯誤 (逗號太多)
    " , 200",             # 4. 帳戶為空 (只有空白)
    "user4, abc",         # 5. 金額錯誤 (含有英文)
    "user5, 100元",       # 6. 金額錯誤 (含有中文單位)
    "user6, -50"          # 7. 正常資料 (負數也是合法浮點數)
]
result = parse_rows(test_lines)
print('Result:',result)