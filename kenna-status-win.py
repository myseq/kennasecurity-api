#!/usr/bin/python3
# -*- coding: utf-8 -*-

from colorama import Fore, Style

import requests, json
from bs4 import BeautifulSoup
from datetime import datetime
from timeit import default_timer as timer

verbose=True

banner = f"""
   Zzzzz   |\      _,,,---,,_   
           /,`.-'`'    -.  ;-;;,_    __author__ : [ zd ]            
          |,4-  ) )-,_..;\ (  `'-'   __year__   : [ 2020 ]
         '---''(_/--'  `-'\_)        __file__   : [ {__file__} ]          
"""

def cjson(link):

    try:
        resp = requests.get(link)
        resp.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(f'HTTP Error : {err}')
    except requests.exceptions.RequestException as err:
        raise SystemExit(f'Req Error : {err}')
    except requests.exceptions.ConnectionError as err:
        raise SystemExit(f'Connection Error : {err}')
    else:
        return json.loads(resp.text)

def chtml(link):

    try:
        resp = requests.get(link)
        resp.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(f'HTTP Error : {err}')
    except requests.exceptions.RequestException as err:
        raise SystemExit(f'Req Error : {err}')
    except requests.exceptions.ConnectionError as err:
        raise SystemExit(f'Connection Error : {err}')
    else:
        return resp.text

def main():
    """ main() function that calls different function accordingly  """

    print(f'{banner}')

    url = 'https://status.kennasecurity.com/api/v2/status.json'

    start = timer()
    today = datetime.today().strftime('%Y-%m-%d %H:%M')
    print(f'\n[{today}] Checking {url}....\n\n ')

    kenna = cjson(url)

    if kenna:
        kpage = kenna.get('page')
        k_id = kpage.get('id')
        k_name = kpage.get('name')
        k_url = kpage.get('url')
        k_tz = kpage.get('time_zone')
        k_upd = kpage.get('updated_at')
        k_last = datetime.strptime(k_upd[:18], '%Y-%m-%dT%H:%M:%S')
        kstat = kenna.get('status')
        k_ind = kstat.get('indicator')
        k_desc = kstat.get('description')

        print(f' * Name/URL : {k_name} ({k_id}) - [{k_url}]')
        print(f' * Status : [ {k_desc}/{k_ind} ]  (Last update : {k_last} / TZ : {k_tz})')

    if verbose:
        url = 'https://status.kennasecurity.com'
        html = chtml(url) 

        if html:
            soup = BeautifulSoup(html, features="lxml")
            divparent = soup.find_all('div', attrs={'class' : 'legend legend-group'})
            us = divparent[0]
            eu = divparent[1]
            us_percent = us.find_all('span', attrs = {'id' : 'uptime-percent-cp6vzmx7n1sy'})[0].text.strip()
            eu_percent = eu.find_all('span', attrs = {'id' : 'uptime-percent-0mftzddf2xk9'})[0].text.strip()
            print(f'')
            print(f'   ** US : {float(us_percent):.2f}% uptime (past 90 days)')
            print(f'   ** EU : {float(eu_percent):.2f}% uptime (past 90 days)')

    end = timer()
    print(f'\n ** Completed within [{end-start:.2f} sec].\n')

if __name__ == "__main__":
    main()


