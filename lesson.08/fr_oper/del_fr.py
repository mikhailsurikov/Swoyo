def my_del(friends_list, friend_name):
    if friend_name in friends_list:
        friends_list.remove(friend_name)
        print(friends_list)
        return f'{friend_name} удален'
    return f'{friend_name} нет в спике списке'