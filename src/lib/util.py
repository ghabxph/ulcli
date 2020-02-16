import json


def response(lang, res, debug=False):

    # If we set debug = true, we'll simply return the status code and raw text
    if debug:
        return res.text

    j_res = None

    try:
        # Tries to convert response to json
        j_res = res.json()
    except json.JSONDecodeError:
        # We set j_res to empty dict in case there's error in decoding the expected json response
        j_res = {}

    finally:
        # If request succeeds
        if j_res.get('type') == 'success' and j_res.get('msg') is not None:
            print(j_res.get('msg'))

        # If request didn't succeed
        elif j_res.get('type') == 'error' and j_res.get('msg') is not None:
            print('Error: %s' % j_res.get('msg'))

        # If we triggered server error, or url is not valid
        else:
            print('Url: %s' % res.url)
            print('Status Code: %s' % str(res.status_code))
            print(lang.msg_err_insvr)

        return j_res
