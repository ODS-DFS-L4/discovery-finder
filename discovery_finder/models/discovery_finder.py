import pandas as pd

from typing import List, Dict  # noqa: F401


class Singleton(object):
    _instances = dict()
    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = object.__new__(cls, *args, **kwargs)
            cls._instances[cls]._read()
        return cls._instances[cls]


DISCOVERY_SERVICE_COLUMNS = ['domain', 'url']

class DiscoveryServiceDB(Singleton):

    def _read(self) -> pd.DataFrame:
        # ファイルを読み込めればそれをメモリに格納する
        try:
            self.df = pd.read_csv('/data/discovery_service_db.csv', index_col=None)
            return
        except:
            pass
        self.df = pd.DataFrame(columns=DISCOVERY_SERVICE_COLUMNS)

    def _write(self):
        self.df.to_csv('discovery_service_db.csv', index=False)

    def create(self, domain: str, url: str):
        # self._read()
        self.delete(domain)

        new_df = pd.DataFrame(
            [[domain, url]],
            columns=DISCOVERY_SERVICE_COLUMNS)
        self.df = pd.concat([self.df, new_df], ignore_index=False)
        self.df = self.df.reset_index(drop=True)
        # self._write()  # デモでは書き込まない

    def delete(self, domain: str):
        # self._read()
        service = self.df[self.df['domain'] == domain]
        if len(service):
            self.df = self.df.drop(service.index, axis=0)
        # self._write()  # デモでは書き込まない

    def get(self, domain: str) -> str:
        # df = self._read()
        service = self.df[self.df['domain'] == domain]
        if len(service):
            return [[service['url'].iloc[0], domain]]
        return []

    def all(self) -> List[str]:
        # df = self._read()
        service_list = []
        for i in range(len(self.df)):
            row = self.df.iloc[i]
            service_list.append({
                'domain': row['domain'],
                'url': row['url']})
        return service_list

