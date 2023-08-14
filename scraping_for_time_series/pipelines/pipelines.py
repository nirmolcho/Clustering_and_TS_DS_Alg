from data_models.product import Product


class Pipeline:
    def __init__(self):
        self.max_elements_to_collect = None
        self.search_term = None
        self.feed_items = []
        self.user_bio_data = []
        self.num_of_elements_collected = 0
        self.user_urls = []
        self.visited_urls = []

    @staticmethod
    def get_user_inputs():
        search_term = input("Enter the search term: ")
        return search_term

    @staticmethod
    def get_user_email():
        user_email = input("Enter the email: ")
        return user_email

    @staticmethod
    def get_user_password():
        user_password = input("Enter the password: ")
        return user_password

    @staticmethod
    def get_max_elements_to_collect():
        max_elements_to_collect = input("Enter the max number of elements to collect: ")
        return max_elements_to_collect

    @staticmethod
    def get_search_filter():
        options = ['People', 'Jobs', 'Posts']
        print("What do you want to filter? Choose from the following options:")

        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")

        choice = 0
        while choice not in range(1, len(options) + 1):
            try:
                choice = int(input("Enter the number of your choice: "))
                if choice not in range(1, len(options) + 1):
                    print("Invalid choice! Please choose a number between 1 and 3.")
            except ValueError:
                print("Please enter a valid number.")

        print(f"You chose to filter {options[choice - 1]}.")
        return options[choice - 1]

    def process_item(self, item):
        processed_item = self.clean_item(item)
        self.store_item(processed_item)
        return processed_item

    def clean_item(self, item):
        cleaned_item = item
        return cleaned_item

    def store_item(self, item):
        pass

