class CreatePortfolio:

    def __init__(self, name, assets: dict[str, int]):

        self.name = name
        self.assets = list(assets.keys())

        self.portfolio_price = sum(keys * values for keys, values in assets.items())

    def add_assets(self, tickers: dict[str, int]):
        for ticker in tickers.keys():
            if ticker not in self.assets:
                self.assets.append(ticker)
            else:
                print('This asset is already in the portfolio')

    def remove_asset(self, ticker):
        assert ticker in self
        pass


class Portfolios:
    def __init__(self, portfolios):

    def add_portfolio(self, name):
        pass

    def remove_portfolio(self, name):
