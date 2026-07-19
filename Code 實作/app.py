def clean_taske(tasks):
    result=[]
    for task in tasks:
        cleaned = str(task).strip()
        if cleaned:
            result.append(cleaned)
    return result 
raw_tasks = ["  買牛奶 ", "", "修電腦\n", "   ", "去銀行轉帳", "  "]
result= clean_taske(raw_tasks)
print('Result:',result)
