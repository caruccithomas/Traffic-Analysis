### Instructions ###

- It is a requirement to have python installed:
    * brew install python3

- Next, we have to install the dependencies found in "requirements.txt" file:
    * pip install -r requirements.txt

- Test if the app.py file executed correctly:
    * python app.py

- Mount Flask library in the project with:
    * app = Flask(__name__)

- Establish manually the Network Interface
- Capture packets
- Use threading for reading the packets
- Filter packets
- GET /packets endpoint data converted to JSON 

- Initialize Flask:
    * app.run(host='0.0.0.0', port=80)

# Dependencies used in this challenge

- Flask
- Scapy
- iproute2 (it will install when the container is built)