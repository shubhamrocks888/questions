##                        Authentication
You wouldn’t allow anyone to access your bank account without your permission, would you?
On the same line of thought, developers put measures in place to ensure you perform actions only when you’re authorized to do.
This prevents others from impersonating you.

Since POST, PUT, PATCH and DELETE requests alter the database, developers almost always put them behind an authentication wall.
In some cases, a GET request also requires authentication (like when you access your bank account to check your current balance, for example).

On the web, there are two main ways to authenticate yourself:
1.With a username and password (also called basic authentication)
2.With a secret token


The secret token method includes oAuth, which lets you to authenticate yourself with social media networks like Github, Google,
Twitter, Facebook, etc.

For this article, you’ll only learn to use basic authentication with a username and a password. If you’re interested in authenticating with oAuth,
I suggest reading “What You Need To Know About OAuth2 And Logging In With Facebook” by Zack Grossbart.

To perform a basic authentication with cURL, you can use the -u option, followed by your username and password, like this:
curl -x POST -u "username:password" https://api.github.com/user/repos


Try authenticating yourself with your username and password in the above request. Once you succeed in authentication, you’ll see the response change
from “Requires authentication” to “Problems parsing JSON.”

This is because you’ve yet to provide any data (which is required by all POST, PUT, PATCH and DELETE requests) to the server.

