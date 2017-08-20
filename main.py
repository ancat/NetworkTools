from flask import Flask, session, redirect, url_for, escape, request, render_template
import os

app = Flask(__name__)

def hostname_lookup(hostname):
    return os.popen('dig +short {}'.format(hostname)).read()

def ping_ip(ip_address):
    return os.popen('ping -c 4 -i .1 {}'.format(ip_address)).read()

@app.route('/hostname', methods=['GET'])
def handle_hostname():
    hostname = request.args.get('hostname', None)
    if hostname is None:
        result = "No hostname provided."
    else:
        ip_address = hostname_lookup(hostname)
        result = "IP address: " + ip_address
    return render_template('results.html', result=result)

@app.route('/ping', methods=['GET'])
def handle_ping():
    ip_address = request.args.get('ip', None)
    if ip_address is None:
        result = "No IP address provided."
    else:
        ping_response = ping_ip(ip_address)
        result = ping_response
    return render_template('results.html', result=result)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

