import os

from werkzeug.utils import secure_filename, redirect

import ar_master

from flask import Flask, render_template, request, session, Response, current_app, send_from_directory


app = Flask(__name__, static_folder='static',template_folder='templates',static_url_path='/static')
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

mm = ar_master.master_flask_code('python_bidding_system')



@app.route("/")
def homepage():
    return render_template('index.html')
@app.route("/admin")
def admin():
    return render_template('admin.html')
@app.route("/admin_home")
def admin_home():
    return render_template('admin_home.html')

@app.route("/user_home")
def user_home():
    return render_template('user_home.html')
@app.route("/retailer_home")
def retailer_home():
    return render_template('retailer_home.html')



@app.route("/admin_login", methods = ['GET', 'POST'])
def admin_login():
    error = None
    if request.method == 'POST':
        if request.form['uname'] == 'admin' and request.form['pass'] == 'admin':
            return render_template('admin_home.html',error=error)
        else:
            return render_template('admin.html', error=error)
@app.route("/user")
def user():
    return render_template('user.html')

@app.route("/user_login",methods = ['GET', 'POST'])
def user_login():
    msg=None
    if request.method == 'POST':
        n = request.form['uname']
        g = request.form['pass']
        n1=str(n)
        g1=str(g)
        print(n1)
        print(g1)
        q = "SELECT * from customer_details where username='" + str(n1) + "' and password='" + str(g1) + "'"
        data = mm.select_login(q)
        print(q)
        data=len(data)
        if data==0:

            return render_template('user_login.html',flash_message=True,data="Failed")
        else:

            msg='Success'
            session['user'] =n

            return render_template('user_home.html',sid=n)
    return render_template('user_login.html',error=msg)
@app.route("/bank_login",methods = ['GET', 'POST'])
def bank_login():
    msg=None
    if request.method == 'POST':
        n = request.form['uname']
        g = request.form['pass']
        n1=str(n)
        g1=str(g)

        q=("SELECT * from retailer_details where username='" + str(n1) + "' and password='" + str(g1) + "'")
        data=mm.select_direct_query(q)
        data=len(data)
        if data==0:
            return render_template('bank_login.html',flash_message=True,data="Failed")
        else:
            msg='Success'
            session['user'] =n
            return render_template('retailer_home.html',sid=n)
    return render_template('bank_login.html',error=msg)






@app.route("/user_register", methods=['GET', 'POST'])
def user_register():
    if request.method == 'POST':
        name = request.form['name']
        contact = request.form['contact']
        email = request.form['email']
        address = request.form['address']
        gender = request.form['gender']
        username = request.form['username']
        password = request.form['password']


        maxin = mm.find_max_id("customer_details")
        qq = "insert into customer_details values('" + str(maxin) + "','" + str(name) + "','" + str(contact) + "','" + str(
            email) + "','" + str(address) + "','" + str(gender) + "','" + str(username) + "','" + str(password) + "')"
        result = mm.insert_query(qq)
        return render_template('user_login.html')
    return render_template('user_register.html')




@app.route("/bank_register", methods=['GET', 'POST'])
def bank_register():
    if request.method == 'POST':
        name = request.form['name']
        contact = request.form['contact']
        address = request.form['address']
        email = request.form['email']
        gender = request.form['gender']
        username = request.form['username']
        password = request.form['password']

        maxin = mm.find_max_id("retailer_details")
        qq = "insert into retailer_details values('" + str(maxin) + "','" + str(name) + "','" + str(contact) + "','" + str(
                address) + "','" + str(email) + "','" + str(gender) + "','" + str(username) + "','" + str(password) + "')"
        result = mm.insert_query(qq)

        if (result == 1):
            return render_template('bank_login.html', msg="Success")
        else:
            return render_template('bank_register.html')
    return render_template('bank_register.html')





