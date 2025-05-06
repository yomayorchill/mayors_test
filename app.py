from flask import Flask, request
import mayorr

app = Flask(__name__)

#We want the user to type in the browser http://192.168.1.34/?num = 87
@app.route('/')
def pickwinner():
    num = request.args.get('n')
    num = int(num)
    winner = mayorr.select(num)
    return (f'The winner of this is {winner.upper()}')

if __name__ == "__main__":
    app.run(host = "0.0.0.0",port = 80,debug=False)
