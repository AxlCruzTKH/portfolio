from flask import Flask, request,jsonify

app = Flask(__name__)

@app.route('/test',methods=['GET','POST'])
def process_json():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data = request.get_json()
        obj_to_return = ""   
        if 'string_to_cut' in data.keys():
            value = data['string_to_cut']
            for i in range(1,len(value)+1):
                if i%3==0:
                    obj_to_return += value[i-1]

        else:
            return 'Error'

        return jsonify({'return_string:':obj_to_return})
    else:
        return 'Error'
