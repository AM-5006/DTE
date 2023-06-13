from flask import Flask, render_template, request, redirect, make_response
import requests
import json 

app = Flask(__name__)

#Index page
@app.route('/')
def index():
    return render_template("index.html")

#Processing of form data
@app.route('/facebook', methods=["POST"])
def facebook():
    access_token= request.form['token']
    page_id= request.form['page']
    message= request.form['message']

    status, response = validate_access_token(access_token= access_token)
    if status:
        status, response = post_on_page(access_token, page_id, message)
        if status:
            page_id, post_id = response["id"].split('_')
            response = { "page_id": page_id, 
                        "post_id": post_id
                       }
            return render_template("success.html", response = response)
        else:
            response['error']['message'] = response['error']['message'].replace('\\\n', '')
            response['site'] = "https://developers.facebook.com/tools/explorer/"
            return render_template("error.html", response = response)
    return render_template("error.html", response = response)

#validates the access token
def validate_access_token(access_token):
    response = requests.get(f"https://graph.facebook.com/v17.0/me?access_token={access_token}")
    if response.status_code == 200:
        return (True, response.json())
    return (False, response.json())

#Posts message
def post_on_page(access_token, page_id, message):
    data = {
        'access_token': access_token,
        'message': message
    }
    response = requests.post(f"https://graph.facebook.com/{page_id}/feed", data=data)
    if response.status_code == 200:
        return (True, response.json())
    else:
        return (False, response.json())


if __name__ == '__main__':
    app.run(debug = True)