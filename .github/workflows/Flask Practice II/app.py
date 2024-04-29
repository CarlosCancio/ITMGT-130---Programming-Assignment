from flask import Flask, render_template, request, redirect, session
import database as db
import authentication
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)
app.logger.setLevel(logging.INFO)
app.secret_key = b's@g@d@c0ff33!'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products')
def products():
    product_list = db.get_products()
    return render_template('products.html', product_list=product_list)

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/productdetails')
def productdetails():
    code = request.args.get('code', '')
    product = db.get_product(int(code))
    quantity = request.args.get('qty', '')  # Get quantity parameter
    return render_template('productdetails.html', product=product, quantity=quantity)

@app.route('/branches')
def branches():
    branch_list = db.get_branches()
    return render_template('branches.html', branch_list=branch_list)

@app.route('/branchdetails')
def branchdetails():
    code = request.args.get('code', '')
    branch = db.get_branch(int(code))
    return render_template('branchdetails.html', branch=branch)

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop("user",None)
    session.pop("cart",None)
    return redirect('/')

@app.route('/auth', methods = ['GET', 'POST'])
def auth():
    username = request.form.get('username')
    password = request.form.get('password')

    if not username or not password:
        error_message = "Incomplete login data. Please provide both username and password."
        return render_template('login.html', error_message=error_message)

    is_successful, user = authentication.login(username, password)
    if is_successful:
        session["user"] = user
        return redirect('/')
    else:
        error_message = "Invalid username or password. Please try again."
        return render_template('login.html', error_message=error_message)

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/addtocart', methods=['POST'])
def addtocart():
    code = request.args.get('code', '')
    product = db.get_product(int(code))
    
    if product:
        if "cart" not in session:
            session["cart"] = {}
            session["total_subtotal"] = 0

        cart = session["cart"]
        total_subtotal = session.get("total_subtotal", 0)

        # Retrieve quantity from the form submission
        qty = int(request.form.get('qty', 1))  # Default to 1 if quantity is not specified
        
        if code in cart:
            # If the product is already in the cart, increment its quantity
            cart[code]["qty"] += qty
        else:
            # If the product is not in the cart, add it with specified quantity
            item = {
                "qty": qty,
                "name": product["name"],
                "price": product.get("price", 0),  # Ensure price field exists in product dict
                "subtotal": product.get("price", 0) * qty  # Calculate subtotal based on quantity
            }
            cart[code] = item
        
        # Update subtotal for the added item
        cart[code]["subtotal"] = cart[code]["qty"] * cart[code].get("price", 0)
        
        # Update total subtotal by summing up the subtotal of all items in the cart
        session["total_subtotal"] = sum(item["subtotal"] for item in cart.values())

        session["cart"] = cart
        return redirect('/cart')
    else:
        # Handle the case where the product is not found
        return "Product not found."
    code = request.args.get('code', '')
    product = db.get_product(int(code))
    
    if product:
        if "cart" not in session:
            session["cart"] = {}
            session["total_subtotal"] = 0

        cart = session["cart"]
        total_subtotal = session.get("total_subtotal", 0)

        # Retrieve quantity from the form submission
        qty = int(request.form.get('qty', 1))  # Default to 1 if quantity is not specified
        
        if code in cart:
            # If the product is already in the cart, increment its quantity
            cart[code]["qty"] += qty
        else:
            # If the product is not in the cart, add it with specified quantity
            item = {
                "qty": qty,
                "name": product["name"],
                "price": product.get("price", 0),  # Ensure price field exists in product dict
                "subtotal": product.get("price", 0) * qty  # Calculate subtotal based on quantity
            }
            cart[code] = item
        
        # Update subtotal for the added item
        cart[code]["subtotal"] = cart[code]["qty"] * cart[code].get("price", 0)
        
        # Update total subtotal by summing up the subtotal of all items in the cart
        session["total_subtotal"] = sum(item["subtotal"] for item in cart.values())

        session["cart"] = cart
        return redirect('/cart')
    else:
        # Handle the case where the product is not found
        return "Product not found."

@app.route('/removeitem/<int:code>')
def remove_item(code):
    if "cart" in session:
        cart = session["cart"]
        if str(code) in cart:  # Convert code to string for dictionary lookup
            # Decrease quantity by 1
            cart[str(code)]["qty"] -= 1
            # If quantity becomes 0, remove the item from the cart
            if cart[str(code)]["qty"] == 0:
                del cart[str(code)]
            # Update total subtotal
            session["total_subtotal"] = sum(item["subtotal"] for item in cart.values())
            session["cart"] = cart
    return redirect('/cart')

if __name__ == "__main__":
    app.run(debug=True)