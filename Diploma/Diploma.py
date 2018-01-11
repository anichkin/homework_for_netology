import requests
import json


def get_ids(ids, VERSION):
    params = {
        'user_ids': ids,
        'v': VERSION
    }

    response = requests.get('https://api.vk.com/method/users.get', params)
    response_json = response.json()
    user_id = response_json['response'][0]['id']
    return user_id


def get_friends_list(user_id, VERSION):
    friend_params = {
        'user_id': user_id,
        'v': VERSION
    }

    response_friend = requests.get('https://api.vk.com/method/friends.get', friend_params)
    response_friend_json = response_friend.json()
    if 'response' in response_friend_json.keys():
        friend_list = response_friend_json['response']['items']
        return friend_list


def get_group_list(user_id, VERSION, TOKEN):
    group_params = {
        'access_token': TOKEN,
        'user_id': user_id,
        'count': 1000,
        'v': VERSION
    }

    response_group = requests.get('https://api.vk.com/method/groups.get', group_params)
    response_group_json = response_group.json()
    group_list = response_group_json['response']['items']
    return group_list



def response(friends_list, group, VERSION):
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


def unique_group(friend_list, group, VERSION):
    if len(friend_list) > 300:
        split_friend_list = [friend_list[d:d + 300] for d in range(0, len(friend_list), 300)]
        for list in split_friend_list:
            t = 0
            friends_list = ((str(list)).replace('[', "'")).replace(']', "'")
            result = response(friends_list, group, VERSION)
            if not result:
                t == 0
                print()
                print('группа', group, 'не уникальна')
                break
            else:
                t += 1
        if t != 0:
            print()
            print('группа УНИКАЛЬНА', group)
            return group


    else:
        friends_list = ((str(friend_list)).replace('[', "'")).replace(']', "'")
        result = response(friends_list, group, VERSION)
        if not result:
            print()
            print('группа', group, 'не уникальна')
        else:
            print()
            print('группа УНИКАЛЬНА', group)
            return group


def group_json(group_list, friend_list, VERSION):
    group_list_for_json = []
    for group in group_list:
        if unique_group(friend_list, group, VERSION):
            group_list_for_json.append(unique_group(friend_list, group, VERSION))
    group_list_for_json = ((str(group_list_for_json)).replace('[', "'")).replace(']', "'")
    params = {
            'group_ids': group_list_for_json,
            'fields': 'members_count',
            'v': VERSION
        }
    response = requests.get('https://api.vk.com/method/groups.getById', params)
    response_json = response.json()
    groups = response_json['response']
    print(groups)
    with open('group.json', 'w', encoding='utf-8') as f:
        json.dump(groups, f, indent=2, ensure_ascii=False)

def program():
    TOKEN = '5dfd6b0dee902310df772082421968f4c06443abecbc082a8440cb18910a56daca73ac8d04b25154a1128'
    VERSION = '5.69'
    user_id = input('Введите имя пользователя или его id')
    user_id = get_ids(user_id, VERSION)
    print(get_ids(user_id, VERSION))
    friend_list = get_friends_list(user_id, VERSION)
    print(friend_list)
    group_list = get_group_list(user_id, VERSION, TOKEN)
    print(group_list)
    group_json(group_list, friend_list, VERSION)


program()