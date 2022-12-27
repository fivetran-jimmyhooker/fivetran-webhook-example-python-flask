import os
import hmac
import hashlib
import colorama
from dotenv import load_dotenv
from flask import Flask, request

# Load the .env file
load_dotenv()

app = Flask(__name__)

# Initialize colorama
colorama.init()

# Read the SIGNATURE_SECRET value from the .env file
SIGNATURE_SECRET = os.getenv("SIGNATURE_SECRET")

def dump_headers(headers):
    print(colorama.Fore.CYAN + "Headers")
    print(headers)
    print("\n")

def dump_payload(payload):
    print(colorama.Fore.CYAN + "Payload")
    print(payload)
    print("\n")

# Check the signature
def check_signature(request):
    actual_signature = request.headers.get("x-fivetran-signature-256")
    if actual_signature:
        if SIGNATURE_SECRET is None:
            print(colorama.Fore.RED + "Error: SIGNATURE_SECRET is not defined. Please create a .env file in the root and define it.")
        else:
            expected_signature = hmac.new(SIGNATURE_SECRET.encode(), request.data, hashlib.sha256).hexdigest().upper()
            if actual_signature.upper() == expected_signature:
                print(colorama.Fore.GREEN + "Signature OK")
            else:
                print(colorama.Fore.RED + "Signature mismatch")

# Create a webhook endpoint to receive webhook events
@app.route("/", methods=["POST"])
def handle_request():
    dump_headers(request.headers)
    dump_payload(request.data)
    check_signature(request)
    print("==========\n")

    return ""

# Run the app
if __name__ == "__main__":
    app.run(port=4242)
