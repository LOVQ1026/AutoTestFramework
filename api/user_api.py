from api.api_client import ApiClient



class UserApi:


    def __init__(self):

        self.client = ApiClient()



    def get_github_user(self):


        url = (
            "https://api.github.com/user"
        )


        return self.client.get(
            url
        )