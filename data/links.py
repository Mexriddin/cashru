import os


class Links:
    # HOST based on what environment
    HOST = ""
    if os.getenv("STAGE") == "dev":
        HOST = "https://dev-koshelek.ru"
    elif os.getenv("STAGE") == "prod":
        HOST = "https://koshelek.ru"

    # Pages addresses
    LOGIN_PAGE = f"{HOST}/authorization/login"
    SIGNUP_PAGE = f"{HOST}/authorization/signup"
    TRANSFERS_PAGE = f"{HOST}/transfers"
    BALANCE_PAGE = f"{HOST}/balance/wallets"
    P2P_PAGE = f"{HOST}/p2p"
    ACADEMY_PAGE = f"{HOST}/academy"

    PROFILE_PAGE = f"{HOST}/account/profile"