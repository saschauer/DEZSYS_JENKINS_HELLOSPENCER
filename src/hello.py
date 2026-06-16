from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello_spencer():
    if not os.path.exists("count.txt"):
        with open("count.txt", "w") as f:
            f.write("0")

    f = open("count.txt","r")
    counter = int(f.read())
    f.close()

    counter += 1

    f = open("count.txt","w")
    f.write(str(counter))
    f.close()

    return jsonify({
        "message": "Hello Spencer",
        "counter" : counter,
        "status": "success"
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5556)