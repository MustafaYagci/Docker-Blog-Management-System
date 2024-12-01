from flask import Flask, jsonify
   
   app = Flask(__name__)

   @app.route('/api/posts', methods=['GET'])
   def get_posts():
       return jsonify({"posts": [{"id": 1, "title": "Hello, Docker!"}]})

   if __name__ == '__main__':
       app.run(host='0.0.0.0', port=5000)