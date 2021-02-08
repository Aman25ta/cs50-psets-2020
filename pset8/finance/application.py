import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required

def index():

    rows = db.execute("SELECT * FROM stocks WHERE user_id = :user",
                          user=session["user_id"])
    cash = db.execute("SELECT cash FROM users WHERE id = :user",
                          user=session["user_id"])[0]['cash']

    total = cash
    stocks = []
    for index, row in enumerate(rows):
        stock_info = lookup(row['symbol'])

        stocks.append(list((stock_info['symbol'], stock_info['name'], row['amount'], stock_info['price'], round(stock_info['price'] * row['amount'], 2))))
        total += stocks[index][4]

    return render_template("index.html", stocks=stocks, cash=round(cash, 2), total=round(total, 2))

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        # Obtain the data
        amount=int(request.form.get("amount"))
        symbol=lookup(request.form.get("symbol"))['symbol']

        if not lookup(symbol):
            return apology("Could not find the stock")

        # Calculate total value
        price=lookup(symbol)['price']
        cash = db.execute("SELECT cash FROM users WHERE id = :user",
                          user=session["user_id"])[0]['cash']
        cash_after = float(cash) - price * float(amount)

        # Check if current cash is enough for transaction
        if cash_after < 0:
            return apology("You don't have enough money for this transaction")

        # Check if user already has one or more stocks from the same company
        stock = db.execute("SELECT amount FROM stocks WHERE user_id = :user AND symbol = :symbol",
                          user=session["user_id"], symbol=symbol)

        # Insert new row into the stock table
        if not stock:
            db.execute("INSERT INTO stocks(user_id, symbol, amount) VALUES (:user, :symbol, :amount)",
                user=session["user_id"], symbol=symbol, amount=amount)

        # update row into the stock table
        else:
            amount += stock[0]['amount']

            db.execute("UPDATE stocks SET amount = :amount WHERE user_id = :user AND symbol = :symbol",
                user=session["user_id"], symbol=symbol, amount=amount)

        # update user's cash
        db.execute("UPDATE users SET cash = :cash WHERE id = :user",
                          cash=cash_after, user=session["user_id"])

        # Update history table
        db.execute("INSERT INTO transactions(user_id, symbol, amount, value, date) VALUES (:user, :symbol, :amount, :value, datetime())",
                user=session["user_id"], symbol=symbol, amount=amount, value=round(price*float(amount)))

        # Redirect user to index page with a success message
        flash("Bought!")
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("buy.html")



@app.route("/history")
@login_required
def history():

    rows = db.execute("SELECT * FROM transactions WHERE user_id = :user",
                            user=session["user_id"])

    # pass a list of lists to the template page
    transactions = []
    for row in rows:
        stock_info = lookup(row['symbol'])

        # create a list with all the info
        transactions.append(list((stock_info['symbol'], stock_info['name'], row['amount'], row['value'], row['date'])))

    # redirect user
    return render_template("history.html", transactions=transactions)



@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)
        rows = db.execute("SELECT * FROM users WHERE name = :username",
                          username=request.form.get("username"))
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    if request.method == "POST":
        stock = lookup(request.form.get("symbol"))
        if not stock:
            return apology("Could not find the stock")
        return render_template("quote.html", stock=stock)
    else:
        return render_template("quote.html", stock="")



@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "POST":

        #check for username
        if not request.form.get("username"):
            return apology("must provide username")

        #chack for mail adress
        elif not request.form.get("email"):
            return apology("must provide email")

        #check password
        elif not request.form.get("password") or not request.form.get("confirm_password"):
            return apology("must provide password and confirmation")

        #recheck/confirm pass
        elif request.form.get("password") != request.form.get("confirm_password"):
            return apology("passwords do not match")

        #check if already registeres
        rows = db.execute("SELECT * FROM users WHERE name = :name", name=request.form.get("username"))
        if len(rows) >= 1:
            return apology("username already exists")

        rows = db.execute("SELECT * FROM users WHERE email = :email", email=request.form.get("email"))
        if len(rows) >= 1:
            return apology("email already exists")
        cash = 10000
        #add user to database
        db.execute("INSERT INTO users (name, hash, email, cash) VALUES (:name, :hash, :email, :cash)",
                    name=request.form.get("username"),
                    email=request.form.get("email"),
                    hash=generate_password_hash(request.form.get("password"), method='pbkdf2:sha256', salt_length=8),
                    cash = cash,
                    )

        #login user automatically
        rows = db.execute("SELECT * FROM users WHERE name = :name", name=request.form.get("username"))
        session["user_id"] = rows[0]["id"]

        return redirect("/")

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    if request.method == "POST":
        amount=int(request.form.get("amount"))
        symbol=request.form.get("symbol")
        price=lookup(symbol)["price"]
        value=round(price*float(amount))
        amount_before = db.execute("SELECT amount FROM stocks WHERE user_id = :user AND symbol = :symbol",
                          symbol=symbol, user=session["user_id"])[0]['amount']
        amount_after = amount_before - amount
        if amount_after == 0:
            db.execute("DELETE FROM stocks WHERE user_id = :user AND symbol = :symbol",
                          symbol=symbol, user=session["user_id"])
        elif amount_after < 0:
            return apology("That's more than the stocks you own")
        else:
            db.execute("UPDATE stocks SET amount = :amount WHERE user_id = :user AND symbol = :symbol",
                          symbol=symbol, user=session["user_id"], amount=amount_after)
        cash = db.execute("SELECT cash FROM users WHERE id = :user",
                          user=session["user_id"])[0]['cash']
        cash_after = cash + price * float(amount)
        db.execute("UPDATE users SET cash = :cash WHERE id = :user",
                          cash=cash_after, user=session["user_id"])
        # Update
        db.execute("INSERT INTO transactions(user_id, symbol, amount, value) VALUES (:user, :symbol, :amount, :value)",
                user=session["user_id"], symbol=symbol, amount=-amount, value=value)
        flash("Sold!")
        return redirect("/")
    else:
        rows = db.execute("SELECT symbol, amount FROM stocks WHERE user_id = :user",
                            user=session["user_id"])
        stocks = {}
        for row in rows:
            stocks[row['symbol']] = row['amount']

        return render_template("sell.html", stocks=stocks)

@app.route("/add", methods=["GET", "POST"])
@login_required

def add():
    if request.method == "POST":
        cashadd = request.form.get("cashadd")
        addget = db.execute("SELECT cash FROM users WHERE id = :user",
                          user=session["user_id"])
        addgetx = addget[0].get('cash')
        finalcash = float(addgetx) + float(cashadd)
        db.execute("UPDATE users SET cash = :cash WHERE id = :user",
                          cash=finalcash, user=session["user_id"])
        return redirect("/")
    else:
        return render_template("add.html")

def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
'''
export API_KEY=pk_ee175a9d1da6440fab1eb44545a848f4
'''