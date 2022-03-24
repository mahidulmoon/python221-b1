# storage = []

# while len(storage) < 10 :
#     userInput = input("Please Enter a Number : ")
#     storage.append(userInput)

# storage.reverse()

# if len(storage) == 10:
#     print("============================\n")
#     for index in range(len(storage)):
#         print(str(10-index),"th entry is :"if 10-index > 3 else ("nd entry is :" if 10-index == 2 else ("st entry is :"if 10-index == 1 else"rd entry is :")),storage[index])



# # print("x") if condition else print("y")


# number_of_int = [x for x in range(20,0,-1) ]
# number_of_int = [100, 50, 65, 82, 23]

# # for value in range(1,21):
# #   if x%2 == 0:
# #     number_of_int.append(value)
# # number_of_int.sort()
# number_of_int.sort(reverse=True)
# print("Data : ",number_of_int)


# variable_tuple = (100, 50, 65, 82, 23)
# variable_tuple = list(variable_tuple)
# print(variable_tuple)
# variable_tuple[2] = 219
# variable_tuple = tuple(variable_tuple)
# print(variable_tuple)



# ext = {"a","b","cherry"}
# variable_set = {"banana", "cherry", "apple"}
# variable_set.add("mahidul")
# variable_set.update(ext)

# print(variable_set.union(ext))

# variable_dict = {
#     'color' : 'green',
#     'number' : 10,
#     1: "abc",
#     'list' : [1,2,3,4,5,6],
# }

# # print(variable_dict['list'])

# # for key,value in variable_dict.items():
# #     print("++++++++++",value)

# variable_dict['color'] = "red"
# # variable_dict['name'] = "mahidul"
# variable_dict.update({'name' : "mahidul","lastname" : "islam"})
# # variable_dict.pop('color')
# variable_dict.popitem()
# print(variable_dict)

final_answer = {
    "name" : {
        "firstname" : "mahidul",
        "lastname" : "islam"
    },
    "address" : {
        "road" : 6,
        "location" : {
            "area" : "mirpur",
            "block" : "C"
        }
    },
    "education" : "bsc",
    "age" : 24
}
print(final_answer['address']['location']['area'])
