from pipelines.elements_actions import FindElements


class WindowPopUP:
    def __init__(self, driver):
        self.driver = driver
        self.element = FindElements(self.driver)

    @staticmethod
    def exit_popup(self):
        path = '//div[@data-e2e="modal-close-inner-button]"'
        return path

    @staticmethod
    def popup_exists():
        path = '//div[@data-e2e="login-modal"]"'
        return path

    def check_if_popup_exists(self, element_):
        try:
            self.element.check_if_element_exist_with_XPATH(self.popup_exists)
        except Exception as e:
            print("Exception occurred: ", str(e))

    def close_popup(self, element_):
        try:
            self.element.click_using_XPATH(self.exit_popup)
        except Exception as e:
            print("Exception occurred: ", str(e))