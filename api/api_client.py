from common.request import RequestClient



class ApiClient:


    def __init__(self):

        self.request = RequestClient()



    def get(
            self,
            url,
            params=None
    ):

        return self.request.get(
            url,
            params
        )



    def post(
            self,
            url,
            json=None
    ):

        return self.request.post(
            url,
            json
        )