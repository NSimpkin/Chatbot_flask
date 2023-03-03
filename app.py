from flask import Flask, render_template, request
from chatbot import predict_class, get_response, intents

app = Flask(__name__)
app.config['SECRET_KEY'] = "a_secret_key_123"

answer_list = []

@app.route("/")
def home():
    global answer_list
    answer_list.clear()
    return render_template("index.html")

@app.route("/chatbot", methods=["GET", "POST"])
def chatbot():
    global answer_list
    if request.method == "POST":
        message = request.form['message']
        message = message.lower()
        ints = predict_class(message)
        res = get_response(ints, intents)
        answer_list.append(res)
        if len(answer_list) > 5:
            del answer_list[0]
        return render_template("chatbot.html", message=message, answer_list=answer_list)
    return render_template("chatbot.html", message="", answer_list=answer_list)

if __name__=="__main__":
    app.run(debug=True)
