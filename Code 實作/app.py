def process_queue(items):
    queue_list = list(items)
    result = []
    front_index = 0 
    while front_index<len(queue_list):
        current = queue_list[front_index]
        result.append(current)
        front_index +=1
    return result 

items =list(range(2000))
result = process_queue(items)
print(result)