# short-uuid-flask

Attention: this project is for demo purposes only and is not intended for use in production environments.

I created this project to mess around with creating a tiny web service in [Flask](https://flask.palletsprojects.com/en/2.0.x/) and demonstrate generating short [base64](https://docs.python.org/3/library/base64.html) encoded [uuid](https://docs.python.org/3/library/uuid.html) ([RFC 4122](https://datatracker.ietf.org/doc/html/rfc4122.html)) strings.

## Short UUID Strings

A goal of this project is to produce short strings. The core of this demo is the following one-liner:

`base64.urlsafe_b64encode(uuid.uuid4().bytes).decode('utf-8')[:-2]`

The output is a 22 character string, which is not bad considering that the uuid is 16 raw bytes (`len(uuid.uuid4().bytes)`) and, of course, 32 hexadecimal chars (`len(uuid.uuid4().hex)`.)

In brief,

* `base64` encoding is used because it's fewer chars than hexidecimal
* `urlsafe_b64encode` is used so that the output can be used in urls and filenames
* `utf-8` is the output encoding
* `[:-2]` strips the `==` suffix

If all you want is short uuid strings without any of the Flask wrapper, this is all you need.

## Security Considerations

Absolutely no security measures are provided for this demo. Some options to consider:

* [Flask app config](https://flask.palletsprojects.com/en/2.0.x/config/) provides an option to use a secret key for user session data
* [OAuthLib](https://oauthlib.readthedocs.io/en/latest/) can be used to integrate with SSO such as Google Signin, [tutorials are online](https://realpython.com/flask-google-login/)
* [PyJWT](https://pyjwt.readthedocs.io/en/latest/) can be used to build a service that issues ssl signed bearer tokens ([JWTs](https://jwt.io/), [RFC 7519](https://datatracker.ietf.org/doc/html/rfc7519))
