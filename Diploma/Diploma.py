import requests
import time

TOKEN = '5dfd6b0dee902310df772082421968f4c06443abecbc082a8440cb18910a56daca73ac8d04b25154a1128'
VERSION = '5.69'


#



def get_ids(ids, VERSION):
    params = {
        'user_ids': ids,
        'v': VERSION
    }

    response = requests.get('https://api.vk.com/method/users.get', params)
    response_json = response.json()
    id = response_json['response'][0]['id']
    return id


print(get_ids('papapapokerface', VERSION))


def get_friends_list(friend_id, VERSION):
    friend_params = {
        'user_id': friend_id,
        'v': VERSION
    }

    response_friend = requests.get('https://api.vk.com/method/friends.get', friend_params)
    response_friend_json = response_friend.json()
    if 'response' in response_friend_json.keys():
        friend_list = response_friend_json['response']['items']
        return friend_list


def get_group_list(friend_id, VERSION):
    group_params = {
        'access_token': TOKEN,
        'user_id': friend_id,
        'count': 1000,
        'v': VERSION
    }

    response_group = requests.get('https://api.vk.com/method/groups.get', group_params)
    response_group_json = response_group.json()
    group_list = response_group_json['response']['items']
    return group_list


def unique_group(friend_list, group, VERSION):
    for friend in friend_list:
        params = {
            'group_id': group,
            'user_id': 1,
            'user_ids': friend,
            'extended': 1,
            'v': VERSION
        }
        response = requests.get('https://api.vk.com/method/groups.isMember', params)
        response_json = response.json()
        is_member = response_json['response'][0]['member']
        if is_member:
            print('группа', group, 'не уникальна')
            break
        else:
            print('.', end=' ')
    if not is_member:
        print('группа уникальна!!!')
        return group


friend_list = get_friends_list(get_ids('papapapokerface', VERSION), VERSION)
group_list = get_group_list('15590964', VERSION)
print(group_list)
print(str(friend_list))


def response(friends_list):
    params = {
        'group_id': group,
        'user_ids': friends_list,
        'extended': 0,
        'v': VERSION
    }
    response = requests.get('https://api.vk.com/method/groups.isMember', params)
    response_json = response.json()
    if 'response' in response_json.keys():
        for member in response_json['response']:
            if member['member']:
                return 0
            else:
                print('.', end=' ')
        if not member['member']:
            return group


def unique_group2(friend_list, group, VERSION):
    if len(friend_list) > 300:
        split_friend_list = [friend_list[d:d + 300] for d in range(0, len(friend_list), 300)]
        for list in split_friend_list:
            t = 0
            friends_list = ((str(list)).replace('[', "'")).replace(']', "'")
            result = response(friends_list)
            if not result:
                t == 0
                print('группа', group, 'не уникальна')
                break
            else:
                t += 1
        if t != 0:
            print('группа уникальна', group)
            return group


    else:
        friends_list = ((str(friend_list)).replace('[', "'")).replace(']', "'")
        result = response(friends_list)
        if not result:
            print('группа', group, 'не уникальна')
        else:
            print('группа уникальна', group)
            return group

listtt = []
for group in group_list:
    if unique_group2(friend_list, group, VERSION):
        listtt.append(unique_group2(friend_list, group, VERSION))
print(listtt)
listt = ((str(listtt)).replace('[', "'")).replace(']', "'")
params = {
        'group_ids': listt,
        'fields': 'members_count',
        'v': VERSION
    }
response = requests.get('https://api.vk.com/method/groups.getById', params)
response_json = response.json()
print(response_json)










fried_list = get_friends_list(get_ids('papapapokerface', VERSION), VERSION)
group_list = get_group_list('15590964', VERSION)
print(str(fried_list))
frienssss = ((str(fried_list)).replace('[', "'")).replace(']', "'")
print(frienssss)

# print(group_list)
# for group in group_list:
#     unique_group(fried_list, group, VERSION)

params = {
    'group_id': 31480508,
    'user_ids': frienssss,
    'extended': 0,
    'v': VERSION
}
response = requests.get('https://api.vk.com/method/groups.isMember', params)
response_json = response.json()
print(response_json['response'])
