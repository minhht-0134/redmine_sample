import crawl_data
# import export_to_database
from datetime import datetime
import warning_chatwork

LINK_URL = 'https://dev.sun-asterisk.com/projects/groupnet/issues?query_id=8061'


if __name__ == '__main__':
    data = crawl_data.crawl_data(LINK_URL)
    file_name = "demo_{0}.xlsx".format(datetime.now().timestamp())
    # export_to_database.update_database(data)
    warning_chatwork.handler(data=data)
