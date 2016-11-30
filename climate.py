from flask import Flask, request, make_response
import os

app = Flask(__name__)

@app.route('/introduction', methods = ['POST', 'GET'])
def introduction():
    #play the introduction menu
    res = '<?xml version="1.0" encoding="UTF-8"?>'
    res+='<Response>'
    res+='<Play url = "https://raw.githubusercontent.com/flacode/climate/master/recording/Welcome.mp3"/>'
    res+= '<GetDigits timeout="20" numDigits="1" callbackUrl="https://7ac21b62.ngrok.io/region"></GetDigits>'
    res+='</Response>'

    res = make_response(res, 200)
    res.headers['Content-Type'] = "application/xml"
    return res


@app.route('/region', methods=['POST', 'GET'])
def region():
    #play the region menu according to the language selected
    language = request.form['dtmfDigits']
    if language ==  1:
        res = '<?xml version="1.0" encoding="UTF-8"?>'
        res += '<Response>'
        res += '<Play url = "https://raw.githubusercontent.com/flacode/climate/master/recording/Region2.mp3"/>'
        res += '<GetDigits timeout="20" numDigits="1" callbackUrl="https://7ac21b62.ngrok.io/information"></GetDigits>'
        res += '</Response>'

        res = make_response(res, 200)
        res.headers['Content-Type'] = "application/xml"
        return res


@app.route('/information', methods = ['POST', 'GET'])
def information():
    #play the regional information
    region=request.form['dtmfDigits']
    if region == 4:
        res = '<?xml version="1.0" encoding="UTF-8"?>'
        res += '<Response>'
        res += '<Play url = "https://raw.githubusercontent.com/flacode/climate/master/recording/Menu.mp3"/>'
        res += '<GetDigits timeout="20" numDigits="1" callbackUrl="https://7ac21b62.ngrok.io/solution"></GetDigits>'
        res += '</Response>'

        res = make_response(res, 200)
        res.headers['Content-Type'] = "application/xml"
        return res


@app.route('/solution', methods = ['POST', 'GET'])
def solution():
    #paly the final menu
    information=request.form['dtmfDigits']
    if information == 2:
        res = '<?xml version="1.0" encoding="UTF-8"?>'
        res += '<Response>'
        res += '<Play url = "https://raw.githubusercontent.com/flacode/climate/master/recording/Output.mp3"/>'
        res += '<GetDigits timeout="20" numDigits="1" callbackUrl="https://7ac21b62.ngrok.io/solution"></GetDigits>'
        res += '</Response>'

        res = make_response(res, 200)
        res.headers['Content-Type'] = "application/xml"
        return res




if __name__ == '__main__':
    app.run(port=int(8000))
