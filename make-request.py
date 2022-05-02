# ~~~ make-request.py ~~~
import requests

# route 1 -- ping
def call_ping_route():
  ''' Execute ping request '''
  r = requests.get("http://localhost:5555/ping") # make the request
  return r



urls = [ # all stolen from https://phishingquiz.withgoogle.com/ on 2022-04-27
  'https://drive--google.com/luke.johnson',
  'https://efax.hosting.com.mailru382.co/efaxdelivery/2017Dk4h325RE3',
  'https://drive.google.com.download-photo.sytez.net/AONh1e0hVP',
  'https://www.dropbox.com/buy',
  'westmountdayschool.org',
  'https://myaccount.google.com-securitysettingpage.ml-security.org/signonoptions/',
  'https://google.com/amp/tinyurl.com/y7u8ewlr',
  'www.tripit.com/uhp/userAgreement'
]

data_to_send = {'domains':urls}

def call_predict_route(urls):

    try:
        r = requests.post('http://localhost:5050/predict', data = data_to_send)
    except requests.exceptions.HTTPError as err:
        print('there was an HTTPerror:' + str(err))
      #    2. Check the request for errors; handle (print) errors if so
      #    3. Assuming no errors, print the predicted response
    pass


route_callers = [
  call_predict_route
  ]

# call route on list of all urls
call_predict_route(urls)
