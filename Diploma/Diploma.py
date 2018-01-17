import requests
import json
from urllib.parse import urlencode, urljoin


def do_request(params, method):
    URL = 'https://api.vk.com/method/'
    print('.', end=' ')
    response = requests.get(urljoin(URL, method), params)
    response.raise_for_status()
    response_json = response.json()
    if 'error' in response_json:
        print(response_json)
    if 'response' in response_json:
        return response_json['response']



def get_ids(ids, version):
    params = {
        'user_ids': ids,
        'v': version
    }
    user_id = do_request(params,'users.get')[0]['id']
    return user_id


def get_friends_list(user_id, version):
    params = {
        'user_id': user_id,
        'v': version
    }
    friends_list = do_request(params, 'friends.get')['items']
    return friends_list



def get_group_list(user_id, version, token):
    params = {
        'access_token': token,
        'user_id': user_id,
        'count': 1000,
        'v': version
    }

    group_list = do_request(params, 'groups.get')['items']
    return group_list


def response(friends_list, group, version):
    params = {
        'group_id': group,
        'user_ids': friends_list,
        'extended': 0,
        'v': version
    }
    is_member = do_request(params, 'groups.isMember')
    for member in is_member:
        if member['member']:
            return 0
        else:
            print('.', end=' ')
    if not member['member']:
        return group


def unique_group(friend_list, group, version, test=0, chunk_size=300):
    if len(friend_list) > chunk_size:
        split_friend_list = [friend_list[d:d + chunk_size] for d in range(0, len(friend_list), chunk_size)]
        for friend_list in split_friend_list:
            friends_list = ', '.join(str(friend) for friend in friend_list)
            result = response(friends_list, group, version)
            if not result:
                print()
                print('группа', group, 'не уникальна')
                return False
            else:
                test += 1
                continue
        if test != 0:
            print()
            print('группа', group, 'УНИКАЛЬНА')
            return group

    else:
        friends_list = ', '.join(str(friend) for friend in friend_list)
        result = response(friends_list, group, version)
        if not result:
            print()
            print('группа', group, 'не уникальна')
        else:
            print()
            print('группа', group, 'УНИКАЛЬНА')
            return group


def group_json(group_list, friend_list, version):
    group_list_for_json = []
    for group in group_list:
        if unique_group(friend_list, group, version):
            group_list_for_json.append(group)
        else:
            continue
    group_list_for_json = ', '.join(str(group) for group in group_list_for_json)
    params = {
        'group_ids': group_list_for_json,
        'fields': 'members_count',
        'v': version
    }
    response = requests.get('https://api.vk.com/method/groups.getById', params)
    response_json = response.json()
    groups = response_json['response']
    with open('group.json', 'w') as f:
        json.dump(groups, f, indent=2, ensure_ascii=False)


def program():
    token = '5dfd6b0dee902310df772082421968f4c06443abecbc082a8440cb18910a56daca73ac8d04b25154a1128'
    version = '5.69'
    user_id = input('Введите имя пользователя или его id: ')
    user_id = get_ids(user_id, version)
    friend_list = get_friends_list(user_id, version)
    group_list = get_group_list(user_id, version, token)
    group_json(group_list, friend_list, version)
    print('список уникальных групп в файле group.json')



# def do_request(params, method):
#     URL = 'https://api.vk.com/method/'
#     response = requests.get(urljoin(URL, method), params)
#     response.raise_for_status()
#     response_json = response.json()
#     if 'error' in response_json:
#         print(response_json)
#     if 'response' in response_json:
#         return response_json['response']





# params = {
#         'user_id': 15590964,
#         'v': '5.69'
#     }
# do_request(params,'friends.get')



program()
# config = open('config.py', 'r')
# token = config.readline()
# version = config.readline()
# print(token)
# print(version)
