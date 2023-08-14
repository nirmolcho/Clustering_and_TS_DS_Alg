

class GeneralFuncs:
    def get_scraperapi_url(self, url):
        """
            Converts url into API request for Scraper API.
        """
        payload = {'api_key': API_KEY, 'url': url}
        proxy_url = 'http://api.scraperapi.com/?' + urlencode(payload)
        return proxy_url

    @staticmethod
    def wrapper(func1, func2):
        if callable(func1) and callable(func2):
            try:
                return func1()
            except Exception as e:
                print(f"Function {func1.__name__} failed with error: {e}. Running function {func2.__name__}...")
                try:
                    return func2()
                except Exception as e:
                    print(f"Function {func2.__name__} also failed with error: {e}")
        else:
            return None

