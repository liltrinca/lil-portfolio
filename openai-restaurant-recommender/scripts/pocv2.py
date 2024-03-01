import pandas as pd

from datetime import datetime
import hashlib

import geopy as geo
from geopy.geocoders import ArcGIS

from math import radians, cos, sin, asin, sqrt

def get_map(address):
    address = address
    geolocator = ArcGIS(timeout=5)
    try_count = 0
    while try_count < 5:
        try:
            location = geolocator.geocode(address)
            break
        except geo.exc.GeocoderUnavailable as e:
            location = None
            try_count += 1
    lat, long = location.latitude, location.longitude

    df = pd.DataFrame([[address,lat,long]], columns=["end","lat","long"])

    return df


def get_df(address, radius):
    address = address
    geolocator = ArcGIS(timeout=5)
    try_count = 0
    while try_count < 5:
        try:
            location = geolocator.geocode(address)
            break
        except geo.exc.GeocoderUnavailable as e:
            location = None
            try_count += 1
    lat, long = location.latitude, location.longitude

    def distance_d(distance_df, LaA=lat, LoA=long):
        LoA = radians(LoA)
        LoB = radians(distance_df['num_longitude'])
        LaA = radians(LaA)
        LaB = radians(distance_df['num_latitude'])

        D_Lo = LoB - LoA
        D_La = LaB - LaA
        P = sin(D_La / 2) ** 2 + cos(LaA) * cos(LaB) * sin(D_Lo / 2) ** 2

        Q = 2 * asin(sqrt(P))

        R_km = 6371

        return (Q * R_km)

    def split_date(row, form):
        return datetime.strftime(datetime.strptime(row, '%Y-%m-%dT%H:%M:%S.000Z'), form)

    df = pd.read_csv('data/amostra_brasilia.csv')

    df = df[((df['num_longitude'] >= long - (radius / 100)) & (df['num_longitude'] <= long + (radius / 100))) &
            ((df['num_latitude'] >= lat - (radius / 100)) & (df['num_latitude'] <= lat + (radius / 100)))]

    df['distancia'] = df.apply(distance_d, axis=1)

    df['ano'] = df.apply(lambda x: split_date(x['dat_transacao'], '%Y'), axis=1)
    df['mes'] = df.apply(lambda x: split_date(x['dat_transacao'], '%m'), axis=1)
    df['dia'] = df.apply(lambda x: split_date(x['dat_transacao'], '%d'), axis=1)
    df['hora'] = df.apply(lambda x: split_date(x['dat_transacao'], '%H'), axis=1)
    df['cd_dia_da_semana'] = df.apply(lambda x: split_date(x['dat_transacao'], '%w'), axis=1)
    df['ds_dia_da_semana'] = df.apply(lambda x: split_date(x['dat_transacao'], '%a'), axis=1)

    df['srk_trabalhador_conta'] = df['srk_trabalhador_conta'].astype(str)
    df['srk_trabalhador_conta'] = df['srk_trabalhador_conta'].apply(lambda x: hashlib.sha256(x.encode()).hexdigest())

    df['num_cnpj'] = df['num_cnpj'].astype(str)
    df['num_cnpj'] = df['num_cnpj'].apply(lambda x: hashlib.sha256(x.encode()).hexdigest())

    df.drop(['dsc_nome_fantasia', 'val_saldo_anterior',
             'num_latitude', 'num_longitude', 'srk_ec_cadastro'],
            axis=1, inplace=True)

    df.rename(columns={'srk_trabalhador_conta': 'beneficiado', 'num_cnpj': 'estabelecimento'}, inplace=True)

    return df