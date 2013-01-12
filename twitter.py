
import twitter
import oauth2

CONSUMER_KEY = '2k0c8ZNbvAIwuaf5LL0x3g'
CONSUMER_SECRET = 'kI4NcGW9hpuiNavcnDz2flWppsRWFnCw1zq4Tw39lE'
ACCESS_KEY = '997135112-H77CM2cCqKoeKCzUsLyJeQLIiecxxEXGZVurEzhpf'
ACCESS_SECRET = 'fusON27CDvAktnWJPVX9OyG68XQbb7y7nqGEjHSw'

api = twitter.Api( 
    consumer_key = CONSUMER_KEY,
    consumer_secret = CONSUMER_SECRET,
    access_token_key = ACCESS_KEY,
    access_token_secret = ACCESS_SECRET)

tl = api.GetUserTimeLine(id='null_poga')

for i in tl:
    print i.text
