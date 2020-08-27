from flask import Flask
import uuid4
from blockchain import BlockChain

app = Flask(__name__)


node_identifier = str(uuid4()).replace("-","")

blockchain = Blockchain()

@app.route("/mine", method=["GET"])
def mine():
   return "Mining a new Block"

@app.route("/transaction/new", method=["POST"])
def new_transaction():
   return "Adding a new transaction"