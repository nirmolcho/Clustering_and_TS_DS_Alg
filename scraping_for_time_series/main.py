from spiders.login_spider import LoginSpider
from utils.driver_manager import DriverManager
from utils.scheduler import Scheduler
from pipelines.pipelines import Pipeline
from page_objects.login_page import LoginPage

driver_manager = DriverManager('/Applications/Brave Browser.app/Contents/MacOS/Brave Browser')
driver_manager.start_drivers()

pipeline = Pipeline()

spider = LoginSpider(driver_manager.get_driver())

scheduler = Scheduler()
login_page = LoginPage(driver_manager.get_driver())

pipeline.get_max_elements_to_collect()
search_term = pipeline.get_user_inputs()
search_filter = pipeline.get_search_filter()


spider.login_website()
spider.login_user()
login_page.search(search_term)

#scheduler.schedule(spider.login(search_term), '1m')
#scheduler.schedule(spider.search(search_term), '1m')


scheduler.start()

driver_manager.quit_drivers()
