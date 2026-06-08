class Config:
    BASE_URL =  "https://www.saucedemo.com"
    USERS = {
        "standard":{
            "username": "standard_user",
            "password": "secret_sauce"
        },
        "locked":{
            "username": "locked_out_user",
            "password": "secret_sauce"
        },
        "invalid":{
            "username": "wrong_user",
            "password": "wrong_password"
        }
    }

    TIMEOUT = 30000 #timeout for 30 seconds