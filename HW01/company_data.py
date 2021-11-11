'''
#Question 4                           
***     حل مسئله در انتهای فایل      ***
                            
'''


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


#part1
def Calculate_markup_percent( p , Quantity):
    if n < markup_list[p-1]["lower_count"]:
        return  markup_list[p-1]["upper_cost"]-((Quantity-1)*(markup_list[p-1]["upper_cost"] - markup_list[p-1]["lower_cost"])/(markup_list[p-1]["lower_count"]))
    else:
        return markup_list[p-1]["lower_cost"]

p = int(input("Enter product type:"))
n = int(input("Enter quantity:"))
print(f' Markup is {Calculate_markup_percent(p, n)}%')


#part2
def Calculate_product_price(product_type, count, userid):
    output = {}
    dscount = {}
    output['pruduct name'] = product_list[product_type-1]["name"]
    output['total price'] = product_list[product_type-1]["price"] * (1 + Calculate_markup_percent(product_type, count)/100)
    
    for i  in range(len(commission_list)):
        if userid in commission_list[i]["users"]:
            #dscount[userid] = [commission_list[i]["group_name"],commission_list[i]["cost"],commission_list[i]["unit"]]
            if commission_list[i]["unit"] == "Dollar":
                dscount[commission_list[i]["cost"]] = [commission_list[i]["group_name"] , commission_list[i]["cost"], commission_list[i]["unit"]]
            else:
                dscount[output['total price']*commission_list[i]["cost"]/100] = [commission_list[i]["group_name"] , commission_list[i]["cost"], commission_list[i]["unit"]]
    
    if len(dscount) > 0 :
        output['total with commission'] = output['total price'] - max(dscount)
        output['u_discount'] = f' group {dscount[max(dscount)][0]}, {dscount[max(dscount)][1]}{dscount[max(dscount)][2]}'
    else:
        output['total with commission'] = "No commission"
        output['u_discount'] = "Zero"

    for j  in range(len(user_list)):
        if user_list[j]["userid"] == userid:
            output['username'] = { 'first name' : user_list[j]["first_name"], 'last name' : user_list[j]["last_name"] }
            break
        else:
            output['username'] = { 'first name' : 'NA', 'last name' : 'NA' }
    
    return output
    return dscount

from pprint import pprint
p2 = int(input("Enter product type:"))
n2 = int(input("Enter quantity:"))
u = int(input("Enter user ID:"))
pprint(Calculate_product_price(p2, n2, u))

