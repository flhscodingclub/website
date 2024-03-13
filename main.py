from flask import Flask, jsonify, request
import datetime

app = Flask(__name__)

bathroom_data = {
    'f1': {
        'b1': {
            'reports_enum': 0,
            'last_push': None
        },
        'b2': {
            'reports_enum': 0,
            'last_push': None
        }
    },
    'f2': {
        'b1': {
            'reports_enum': 0,
            'last_push': None
        },
        'b2': {
            'reports_enum': 0,
            'last_push': None
        }
    },
    'f3': {
        'b1': {
            'reports_enum': 0,
            'last_push': None
        },
        'b2': {
            'reports_enum': 0,
            'last_push': None
        }
    }
}

# http://127.0.0.1:5000/bathroom?floor=f1&bathroom=b1


@app.route('/bathroom', methods=['GET', 'PUT'])
def get_or_update_bathroom_data():
    if request.method == 'GET':
        return jsonify(bathroom_data)

    elif request.method == 'PUT':
        floor = request.args.get('floor')
        room_name = request.args.get('bathroom')

        if floor and room_name:
            if floor in bathroom_data and room_name in bathroom_data[floor]:
                bathroom_data[floor][room_name]['reports_enum'] += 1
                bathroom_data[floor][room_name]['last_push'] = datetime.datetime.now().strftime('%m/%d/%y %H:%M')

                return jsonify(bathroom_data)

        return jsonify({'error': 'Invalid parameters'})


if __name__ == '__main__':
    app.run(debug=True)
