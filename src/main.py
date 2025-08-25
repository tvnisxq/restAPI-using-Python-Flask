from flask import Flask, jsonify, make_response, request

app = Flask(__name__)


def json_error(message, status=400):
    return make_response(jsonify({"error": message}), status)


@app.route("/")
def hello_world():
    return jsonify({"message": "This is a Sample restAPI."})


def sum(a, b):
    return a + b


def avg(a, b):
    return (a + b) / 2


def is_armstrong(n: int) -> bool:
    """Return True if n is an Armstrong number."""
    if n < 0:
        return False
    order = len(str(n))
    total = 0
    tmp = n
    while tmp > 0:
        digit = tmp % 10
        total += digit ** order
        tmp //= 10
    return total == n


def is_palindrome(n: int) -> bool:
    """Return True if integer n is a palindrome."""
    if n < 0:
        return False
    s = str(n)
    return s == s[::-1]


@app.route("/armstrong/<int:n>")
def armstrongNumber(n):
    # Basic validation
    if n < 0:
        return json_error("n must be a non-negative integer", 400)
    if len(str(n)) > 100:
        return json_error("number too large", 413)

    try:
        result = {
            "Number": n,
            "Armstrong": is_armstrong(n),
            "Server IP": "127.0.0.1:5000",
        }
        return jsonify(result)
    except Exception as e:
        return json_error(f"internal error: {e}", 500)


from flask import Flask, jsonify, make_response

app = Flask(__name__)


def json_error(message, status=400):
    return make_response(jsonify({"error": message}), status)


@app.route("/")
def hello_world():
    return jsonify({"message": "Hello, World!"})


def sum(a, b):
    return a + b


def avg(a, b):
    return (a + b) / 2


def is_armstrong(n: int) -> bool:
    """Return True if n is an Armstrong number."""
    if n < 0:
        return False
    order = len(str(n))
    total = 0
    tmp = n
    while tmp > 0:
        digit = tmp % 10
        total += digit ** order
        tmp //= 10
    return total == n


def is_palindrome(n: int) -> bool:
    """Return True if integer n is a palindrome."""
    if n < 0:
        return False
    s = str(n)
    return s == s[::-1]


@app.route("/armstrong/<int:n>")
def armstrongNumber(n):
    # Basic validation
    if n < 0:
        return json_error("n must be a non-negative integer", 400)
    if len(str(n)) > 100:
        return json_error("number too large", 413)

    try:
        result = {
            "Number": n,
            "Armstrong": is_armstrong(n),
            "Server IP": "127.0.0.1:5000",
        }
        return jsonify(result)
    except Exception as e:
        return json_error(f"internal error: {e}", 500)


@app.route("/palindrome/<int:n>")
def palindromeNumber(n):
    if n < 0:
        return json_error("n must be a non-negative integer", 400)
    if len(str(n)) > 100:
        return json_error("number too large", 413)

    try:
        result = {
            "Number": n,
            "Palindrome": is_palindrome(n),
            "Server IP": "127.0.0.1:5000",
        }
        return jsonify(result)
    except Exception as e:
        return json_error(f"internal error: {e}", 500)


@app.route("/sum")
def sum_get():
    # Accepts query params: ?a=2&b=3
    a_raw = request.args.get("a")
    b_raw = request.args.get("b")
    if a_raw is None or b_raw is None:
        return json_error("a and b query parameters are required", 400)
    try:
        a = int(a_raw)
        b = int(b_raw)
    except ValueError:
        return json_error("a and b must be integers", 400)

    try:
        return jsonify({"a": a, "b": b, "result": sum(a, b)})
    except Exception as e:
        return json_error(f"internal error: {e}", 500)


@app.route("/sum", methods=["POST"])
def sum_post():
    # Accepts JSON body: {"a": 2, "b": 3}
    if not request.is_json:
        return json_error("JSON body required", 400)
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return json_error("invalid JSON body", 400)
    if "a" not in data or "b" not in data:
        return json_error("a and b fields are required", 400)
    try:
        a = int(data["a"])
        b = int(data["b"])
    except (ValueError, TypeError):
        return json_error("a and b must be integers", 400)

    try:
        return jsonify({"a": a, "b": b, "result": sum(a, b)})
    except Exception as e:
        return json_error(f"internal error: {e}", 500)


@app.route("/avg")
def avg_get():
    # Accepts query params: ?a=2&b=3
    a_raw = request.args.get("a")
    b_raw = request.args.get("b")
    if a_raw is None or b_raw is None:
        return json_error("a and b query parameters are required", 400)
    try:
        a = float(a_raw)
        b = float(b_raw)
    except ValueError:
        return json_error("a and b must be numbers", 400)

    try:
        return jsonify({"a": a, "b": b, "result": avg(a, b)})
    except Exception as e:
        return json_error(f"internal error: {e}", 500)


@app.route("/avg", methods=["POST"])
def avg_post():
    # Accepts JSON body: {"a": 2, "b": 3}
    if not request.is_json:
        return json_error("JSON body required", 400)
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return json_error("invalid JSON body", 400)
    if "a" not in data or "b" not in data:
        return json_error("a and b fields are required", 400)
    try:
        a = float(data["a"])
        b = float(data["b"])
    except (ValueError, TypeError):
        return json_error("a and b must be numbers", 400)

    try:
        return jsonify({"a": a, "b": b, "result": avg(a, b)})
    except Exception as e:
        return json_error(f"internal error: {e}", 500)


if __name__ == "__main__":
    app.run(debug=True)
