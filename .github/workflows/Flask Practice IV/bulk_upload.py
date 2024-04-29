import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['cafedatabase']

# Collections
product_collection = db['product']
usercred_collection = db['usercred']
branches_collection = db['branches']
ordermanagement_collection = db['ordermanagement']

products = {
    100: {"name": "Americano", "price": 125},
    200: {"name": "Brewed Coffee", "price": 100},
    300: {"name": "Cappuccino", "price": 120},
    400: {"name": "Espresso", "price": 120},
    1000: {"name": "Tiramisu", "price": 150},
    1100: {"name": "Red Velvet", "price": 130},
    1200: {"name": "Mango Cream Pie", "price": 200}
}

branches = {
    1: {"name": "Katipunan", "phonenumber": "09179990000"},
    2: {"name": "Tomas Morato", "phonenumber": "09179990001"},
    3: {"name": "Eastwood", "phonenumber": "09179990002"},
    4: {"name": "Tiendesitas", "phonenumber": "09179990003"},
    5: {"name": "Arcovia", "phonenumber": "09179990004"}
}

users = {
    "chums@example.com": {"password": "Ch@ng3m3!",
                          "first_name": "Matthew",
                          "last_name": "Uy"},
    "joben@example.com": {"password": "Ch@ng3m3!",
                          "first_name": "Joben",
                          "last_name": "Ilagan"},
    "bong@example.com": {"password": "Ch@ng3m3!",
                         "first_name": "Bong",
                         "last_name": "Olpoc"},
    "joaqs@example.com": {"password": "Ch@ng3m3!",
                          "first_name": "Joaqs",
                          "last_name": "Gonzales"},
    "gihoe@example.com": {"password": "Ch@ng3m3!",
                          "first_name": "Gio",
                          "last_name": "Hernandez"},
    "vic@example.com": {"password": "Ch@ng3m3!",
                        "first_name": "Vic",
                        "last_name": "Reventar"},
    "joe@example.com": {"password": "Ch@ng3m3!",
                        "first_name": "Joe",
                        "last_name": "Ilagan"},
}

def bulk_upload_products():
    for code, product_info in products.items():
        product_collection.insert_one({"code": code, "name": product_info["name"], "price": product_info["price"]})

def bulk_upload_branches():
    for branch_id, branch_info in branches.items():
        branches_collection.insert_one({"code": branch_id, "name": branch_info["name"], "phonenumber": branch_info["phonenumber"]})

def bulk_upload_users():
    for email, user_info in users.items():
        usercred_collection.insert_one({"email": email, "password": user_info["password"], "first_name": user_info["first_name"], "last_name": user_info["last_name"]})

if __name__ == "__main__":
    bulk_upload_products()
    bulk_upload_branches()
    bulk_upload_users()