@app.route("/retailer_add_product", methods=['GET', 'POST'])
def retailer_add_product():
    if request.method == 'POST':
        product_name = request.form['product_name']
        brand = request.form['brand']
        starting_price = request.form['starting_price']
        category = request.form['category']
        f = request.files['file']
        f.save(os.path.join("static/uploads/", secure_filename(f.filename)))

        maxin = mm.find_max_id("product_details")
        qq = "insert into product_details values('" + str(maxin) + "','" + str(product_name) + "','" + str(brand) + "','" + str(
                starting_price) + "','" + str(f.filename) + "','" + str(category) + "','')"
        result = mm.insert_query(qq)

        return render_template('retailer_add_product.html')
    return render_template('retailer_add_product.html')






@app.route("/user_view_product")
def user_view_product():
    data = mm.select_direct_query("select * from product_details")
    return render_template('user_view_product.html',items=data)


@app.route("/bid_click1",methods = ['GET', 'POST'])
def bid_click1():
    n=session['user']

    q = ("SELECT * from customer_details where username='" + str(n) + "'")
    data = mm.select_direct_query(q)
    cname=data[0][1]
    contact=data[0][2]

    id=session['id']
    data = mm.select_direct_query("select * from product_details where id='"+ str(id) +"'")
    pname=data[0][1]
    brand=data[0][2]
    amount=data[0][3]

    if request.method == 'POST':
        price = request.form['price']


        maxin = mm.find_max_id("bidding_details")
        qq = "insert into bidding_details values('" + str(maxin) + "','" + str(pname) + "','" + str(brand) + "','" + str(
                amount) + "','" + str(cname) + "','" + str(contact) + "','"+ str(price) +"','Requested')"
        result = mm.insert_query(qq)

        return redirect('user_view_product')
    return render_template('bid_click1.html',items=data)


@app.route("/bid_click/<id>")
def bid_click(id):

      session['id'] = id
      return redirect('/bid_click1')



@app.route("/user_bidding_request")
def user_bidding_request():
    n = session['user']

    data = mm.select_direct_query("select * from bidding_details where status='Requested' and cus_name='"+ str(n) +"'")
    return render_template('user_bidding_request.html',items=data)


@app.route("/user_payment")
def user_payment():
    data = mm.select_direct_query("select * from bidding_details where status='Final Accept'")
    return render_template('user_payment.html',items=data)




@app.route("/payment",methods = ['GET', 'POST'])
def payment():
    id=session['id']
    data = mm.select_direct_query("select * from bidding_details where id='" + str(id) + "'")
    pname = data[0][1]
    brand = data[0][2]
    amount = data[0][6]

    n = session['user']
    if request.method == 'POST':
        holder_name = request.form['holder_name']
        accno = request.form['accno']
        cvv = request.form['cvv']


        maxin = mm.find_max_id("payment")
        qq = "insert into payment values('" + str(maxin) + "','" + str(holder_name) + "','" + str(accno) + "','" + str(
                cvv) + "','" + str(n) + "','"+ str(pname) +"','"+ str(brand) +"','"+ str(amount) +"')"
        result = mm.insert_query(qq)
        d = mm.insert_query("update bidding_details set status='Paid' where id='" + str(id) + "'")
        return redirect('/user_payment')
    return render_template('payment.html',amount=amount)



@app.route("/user_pay/<id>")
def user_pay(id):

      session['id'] = id
      return redirect('/payment')



@app.route("/admin_view_user")
def admin_view_user():
    data = mm.select_direct_query("select name,contact,email,address,gender,username from customer_details")
    return render_template('admin_view_user.html',items=data)


@app.route("/admin_view_retailer")
def admin_view_retailer():
    data = mm.select_direct_query("select name,contact,email,address,gender,username from retailer_details")
    return render_template('admin_view_retailer.html',items=data)


@app.route("/admin_view_product")
def admin_view_product():
    data = mm.select_direct_query("select * from product_details")
    return render_template('admin_view_product.html',items=data)




@app.route("/retailer_time_notification")
def retailer_time_notification():
    s="select * from bidding_details where status='First Accept' or status='Second Accept'"
    print(s)
    data = mm.select_direct_query(s)

    return render_template('retailer_time_notification.html',items=data)


@app.route("/retailer_no1/<id>")
def retailer_no1(id):

      session['id'] = id
      d = mm.insert_query("update bidding_details set status='Second Accept' where id='" + str(id) + "'")
      return redirect('/retailer_time_notification')



