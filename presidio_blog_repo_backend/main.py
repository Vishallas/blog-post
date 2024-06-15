from flask import Flask, jsonify, request
import aws_controller

app = Flask(__name__)
    
@app.route('/get-items')
def get_items():
    return jsonify(aws_controller.get_all_posts())


@app.route('/put-item', methods=['PUT'])
def put_item():
    return jsonify(aws_controller.put_post(request))