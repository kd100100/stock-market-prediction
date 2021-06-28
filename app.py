from flask import Flask, render_template, url_for, request, redirect, session
app = Flask(__name__)
app.secret_key='knowNinvest'
#knowninvest.pythonanywhere.com
from news import get_news
from operation import check_login, get_history
from predict import get_data

from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
db = SQLAlchemy(app)

class user(db.Model):
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(40), primary_key = True, nullable = False)
    password = db.Column(db.String(20), nullable=False)
    history = db.Column(db.String(50000))

    def __repr__(self):
        return f"{self.name}:{self.email}:{self.password}:{self.history}"

# Completed
@app.route('/')
def home():
    session['redirect'] = "home"
    return render_template('home.html', session = session)

@app.route('/predict', methods=['POST','GET'])
def predict():
    # 2021-03-20
    session['redirect'] = "predict"
    if request.method == 'POST':
        date = request.form['date']
        session['pred_date'] = date
        company = request.form['company']
        session['pred_company'] = company
        if company == 'Adani Ports': dataset = 'ADANIPORTS'
        elif company == 'Asian Paints': dataset = 'ASIANPAINTS'
        elif company == 'Axis Bank': dataset = 'AXISBANK'
        elif company == 'Bajaj Auto': dataset = 'BAJAJ-AUTO'
        elif company == 'Bajaj Finserv': dataset = 'BAJAJFINSV'
        elif company == 'Bajaj Finance': dataset = 'BAJFINANCE'
        elif company == 'Bharati Airtel': dataset = 'BHARTIARTL'
        elif company == 'BPCL': dataset = 'BPCL'
        elif company == 'Britannia': dataset = 'BRITANNIA'
        elif company == 'CIPLA': dataset = 'CIPLA'
        elif company == 'Coal India': dataset = 'COALINDIA'
        elif company == 'Dr.Reddy': dataset = 'DRREDDY'
        elif company == 'Eicher Motors': dataset = 'EICHERMOT'
        elif company == 'GAIL': dataset = 'GAIL'
        elif company == 'GRASIM': dataset = 'GRASIM'
        elif company == 'HCl Technologies': dataset = 'HCLTECH'
        elif company == 'HDFC': dataset = 'HDFC'
        elif company == 'HDFC Bank': dataset = 'HDFCBANK'
        elif company == 'Hero Moto Coporation': dataset = 'HEROMOTOCO'
        elif company == 'Hindal Corporation': dataset = 'HINDALCO'
        elif company == 'Hindustan Uniliver': dataset = 'HINDUNILVR'
        elif company == 'ICICI Bank': dataset = 'ICICIBANK'
        elif company == 'Indusind Bank': dataset = 'INDUSINDBK'
        elif company == 'Infra Tel': dataset = 'INFRATEL'
        elif company == 'Infy': dataset = 'INFY'
        elif company == 'Indian Oil Coporation': dataset = 'IOC'
        elif company == 'ITC': dataset = 'ITC'
        elif company == 'JSW Steels': dataset = 'JSWSTEEL'
        elif company == 'Kotak Bank': dataset = 'KOTAKBANK'
        elif company == 'L&T': dataset = 'LT'
        elif company == 'Maruti': dataset = 'MARUTI'
        elif company == 'Mudman PCL': dataset = 'MM'
        elif company == 'Nestle India': dataset = 'NESTLEIND'
        elif company == 'NTPC': dataset = 'NTPC'
        elif company == 'ONGC': dataset = 'ONGC'
        elif company == 'Powergrid': dataset = 'POWERGRID'
        elif company == 'Reliance': dataset = 'RELIANCE'
        elif company == 'SBIN': dataset = 'SBIN'
        elif company == 'SHREECEM': dataset = 'SHREECEM'
        elif company == 'Sun Pharma': dataset = 'SUNPARMA'
        elif company == 'Tata Motors': dataset = 'TATAMOTORS'
        elif company == 'Tata Steel': dataset = 'TATASTEEL'
        elif company == 'TCS': dataset = 'TCS'
        elif company == 'Tech Mahindra': dataset = 'TECHM'
        elif company == 'Titan': dataset = 'TITAN'
        elif company == 'Ultra Cement': dataset = 'ULTRACEMCO'
        elif company == 'UPL': dataset = 'UPL'
        elif company == 'VEDL': dataset = 'VEDL'
        elif company == 'WIPRO': dataset = 'WIPRO'
        elif company == 'ZEEL': dataset = 'ZEEL'
        res = get_data(dataset, date)
        session['pred_open'] = round(float(res['open'][0]), 2)
        session['pred_low'] = round(float(res['low'][0]), 2)
        session['pred_high'] = round(float(res['high'][0]), 2)
        session['pred_close'] = round(float(res['close'][0]), 2)
        return redirect('/result')

    if 'login' in session:
        db_obj = user.query.all()
        data = get_history(db_obj, session['email'])
        return render_template('predict.html', session = session, data = data)
    else: 
        return redirect('/login')

@app.route('/result')
def result():
    if 'login' in session:
        return render_template('result.html', session = session)
    else: 
        return redirect('/login')       

# Completed
@app.route('/news')
def news():
    session['redirect'] = "news"
    data = get_news()
    return render_template('news.html', data = data)

# Completed
@app.route('/login', methods=['POST','GET'])
def login():
    if request.method=="POST":
        email = request.form['email']
        password = request.form['password']
        print(email,password)
        db_obj = user.query.all()
        res, name = check_login(db_obj, email, password)
        print(res)  
        if res == 0:
            return "redirect('/404/user-not-found')"
        elif res == 2:
            return "redirect('/404/wrong-password')"
        elif res == 1:
            session["login"] = name
            session["email"] = email
            if session['redirect'] != "home":
                return redirect('/'+session['redirect'])
            else:
                return redirect('/')
    return render_template('login.html')

# Completed
@app.route('/register', methods=['POST','GET'])
def register():
    if request.method=='POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        session["login"] = name
        session["email"] = email
        new = user(name=name,email=email,password=password)
        db.session.add(new)
        db.session.commit()
        if session['redirect'] != "home":
            return redirect('/'+session['redirect'])
        else:
            return redirect('/')
    return render_template('register.html')

# Completed
@app.route('/logout')
def logout():
    del session['login']
    del session['email']
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)