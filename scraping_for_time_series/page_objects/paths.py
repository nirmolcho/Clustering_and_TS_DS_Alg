class PathsFunctions:

    # main website element
    @staticmethod
    def main_element_XPATH():
        path2 = ("//body/div[@class='application-outlet']/div[@class='authentication-outlet']/div["
                 "@id='voyager-feed']/div[@id='ember21']/div[2]/div[1]/div[1]")
        return path2

    @staticmethod
    def main_element_CSS_SELECTOR():
        path = '.scaffold-layout__row.scaffold-layout__content'
        return path

    @staticmethod
    def search_general_XPATH():
        path2 = "//input[@placeholder='Search']"
        return path2

    @staticmethod
    def search_general_CSS_SELECTOR():
        path = "input[placeholder='Search']"
        return path

    @staticmethod
    def username_XPATH():
        path2 = '//div[@class="text-input flex"]/input[@id="session_key"]'
        return path2

    @staticmethod
    def username_CSS_SELECTOR():
        path = "div.text-input.flex > input#session_key"
        return path

    @staticmethod
    def password_XPATH():
        path2 = "//input[@id='session_password']"
        return path2

    @staticmethod
    def password_CSS_SELECTOR():
        path = "#session_password"
        return path

    @staticmethod
    def posts_search_element_XPATH():
        path = ""
        return path

    @staticmethod
    def posts_search_element_CSS_SELECTOR():
        path = ""
        return path




