                      #The HEAD Method

->HEAD is almost identical to GET, but without the response body.

->In other words, if GET /users returns a list of users, then HEAD /users will make the same request
  but will not return the list of users.

->HEAD requests are useful for checking what a GET request will return before actually making a GET request -
  like before downloading a large file or response body.


                      'OR'

The HEAD method is identical to GET except that the server MUST NOT return a message-body in the response.
The metainformation contained in the HTTP headers in response to a HEAD request SHOULD be identical to the
information sent in response to a GET request.
