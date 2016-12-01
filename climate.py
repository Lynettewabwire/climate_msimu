from flask import Flask, request, make_response
from africastalking import AfricasTalkingGateway


username = "djangoGirlsKampala"
apikey   = '24ccf14a4274c58e0f99c429f313b357c79500457735f05c3b62239273005830'


gateway = AfricasTalkingGateway.AfricasTalkingGateway(username, apikey)

app = Flask(__name__)

@app.route('/introduction', methods = ['POST', 'GET'])
def introduction():
    answer=0
    #play the introduction menu
    res = '<?xml version="1.0" encoding="UTF-8"?>'
    res+='<Response>'
    res+='<GetDigits timeout="20" numDigits="1" callbackUrl="http://62.12.117.25:8000/region">'
    res+='<Play url="https://raw.githubusercontent.com/flacode/climate/master/recording/Welcome.mp3"/>'
    res+='</GetDigits>'
    res+='</Response>'

    res = make_response(res, 200)
    res.headers['Content-Type'] = "application/xml"
    return res


@app.route('/region', methods=['POST', 'GET'])
def region():
    #play the region menu according to the language selected
    language = request.values.get('dtmfDigits', type=int)
    if language ==  1:
        res = '<?xml version="1.0" encoding="UTF-8"?>'
        res += '<Response>'
        res += '<GetDigits timeout="20" numDigits="1" callbackUrl="http://62.12.117.25:8000/information">'
        res += '<Play url="https://raw.githubusercontent.com/flacode/climate/master/recording/Region2.mp3"/>'
        res += '</GetDigits>'
        res += '</Response>'

        res = make_response(res, 200)
        res.headers['Content-Type'] = "application/xml"
        return res
    else:
        region()


@app.route('/information', methods = ['POST', 'GET'])
def information():
    #play the regional information
    region=request.values.get('dtmfDigits', type=int)
    if region == 2:
        res = '<?xml version="1.0" encoding="UTF-8"?>'
        res += '<Response>'
        res += '<GetDigits timeout="20" numDigits="1" callbackUrl="http://62.12.117.25:8000/solution">'
        res += '<Play url="https://raw.githubusercontent.com/flacode/climate/master/recording/Menu.mp3"/>'
        res += '</GetDigits>'
        res += '</Response>'

        res = make_response(res, 200)
        res.headers['Content-Type'] = "application/xml"
        return res
    else:
        information()

@app.route('/solution', methods = ['POST', 'GET'])
def solution():
    #paly the final menu
    information=request.values.get('dtmfDigits', type=int)
    phoneNumber = request.values.get('callerNumber')

    if information == 2:
        res = '<?xml version="1.0" encoding="UTF-8"?>'
        res += '<Response>'
        res += '<Play url="https://raw.githubusercontent.com/flacode/climate/master/recording/Output.mp3"/>'
        res += '</Response>'

        gateway.sendMessage(to_= phoneNumber, message_= 'The drought is likely to last from May to July. However, over '
                                                        'the next 10 days light showers of rain are expected from '
                                                        'Wednesday to Friday. Please collect as much much water as possible. '
                                                        'Thank you for using our application.')

        res = make_response(res, 200)
        res.headers['Content-Type'] = "application/xml"
        return res
    else:
        solution()


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=int(8000))
