
product_list = [
       {
           "type": "1",
           "name": "shirt",
           "price": 30,
           "unit": "Dollar",
           "commission_groups": ["A", "B"]
       },
       {
           "type": "2",
           "name": "pants",
           "price": 50,
           "unit": "Dollar",
           "commission_groups": ["A", "C"]
       },
       {
           "type": "3",
           "name": "shoes",
           "price": 80,
           "unit": "Dollar",
           "commission_groups": ["B"]
       },
       {
           "type": "4",
           "name": "hat",
           "price": 20,
           "unit": "Dollar",
           "commission_groups": []
       }
]

markup_list = [
    {
        "product_type": "1",
        "lower_cost": 10,
        "upper_cost": 20,
        "unit": "percent",
        "lower_count": 10
    },
    {
        "product_type": "2",
        "lower_cost": 15,
        "upper_cost": 20,
        "unit": "percent",
        "lower_count": 10
    },
    {
        "product_type": "3",
        "lower_cost": 10,
        "upper_cost": 15,
        "unit": "percent",
        "lower_count": 5
    },
    {
        "product_type": "4",
        "lower_cost": 10,
        "upper_cost": 30,
        "unit": "percent",
        "lower_count": 20
    },
]

commission_list = [
    {
        "group_name": "A",
        "cost": 5,
        "unit": "percent",
        "users": [1001, 1002, 1003, 1005]
    },
    {
        "group_name": "B",
        "cost": 3,
        "unit": "Dollar",
        "users": [1001, 1003, 1006]
    },
    {
        "group_name": "C",
        "cost": 7,
        "unit": "percent",
        "users": [1001, 1002, 1004]
    }
]


user_list = [
    {
        "userid": 1001,
        "first_name": "Mohsen",
        "last_name": "Bayat",
    },
    {
        "userid": 1002,
        "first_name": "Sobhan",
        "last_name": "Taghadosi",
    },
    {
        "userid": 1003,
        "first_name": "Javad",
        "last_name": "Jafari",
    },
    {
        "userid": 1004,
        "first_name": "Masoud",
        "last_name": "Hosseini",
    },
    {
        "userid": 1005,
        "first_name": "Hassan",
        "last_name": "Zand",
    },
    {
        "userid": 1006,
        "first_name": "Ali",
        "last_name": "Ebadi",
    }
]
typ = input('enter yr type of product:')
cunt = int(input('enter yr count of product:'))
userid = int(input())

def markup_pro(typ,cunt):
    markup = ''
    for i in range(len(markup_list)):
        prd_typ = markup_list[i]["product_type"]
        low_cost = markup_list[i]["lower_cost"]
        low_count = markup_list[i]["lower_count"]
        upe_cost = markup_list[i]["upper_cost"]
        if typ == prd_typ:
            if cunt >= low_count:
                markup = low_cost
            elif cunt < low_count and cunt > 1:
                x = (1 / low_count)
                markup = upe_cost - x

            return markup
def calc_prod_price(typ):
    for i in range(len(product_list)):
        type_prod = product_list[i]["type"]
        prod_name = product_list[i]["name"]
        price = product_list[i]["price"]
        commi = product_list[i]["commission_groups"]
        if typ == type_prod:
            price = (price * markup_pro(typ, cunt) / 100) + price
            return price, commi, prod_name
pri, comii , product_name = calc_prod_price(typ)
pri = int(pri)
def commiss_prod(pri,comii):
    for i in range(len(commission_list)):
        group = commission_list[i]["group_name"]
        perc_reduce = commission_list[i]["cost"]
        user = commission_list[i]["users"]
        for j in range(len(comii)):
            if comii[j] == group :
                price_by_commi = abs((pri * perc_reduce / 100) - pri)
            return price_by_commi, user
pri_commi, useeer = commiss_prod(pri, comii)
pri_commi = int(pri_commi)
def user_commi(userid):
    for i in range(len(user_list)):
        use = user_list[i]["userid"]
        first_name = user_list[i]["first_name"]
        last_name = user_list[i]["last_name"]
        for j in range(len(useeer)):
            if useeer[j] == use :
                return first_name, last_name
firstname, lastname = user_commi(userid)
dict = {"product_name" : product_name,
"total_price" : pri,
"total_with_commision" : pri_commi,
"discount" : pri - pri_commi,
"username" : {"first_name" : firstname,
              "last_name" : lastname}}
print(dict)