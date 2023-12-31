import datetime
import time
import json
import markdown

d = {'eyes': {'amount': 4, 'user': 'UTDCLSCBX'}, 'white_check_mark': {'amount': 6, 'user': 'UTDCLSCBX'}}

mrkstring = '''
Rank  Name  Score
'''

import operator

# Create a dictionary
dict = {'clap': {'amount': 2, 'user': 'UTDCLSCBX', 'reaction': 'clap'},
        'raised_hands': {'amount': 2, 'user': 'UTDCLSCBX', 'reaction': 'raised_hands'},
        'eyes': {'amount': 4, 'user': 'UTDCLSCBX', 'reaction': 'eyes'},
        'white_check_mark': {'amount': 6, 'user': 'UTDCLSCBX', 'reaction': 'white_check_mark'}}

# Get the amount of each emoji
amounts = dict.values()

# Sort the amounts in descending order
sorted_amounts = sorted(amounts, key=operator.itemgetter('amount'), reverse=True)

# Print the sorted amounts
print(sorted_amounts)

# separated_reactions_count_dict = {}
# with open("json_data.json", 'r') as json_file:
#     data = json.loads(json_file.read())
#     messages = data['messages']
#
#     for react in messages:
#         try:
#             # print(react['reactions'])
#             if react['reactions'][0]['name'] not in separated_reactions_count_dict:
#                 separated_reactions_count_dict[react['reactions'][0]['name']] = 1
#
#             if react['reactions'][0]['name'] in separated_reactions_count_dict:
#                 separated_reactions_count_dict[react['reactions'][0]['name']] = separated_reactions_count_dict[
#                                                                                     react['reactions'][0]['name']] + 1
#
#         except Exception as e:
#             pass
# print(separated_reactions_count_dict)
# today_date_time = datetime.datetime.today()
# print("first day Date:", today_date_time.day - today_date_time.day + 1)
#
# latest_date_time = time.mktime(today_date_time.timetuple())
# print("latest UNIX timestamp:", latest_date_time)
#
# oldest_date_time = datetime.datetime(year=today_date_time.year, month=today_date_time.month,
#                                      day=today_date_time.day - today_date_time.day + 1, hour=0, minute=1, second=1)
# oldest_date_unix_time = time.mktime(oldest_date_time.timetuple())
# print("oldest UNIX timestamp:", oldest_date_unix_time)

# data = {'eyes': 56, 'white_check_mark': 8}
#
# data_list = [f':{key}: :{value}' for key, value in data.items()]
# print(data_list)
# # for key, value in data.items():
# #     print("".join(f'{key}: {value}', end=" "))
#
# print(" ".join(data_list))
# sorted_list = sorted(data.items(), key=lambda x: x[1], reverse=True)
# print(sorted_list)
