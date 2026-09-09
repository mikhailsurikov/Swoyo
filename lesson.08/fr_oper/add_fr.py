def my_add(friends_list, friend_name):
    if friend_name not in friends_list:
        friends_list.append(friend_name)
        print(friends_list)
        return f'{friend_name} добавлен'
    return f'{friend_name} уже в списке'
