#list slicing will create new copy of list
#list reference to other list will change original list also

cart = ['glue', 'rubber', 'pencil', 'sharpner']

cart_ref = cart # modification/updation in cart_ref will reflect in cart
cart_not_ref = cart[:] #slicing will create new list for cart_not_ref hence update do not affect original cart
#'OR'
cart_not_ref_2 = cart.copy()
#append, extend, insert method for list
#pop, remove methods to remove element based on index and based on values respectively
#clear method
#index method to search an element in index
#list.count(element) -> shows how many time element occurs in list
#list.sort() -> do inplace sorting doesn't return anything
#sorted(list) -> return new sorted list
#reverse() -> to print reverse list


print('glue' in cart)
print(list(range(5,20)))
sentence = ['HI,','My','Name','is','Sumeet']
new_sentence = ' '.join(sentence)
print(new_sentence)

#list unpacking
a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(other)
print(d)
