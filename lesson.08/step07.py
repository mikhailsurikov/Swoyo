import fr_oper.add_fr as fr_a
import fr_oper.del_fr as fr_d


friends_list = ["Bob", "Anna"]
print(fr_a.my_add(friends_list, "Mary"))
print(fr_d.my_del(friends_list, "Bob"))