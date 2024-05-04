list_=['kiwi','banana','apple','orange','peach']
my_list=list_
print('List: ',my_list)
print('First element: ',list_[0])
print('Last element: ',list_[-1])
print('Sublist: ',list_[2:5])
list_[2]='яблоко'
print('Modified list: ',list_)
print()
my_dict={}
my_dict['kiwi']='киви'
my_dict['banana']='банан'
my_dict['apple']='яблоко'
my_dict['orange']='апельсин'
my_dict['peach']='персик'
print('Dictionary: ',my_dict)
print('Translation: ',my_dict['banana'])
my_dict['orange']='АРБУЗ'
my_dict['grape']='виноград'
print('Modified dictionary: ',my_dict)
