                                            ##The METHODS

The method is the type of request you send to the server. You can choose from these five types below:

GET
POST
PUT
PATCH
DELETE


->These methods provide meaning for the request you’re making.
->They are used to perform four possible actions: Create, Read, Update and Delete (CRUD).

##NOTE
Each URL is called a request while the data sent back to you is called a response.



'''Method Name'''	                                            '''Request Meaning'''

GET	                     This request is used to get a resource from a server
                             If you perform a `GET` request, the server looks for the data you requested and sends it back to you.
                             In other words, a `GET` request performs a `READ` operation. This is the default request method.


POST	                    This request is used to create a new resource on a server. If you perform a `POST` request, the server
                            creates a new entry in the database and tells you whether the creation is successful.
                            In other words, a `POST` request performs an `CREATE` operation.


PUT and PATCH	            These two requests are used to update a resource on a server. If you perform a `PUT` or `PATCH` request,
                            the server updates an entry in the database and tells you whether the update is successful. In other words,
                            a `PUT` or `PATCH` request performs an `UPDATE` operation.

DELETE	                    This request is used to delete a resource from a server. If you perform a `DELETE` request, the server deletes
                            an entry in the database and tells you whether the deletion is successful. In other words, a `DELETE` request
                            performs a `DELETE` operation.



##                            HTTP Status Codes And Error Messages
Some of the messages you’ve received earlier, like “Requires authentication” and “Problems parsing JSON” are error messages.
They only appear when something is wrong with your request. HTTP status codes let you tell the status of the response quickly.
The range from 100+ to 500+. In general, the numbers follow the following rules:

200+                means the request has succeeded.
300+                means the request is redirected to another URL
400+                means an error that originates from the client has occurred
500+                means an error that originates from the server has occurred

