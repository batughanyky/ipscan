from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/")
def index():
    ips = os.popen('arp -a').read()
    return render_template("index.html", ips=ips)

@app.route("/ip")
def get_ip():
    ip = request.remote_addr
    return render_template("ip.html", ip=ip)

if __name__ == "__main__":
    app.run(debug=True)
