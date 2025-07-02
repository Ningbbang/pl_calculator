from flask import Flask, request, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/calculate/?date=<date_val>', methods=['GET'])
def calculate(date_val):
    join_date = datetime.strptime(date_val, "%Y-%m-%d")
    first_amt = 12 - join_date.month
    second_date1 = datetime(join_date.year + 1, 1, 1)
    second_amt1 = 11 - first_amt
    second_date2 = datetime(join_date.year+1, join_date.month, join_date.day)
    second_amt2 = int(round((datetime(join_date.year, 12, 31) - join_date) /
                        (datetime(join_date.year, 12, 31) - datetime(join_date.year,1,1)) * 15, 0))
    third_date = datetime(join_date.year + 2, 1, 1)
    third_amt = 15
    fourth_date = datetime(join_date.year + 3, 1, 1)
    fourth_amt = 16

    paid_leave = {
        "date_val": date_val,
        "first_amt": first_amt,
        "second_date1": f'{second_date1.year}-{second_date1.month}-{second_date1.day}',
        "second_amt1": second_amt1,
        "second_date2": f'{second_date2.year}-{second_date2.month}-{second_date2.day}',
        "second_amt2": second_amt2,
        "third_date": f'{third_date.year}-{third_date.month}-{third_date.day}',
        "third_amt": third_amt,
        "fourth_date": f'{fourth_date.year}-{fourth_date.month}-{fourth_date.day}',
        "fourth_amt": fourth_amt
    }
    return jsonify(paid_leave), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
