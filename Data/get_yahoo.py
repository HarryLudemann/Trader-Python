# Get Product Page Links
import requests
from bs4 import BeautifulSoup


baseurl = 'https://finance.yahoo.com/trending-tickers?soc_src=mail&soc_trk=ma'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}


def get_yahoo_trending():
    """
    Scrapes trending tickers and infomation from yahoo.com
    :return list of dictionary's:
    """
    ticker_infomation = []                                     # list to store all the ticker information

    r = requests.get(baseurl)                                  # get the page                  
    soup = BeautifulSoup(r.content, 'lxml')                    # parse the page
    tickers = soup.find_all('td', class_='Va(m)')              # get all the tickers and infomation
    r.close()                                                  # close the connection

    tickers = [str( x.text ).strip() for x in tickers]         # Remove leading and trailing spaces

    for i in range(0, len(tickers), 8):                        # Split into  list of 8
        for item in tickers[i:i+8]:                            # iterate over list
            if item == '':                                     # if item empty Remove empty                                
                tickers.remove(item)

    for i in range(0, len(tickers), 8):                        # Split into  list of 8
        ticker_info = {
            'Ticker': tickers[0::8],
            'Name': tickers[1::8],
            'Last Price': tickers[2::8],
            'Market Time': tickers[3::8],
            'Change': tickers[4::8],
            'Percent Change': tickers[5::8],
            'Volume': tickers[6::8],
            'Market Cap': tickers[7::8]
        }
        ticker_infomation.append(ticker_info)

    return ticker_infomation


if __name__ == '__main__':
    trending_tickers = get_trending_tickers()       # get the trending tickers

    print( str( len( trending_tickers ) ) + ' Trending Tickers Found' )     # total number of trending tickers should be 30
