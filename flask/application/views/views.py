from application import app
from flask import request, jsonify, Response
from application.model.models import db, Payments

@app.route('/')
def index():
    return "Hello World"

@app.route('/add_payment', methods= ["POST"])
def post():
    input_data = request.get_json()
    #checks
    payment = Payments(amount = input_data["amount"], status = input_data["status"], items=input_data["items"])
    print(input_data)
    db.session.add(payment)
    db.session.commit()

    data = {'SUCCESS': 'new payment added'}
    return jsonify(data)


@app.route('/view_payments', methods= ["GET"])
def get():

    queryset = Payments.query.all()
    all_payments = []
    for x in queryset:
        y = {
            "orderid": x.orderid,
            "date": x.date,
            "amount": x.amount,
            "status" : x.status,
            "items" : x.items
        }
        all_payments.append(y)
    return all_payments, 200
