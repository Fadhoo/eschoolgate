API endpoints
Basic
    /rest-auth/login/ (POST)
    args -
        username
        email
        password

    Returns Token key

    /rest-auth/logout/ (POST) - logout

    /rest-auth/password/reset/ (POST)
    args -
        email

    /rest-auth/password/reset/confirm/ (POST)
    args -
        uid
        token
        new_password1
        new_password2

    /rest-auth/password/change/ (POST)
    args -
        new_password1
        new_password2

    /rest-auth/user/ (GET, PUT, PATCH)
    args -
        username
        first_name
        last_name
    Returns
        pk, username, email, first_name, last_name

Registration

    /rest-auth/registration/ (POST)
    args -
        username
        password1
        password2
        email

    /rest-auth/registration/verify-email/ (POST)
    args -
        key
        Social Media Authentication
        Basing on example from installation section Installation

    /rest-auth/facebook/ (POST)
    args -
        access_token
        code