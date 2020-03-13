from bs4 import BeautifulSoup
from authen import login
import export_to_database

session = login()


def crawl_data(link):
    page = 1
    report_data = []
    print('Start crawl data ...')
    while True:
        print("Parsing page=%s" % (page))
        response = session.get(link)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.select_one('h2').string
        trs = soup.select('table.issues > tbody > tr')

        pagination = soup.select_one('span.pagination > ul.pages > li.next')
        has_next = False
        if pagination and 'page' in pagination.attrs['class']:
            has_next = True

        print("Get info of %s issues" % len(trs))
        for tr in trs:

            try:
                _classes = tr.attrs['class']
            except:
                print(tr)
            if 'parent' not in _classes:
                # time
                issue = tr
                if issue:
                    id = issue.select_one('td.id > a').string
                    tracker = issue.select_one('td.tracker').string
                    status = issue.select_one('td.status').string
                    priority = issue.select_one('td.priority').string
                    subject = issue.select_one('td.subject > a').string

                    assigned_to = issue.select_one('td.assigned_to')
                    if not assigned_to:
                        assigned_to = ''
                    else:
                        assigned_to = assigned_to.string

                    report_data_item = {
                        'id': id,
                        'tracker': tracker,
                        'status': status,
                        'priority': priority,
                        'subject': subject,
                        'assigned_to': assigned_to,
                    }

                    report_data.append(report_data_item)

        if not has_next:
            break
        else:
            page = page + 1
    print('Crawl data completed!')
    return report_data


if __name__ == '__main__':
    url = 'https://dev.sun-asterisk.com/projects/groupnet/issues?query_id=8061'
    data = crawl_data(url)
    export_to_database.update_database(data)
