from flask import Flask, request

app = Flask(__name__)

BASE_DIR = '/path/to/your/directory'  # Change this to your desired directory

@app.route('/read-file/<filename>', methods=['GET'])
def read_file(filename):
    print(filename)
    try:
        with open(f"{BASE_DIR}/{filename}", 'r') as file:
            content = file.read()
        return content, 200
    except FileNotFoundError:
        return "File not found", 404
    except Exception as e:
        return str(e), 500  
    
@app.route('/write-file/<filename>', methods=['POST'])
def write_file(filename):
    print(filename)
    data = request.get_json()
    try:
        with open(f"{BASE_DIR}/{filename}", 'w') as file:
            file.write(data['body'])
        return "File written successfully", 200
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)