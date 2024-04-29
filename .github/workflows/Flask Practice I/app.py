from flask import Flask, render_template, request
import database as db

app = Flask(__name__)

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
    return render_template('productdetails.html', product=product)

@app.route('/branches')
def branches():
    branch_list = db.get_branches()
    return render_template('branches.html', branch_list=branch_list)

@app.route('/branchdetails')
def branchdetails():
    code = request.args.get('code', '')
    branch = db.get_branch(int(code))
    return render_template('branchdetails.html', branch=branch)

if __name__ == "__main__":
    app.run(debug=True)