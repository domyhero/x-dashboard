import argparse
import httplib2


from apiclient import discovery
from oauth2client import file
from oauth2client import client
from oauth2client import tools

from apiclient.errors import HttpError
from oauth2client.client import AccessTokenRefreshError

# Parser for command-line arguments.
parser = argparse.ArgumentParser(
    description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter,
    parents=[tools.argparser])


# CLIENT_SECRETS is name of a file containing the OAuth 2.0 information for this
# application, including client_id and client_secret. You can see the Client ID
# and Client secret on the APIs page in the Cloud Console:
# <https://cloud.google.com/console#/project/260257625081/apiui>
CLIENT_SECRETS = 'client_secrets.json'

# Set up a Flow object to be used for authentication.
# Add one or more of the following scopes. PLEASE ONLY ADD THE SCOPES YOU
# NEED. For more information on using scopes please see
# <https://developers.google.com/+/best-practices>.
FLOW = client.flow_from_clientsecrets(CLIENT_SECRETS,
  scope=[
      'https://www.googleapis.com/auth/analytics',
      'https://www.googleapis.com/auth/analytics.readonly',
    ],
    message=tools.message_if_missing(CLIENT_SECRETS))

flags = parser.parse_args()

# If the credentials don't exist or are invalid run through the native client
# flow. The Storage object will ensure that if successful the good
# credentials will get written back to the file.
storage = file.Storage('sample.dat')
credentials = storage.get()
if credentials is None or credentials.invalid:
  credentials = tools.run_flow(FLOW, storage, flags)

# Create an httplib2.Http object to handle our HTTP requests and authorize it
# with our good Credentials.
http = httplib2.Http()
http = credentials.authorize(http)

# Construct the service object for the interacting with the Google Analytics API.
service = discovery.build('analytics', 'v3', http=http)

profile_id = u'74539311'
import time
today = time.strftime('%Y-%m-%d', time.localtime(time.time()))
pv_results = service.data().ga().get(
      ids='ga:' + profile_id,
      start_date=today,
      end_date=today,
      metrics='ga:pageviews').execute()

uv_results = service.data().ga().get(
      ids='ga:' + profile_id,
      start_date=today,
      end_date=today,
      metrics='ga:visits').execute()

print pv_results.get('rows')[0][0]
print uv_results.get('rows')[0][0]
# more metrics: ga:visits, ga:timeOnPage, ga:pageLoadTime, ga:pageviews

try:
  print "Success! Now add code here."

except client.AccessTokenRefreshError:
  print ("The credentials have been revoked or expired, please re-run"
    "the application to re-authorize")

