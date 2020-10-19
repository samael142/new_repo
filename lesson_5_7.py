import json

json_list = []
dict_firm = {}
average_profit = 0
profit_counter = 0
profit = 0
with open('lesson_5_7.txt', 'r', encoding='UTF-8') as f_obj:
    for line in f_obj:
        profit = int(line.split()[2]) - int(line.split()[3])
        dict_firm[line.split()[0]] = profit
        if profit > 0:
            profit_counter += 1
            average_profit += profit
json_list = [dict_firm, {'average_profit': int(average_profit / profit_counter)}]
with open('lesson_5_7_out.json', 'w') as write_f:
    json.dump(json_list, write_f)
