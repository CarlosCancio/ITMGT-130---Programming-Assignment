import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['cafedatabase']

#collections
product_collection = db['product']
usercred_collection = db['usercred']
branches_collection = db['branches']
ordermanagement_collection = db['ordermanagement']

def get_product(code):
    products_coll = product_collection["products"]

    product = products_coll.find_one({"code":code},{"_id":0})

    return product


def get_products():
    product_list = []

    products_coll = product_collection["products"]

    for p in products_coll.find({},{"_id":0}):
        product_list.append(p)


def get_branch(code):
    branch = branches_collection.find_one({"code": code})
    return branch

def get_branches():
    branch_list = []
    for branch in branches_collection.find():
        branch_list.append({"code": branch["code"], "name": branch["name"]})
    return branch_list

def get_user(code):
    user = usercred_collection.find_one({"email":code})
    return user


def create_order(order):
    ordermanagement_collection.insert_one(order)