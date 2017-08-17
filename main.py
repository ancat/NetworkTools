from flask import Flask, session, redirect, url_for, escape, request
import os

app = Flask(__name__)

def hostname_lookup(hostname):
    return os.popen('dig +short {}'.format(hostname)).read()

def ping_ip(ip_address):
    return os.popen('ping -c 4 -i .1 {}'.format(ip_address)).read() 

@app.route('/hostname', methods=['GET'])
def handle_hostname():
    hostname = request.args.get('hostname', None)
    if not hostname:
        return "No hostname provided."

    ip_address = hostname_lookup(hostname)
    return "IP address: " + ip_address

@app.route('/ping', methods=['GET'])
def handle_ping():
    ip_address = request.args.get('ip', None)
    if not ip_address:
        return "No IP address provided."

    ping_response = ping_ip(ip_address)
    return '<pre>'+ping_response+'</pre>'


@app.route('/', methods=['GET'])
def index():
    template = open('router_index.html').read()
    return template.replace('{html}', '''
        <h1>Your Basic Router's Network Tools Page</h1>
        <h2>Hostname to IP address</h2>
        <form action="/hostname">
            <p><input type=text name=hostname>
            <p><input type=submit value=lookup!>
        </form>
        <h2>Ping IP address</h2>
        <form action="/ping">
            <p><input type=text name=ip>
            <p><input type=submit value=ping!>
        </form>
    ''')