@app.route("/retailer_no2/<id>")
def retailer_no2(id):

      session['id'] = id
      d = mm.insert_query("update bidding_details set status='End'")
      d = mm.insert_query("update bidding_details set status='Final Accept' where id='" + str(id) + "'")
      vs = mm.select_direct_query("select productname,cus_price from bidding_details where id='" + str(id) + "'")
      proname = vs[0][0]
      cusp=vs[0][1]
      d = mm.insert_query("update product_details set status='1',start_price='"+ str(cusp) +"' where product_name='" + str(proname) + "'")

      return redirect('/retailer_time_notification')





@app.route("/retailer_bidding_price")
def retailer_bidding_price():
    data = mm.select_direct_query("select * from bidding_details where status='Requested'")
    return render_template('retailer_bidding_price.html',items=data)


@app.route("/retailer_acp/<id>")
def retailer_acp(id):

      session['id'] = id
      vs = mm.select_direct_query("select productname,cus_name from bidding_details where id='"+ str(id) +"'")
      productname=vs[0][0]
      print(productname)

      data=mm.select_direct_query("select id,status from bidding_details where productname='"+ str(productname) +"' and status='First Accept' or status='Second Accept'")

      sf=len(data)

      if (sf):

         sid=data[0][0]
         print(sid)
         datac = mm.select_direct_query("select * from bidding_details where productname='"+ str(productname) +"'")
         for da in datac:
             mid=da[0]
             cv="update bidding_details set status='Requested'"
             print(cv)
             df = mm.insert_query(cv)



         df = mm.insert_query("update bidding_details set status='First Accept' where id='" + str(id) + "'")
         return redirect('/retailer_bidding_price')
      d = mm.insert_query("update bidding_details set status='First Accept' where id='" + str(id) + "'")
      return redirect('/retailer_bidding_price')








@app.route("/user_view_notification")
def user_view_notification():
    data = mm.select_direct_query("select * from bidding_details")
    return render_template('user_view_notification.html',items=data)



@app.route("/user_chat", methods=['GET', 'POST'])
def user_chat():
    n = session['user']
    data = mm.select_direct_query("select * from chat where username='"+ (n) +"'")
    print(data)
    vs = mm.select_direct_query("select name from retailer_details")
    productname = vs[0][0]

    if request.method == 'POST':

        rname = request.form['rname']
        chat = request.form['chat']


        maxin = mm.find_max_id("chat")
        qq = "insert into chat values('" + str(maxin) + "','" + str(rname) + "','" + str(chat) + "','" + str(
            n) + "','" + str(n) + "')"
        result = mm.insert_query(qq)
        return render_template('user_chat.html',items=vs,data=data)
    return render_template('user_chat.html',items=vs,data=data)



@app.route("/retailer_chat")
def retailer_chat():
    data = mm.select_direct_query("select DISTINCT username from chat")
    return render_template('retailer_chat.html',items=data)



@app.route("/retailer_chat_user", methods=['GET', 'POST'])
def retailer_chat_user():
    n=session['user']
    id=session['id']
    data = mm.select_direct_query("select * from chat where retailer_name='"+ str(n) +"'")
    print(data)
    if request.method == 'POST':


        chat = request.form['chat']


        maxin = mm.find_max_id("chat")
        qq = "insert into chat values('" + str(maxin) + "','" + str(n) + "','" + str(chat) + "','" + str(id) + "','"+ str(n) +"')"
        result = mm.insert_query(qq)
        return redirect('retailer_chat_user')
    return render_template('retailer_chat_user.html',items=data)



@app.route("/chat_view/<id>")
def chat_view(id):

      session['id'] = id
      d = mm.insert_query("update bidding_details set status='Second Accept' where id='" + str(id) + "'")
      return redirect('/retailer_chat_user')






@app.route("/retailer_view_payment")
def retailer_view_payment():
    data = mm.select_direct_query("select * from payment")
    return render_template('retailer_view_payment.html',items=data)







@app.route("/admin_view_bidding")
def admin_view_bidding():
    data = mm.select_direct_query("select * from bidding_details where status='Paid'")
    return render_template('admin_view_bidding.html',items=data)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

