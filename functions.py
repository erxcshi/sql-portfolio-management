import pandas as pd
import yfinance as yf


def update_port(asset_list):
    pass


def calc_vol(portfolio_name, portfolio_df):
    pass


def create_port(tickers_list, port_name, period):

    asset_info = []
    historical_prices = []

    for ticker in tickers_list:
        # create portfolio table
        dct = yf.Ticker(ticker).info
        df = pd.DataFrame([{'Ticker': ticker, 'Asset Type': dct['quoteType'], 'Asset Name': dct['shortName'], 'Portfolio': port_name, 'Portfolio Count': len(tickers_list)}])
        asset_info.append(df)

        # create historical asset pricing
        prices = yf.download('AAPL', period=period, auto_adjust=True).to_dict()
        # create column with ticker name, reordering, and creating dataframe
        prices['Ticker'] = ticker
        df = pd.DataFrame(prices)
        val = df.pop('Ticker')
        df.insert(0, 'Ticker', val)
        # append series into a list
        historical_prices.append(df)

    return pd.concat(asset_info), pd.concat(historical_prices)


