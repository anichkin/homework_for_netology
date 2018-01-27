import requests
import json
import time
from urllib.parse import urljoin


def do_request(params, method):
    url = 'https://api.vk.com/method/'
    print('.', end=' ')
    try:
        response = requests.get(urljoin(url, method), params)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print('Oops. HTTP Error occured')
        print('Response is: {content}'.format(content=err.response.content))
        return do_request(params, method)
    response_json = response.json()
    if 'error' in response_json:
        error_code = response_json['error']['error_code']
        error_message = response_json['error']['error_msg']
        TOO_MANY_REQUESTS = 6
        ACCESS_DENIED = 15
        INVALID_USER_ID = 113
        if error_code == TOO_MANY_REQUESTS:
            print(error_message)
            time.sleep(1)
            return do_request(params, method)
        if error_code == ACCESS_DENIED or error_code == INVALID_USER_ID:
            print(error_message)
            return None
        print(error_code)
        print(error_message)
        print(method)
        return None
    return response_json['response']


def get_ids(ids, version):
    params = {
        'user_ids': ids,
        'v': version
    }
    user_id = do_request(params, 'users.get')
    if not user_id:
        return None
    return user_id[0]['id']


def get_friends_list(user_id, version):
    params = {
        'user_id': user_id,
        'v': version
    }
    friends_list = do_request(params, 'friends.get')
    if not friends_list:
        print('Доступ к пользователю запрещен')
        return None
    if len(friends_list['items']) == 0:
        print('У этого пользователя нет друзей')
        return None
    return friends_list['items']


def get_group_list(user_id, version, token):
    params = {
        'access_token': token,
        'user_id': user_id,
        'count': 1000,
        'v': version
    }
    group_list = do_request(params, 'groups.get')
    return group_list['items']


def is_member(friends_list, group, version):
    params = {
        'group_id': group,
        'user_ids': friends_list,
        'extended': 0,
        'v': version
    }
    is_member = do_request(params, 'groups.isMember')
    return is_member


def unique_group(friend_list, group, version, chunk_size=300):
    split_friend_list = [friend_list[d:d + chunk_size] for d in range(0, len(friend_list), chunk_size)]
    for friend_list in split_friend_list:
        friends_list = ', '.join(str(friend) for friend in friend_list)
        result = is_member(friends_list, group, version)
        if not result:
            return None
        for member in result:
            if member['member']:
                print('группа {} не уникальна'.format(group))
                return None
    print('группа {} УНИКАЛЬНА'.format(group))
    return group


def group_json(group_list, friend_list, version):
    json_group = []
    group_list_for_json = []
    for group in group_list:
        if unique_group(friend_list, group, version):
            group_list_for_json.append(group)
    if len(group_list_for_json) == 0:
        print('У этого пользователя нет уникальных групп')
        return None
    group_list_for_json = ', '.join(str(group) for group in group_list_for_json)
    params = {
        'group_ids': group_list_for_json,
        'fields': 'members_count',
        'extended': 1,
        'v': version
    }
    groups = do_request(params, 'groups.getById')
    for group in groups:
        group_param = {}
        group_param['name'] = group['name']
        group_param['id'] = group['id']
        group_param['members_count'] = group['members_count']
        json_group.append(group_param)
    with open('group.json', 'w', encoding='UTF-8') as f:
        json.dump(json_group, f, indent=2, ensure_ascii=False)
        print('список уникальных групп в файле group.json')
        exit()


def program():
    file = open('config.json', 'r')
    config = json.load(file)
    token = config['token']
    version = config['version']
    user_id = input('Введите имя пользователя или его id: ')
    user_id = get_ids(user_id, version)
    if not user_id:
        print('нет такого пользователя, введите заново')
        program()
    friend_list = get_friends_list(user_id, version)
    if not friend_list:
        program()
    group_list = get_group_list(user_id, version, token)
    if len(group_list) == 0:
        print('у этого пользователя нет групп')
        program()
    group_list_for_json = group_json(group_list, friend_list, version)
    if not group_list_for_json:
        program()


program()
