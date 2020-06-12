from os.path import ( join )
from typing import ( Dict, List, Optional, Tuple )

COVID19RU_ROOT=join('..','csse_covid_19_data','csse_covid_19_daily_reports')
COVID19RU_TSROOT=join('..','csse_covid_19_data','csse_covid_19_time_series')
COVID19RU_PENDING=join('..','pending')

# Format: (EN_OLD, RU, EN_CORRECTED)
REGIONS:List[Tuple[str,str,str]]=[
  ('Moscow','Москва', "Moscow"),
  ('Saint Petersburg','Санкт-Петербург', "Saint Petersburg"),
  ('Moscow oblast','Московская область', "Moscow Oblast"),
  ('Samara oblast','Самарская область', "Samara Oblast"),
  ("Saha republic","Республика Саха (Якутия)", "Sakha (Yakutiya) Republic"),
  ("Sverdlov oblast","Свердловская область", "Sverdlovsk Oblast"),
  ("Kaliningrad oblast","Калининградская область", "Kaliningrad Oblast"),
  ("Kirov oblast","Кировская область", "Kirov Oblast"),
  ("Novosibirsk oblast","Новосибирская область", "Novosibirsk Oblast"),
  ("Krasnoyarskiy kray","Красноярский край", "Krasnoyarsk Krai"),
  ("Tambov oblast","Тамбовская область", "Tambov Oblast"),
  ("Lipetsk oblast","Липецкая область", "Lipetsk Oblast"),
  ("Tver oblast","Тверская область", "Tver Oblast"),
  ("Habarovskiy kray","Хабаровский край", "Khabarovsk Krai"),
  ("Tumen oblast","Тюменская область", "Tyumen Oblast"),
  ("Tula oblast","Тульская область", "Tula Oblast"),
  ("Perm oblast","Пермский край", "Perm Krai"),
  ("Nizhegorodskaya oblast","Нижегородская область", "Nizhny Novgorod Oblast"),
  ("Krasnodarskiy kray","Краснодарский край", "Krasnodar Krai"),
  ("Voronezh oblast","Воронежская область", "Voronezh Oblast"),
  ("Kemerovo oblast","Кемеровская область", "Kemerovo Oblast"),
  ("Republic of Hakassia","Республика Хакасия", "Khakassia Republic"),
  ("Murmansk oblast","Мурманская область", "Murmansk Oblast"),
  ("Komi republic","Республика Коми", "Komi Republic"),
  ("Kaluga oblast","Калужская область", "Kaluga Oblast"),
  ("Ivanovo oblast","Ивановская область", "Ivanovo Oblast"),
  ("Zabaykalskiy kray","Забайкальский край", "Zabaykalsky Krai"),
  ("Tomsk oblast","Томская область", "Tomsk Oblast"),
  ("Arkhangelsk oblast","Архангельская область","Arkhangelsk Oblast"),
  ("Ryazan oblast","Рязанская область", "Ryazan Oblast"),
  ("Republic of Chuvashia","Чувашская Республика", "Chuvashia Republic"),
  ("Ulianovsk oblast","Ульяновская область", "Ulyanovsk Oblast"),
  ("Yaroslavl oblast","Ярославская область", "Yaroslavl Oblast"),
  ("Pensa oblast","Пензенская область", "Penza Oblast"),
  ("Belgorod oblast","Белгородская область", "Belgorod Oblast"),
  ("Hanty-Mansiyskiy AO","Ханты-Мансийский АО", "Khanty-Mansi Autonomous Okrug"),
  ("Leningradskaya oblast","Ленинградская область", "Leningrad Oblast"),
  ("Orenburg oblast","Оренбургская область", "Orenburg Oblast"),
  ("Saratov oblast","Саратовская область", "Saratov Oblast"),
  ("Republic of Tatarstan","Республика Татарстан", "Tatarstan Republic"),
  ("Kurgan oblast","Курганская область", "Kurgan Oblast"),
  ("Republic of Kabardino-Balkaria","Кабардино-Балкарская Республика","Kabardino-Balkarian Republic"),
  ("Cheliabinsk oblast","Челябинская область", "Chelyabinsk Oblast"),
  ("Stavropolskiy kray","Ставропольский край", "Stavropol Krai"),
  ("Briansk oblast","Брянская область", "Bryansk Oblast"),
  ("Republic of Udmurtia","Удмуртская Республика", "Udmurt Republic"),
  ("Novgorod oblast","Новгородская область", "Novgorod Oblast"),
  ("Republic of Crimea","Республика Крым", "Crimea Republic"),
  ("Republic of Bashkortostan","Республика Башкортостан", "Bashkortostan Republic"),
  ("Chechen republic","Чеченская Республика", "Chechen Republic"),
  ("Primorskiy kray","Приморский край", "Primorsky Krai"),
  ("Volgograd oblast","Волгоградская область", "Volgograd Oblast"),
  ("Orel oblast","Орловская область", "Orel Oblast"),
  ("Pskov oblast","Псковская область", "Pskov Oblast"),
  ("Rostov oblast","Ростовская область", "Rostov Oblast"),
  ("Republic of Buriatia","Республика Бурятия", "Buryatia Republic"),
  ("Republic of Mordovia","Республика Мордовия", "Mordovia Republic"),
  ("Republic of Dagestan","Республика Дагестан", "Dagestan Republic"),
  ("Sakhalin oblast","Сахалинская область", "Sakhalin Oblast"),
  ("Kostroma oblast","Костромская область", "Kostroma Oblast"),
  ("Smolensk oblast","Смоленская область", "Smolensk Oblast"),
  ("Republic of Adygeia","Республика Адыгея","Adygea Republic"),
  ("Omsk oblast","Омская область", "Omsk Oblast"),
  ("Irkutsk oblast","Иркутская область", "Irkutsk Oblast"),
  ("Amursk oblast","Амурская область", "Amur Oblast"),
  ("Altayskiy kray","Алтайский край", "Altai Krai"),
  ("Vladimir oblast","Владимирская область", "Vladimir Oblast"),
  ("Vologda oblast","Вологодская область", "Vologda Oblast"),
  ("Republic of Kalmykia","Республика Калмыкия", "Kalmykia Republic"),
  ("Republic of Mariy El","Республика Марий Эл", "Mari El Republic"),
  ("Republic of Chuvashia","Республика Чувашия", "Chuvashia Republic"),
  ("Astrahan oblast","Астраханская область", "Astrakhan Oblast"),
  ("Magadan oblast","Магаданская область", "Magadan Oblast"),
  ("Sevastopol","Севастополь", "Sevastopol"),
  ("Kursk oblast","Курская область", "Kursk Oblast"),
  ("Republic of North Osetia - Alania","Республика Северная Осетия — Алания", "North Ossetia - Alania Republic"),
  ("Yamalo-Nenetskiy AO","Ямало-Ненецкий автономный округ", "Yamalo-Nenets Autonomous Okrug"),
  ("Ingushetia republic","Республика Ингушетия", "Ingushetia Republic"),
  ("Jewish Autonomous oblast","Еврейская автономная область", "Jewish Autonomous Okrug"),
  ("Kamchatskiy kray","Камчатский край", "Kamchatka Krai"),
  ("Republic of Karelia", "Республика Карелия", "Karelia Republic"),
  ("Republic of Karachaevo-Cherkessia", "Карачаево-Черкесская Республика","Karachay-Cherkess Republic"),
  ("Republic of Tyva", "Республика Тыва", "Tyva Republic"),
  ("Nenetskiy autonomous oblast", "Ненецкий автономный округ", "Nenets Autonomous Okrug"),
  ("Chukotskiy autonomous oblast", "Чукотский автономный округ", "Chukotka Autonomous Okrug"),
  ("Altay republic", "Республика Алтай", "Altai Republic"),
]

Lat=float
Lon=float

# FIXME: incomplete
LOCATION:Dict[str,Tuple[Lat,Lon]]={
  "Moscow":(55.75222, 37.61556),
  "Saint Petersburg":(59.93863, 30.31413),
  "Moscow oblast":(55.81363, 36.71631),
  "Samara oblast":(53.20007, 50.15),
  "Saha republic":(62.30161, 32.68536),
  "Sverdlov oblast":(43.25, 71.75),
  "Kaliningrad oblast":(54.70649, 20.51095),
  "Kirov oblast":(58.59665, 49.66007),
  "Novosibirsk oblast":(55.0415, 82.9346),
  "Krasnoyarskiy kray":(58.0, 93.0),
  "Tambov oblast":(52.73169, 41.44326),
  "Lipetsk oblast":(52.60311, 39.57076),
  "Tver oblast":(56.85836, 35.90057),
  "Habarovskiy kray":(48.48271,135.08379),
  "Tumen oblast":(57.15222, 65.52722),
  "Tula oblast":(54.19609, 37.61822),
  "Perm oblast":(58.01046, 56.25017),
  "Nizhegorodskaya oblast":(56.32867, 44.00205),
  "Krasnodarskiy kray":(44.98811, 38.97675),
  "Voronezh oblast":(51.67204, 39.1843),
  "Kemerovo oblast":(55.33333, 86.08333),
  "Republic of Hakassia":(53.71556, 91.42917),
  "Murmansk oblast":(68.97917, 33.09251),
  "Komi republic":(64.0, 54.0),
  "Kaluga oblast":(54.5293, 36.27542),
  "Ivanovo oblast":(56.99719, 40.97139),
  "Zabaykalskiy kray":(52.0, 117.0),
  "Tomsk oblast":(56.49771, 84.97437),
  "Arkhangelsk oblast":(64.0, 44.0),
  "Ryazan oblast":(54.6269, 39.6916),
  "Republic of Chuvashia":(56.13222, 47.25194),
  "Ulianovsk oblast":(54.32824, 48.38657),
  "Yaroslavl oblast":(57.62987, 39.87368),
  "Pensa oblast":(53.20066, 45.00464),
  "Belgorod oblast":(50.61074, 36.58015),
  "Hanty-Mansiyskiy AO":(61.00417, 69.00194),
  "Leningradskaya oblast":(60.0, 32.0),
  "Orenburg oblast":(51.7727, 55.0988),
  "Saratov oblast":(51.54056, 46.00861),
  "Republic of Tatarstan":(55.33333, 51.0),
  "Kurgan oblast":(55.45, 65.33333),
  "Republic of Kabardino-Balkaria":(43.355, 42.43917),
  "Cheliabinsk oblast":(55.15402, 61.42915),
  "Stavropolskiy kray":(45.0, 44.0),
  "Briansk oblast":(53.25209, 34.37167),
  "Republic of Udmurtia":(57.0, 53.0),
  "Novgorod oblast":(56.32867, 44.00205),
  "Republic of Crimea":(45.0, 34.0),
  "Republic of Bashkortostan":(54.0, 56.0),
  "Chechen republic":(43.2, 45.78889),
  "Primorskiy kray":(45.0, 135.0),
  "Volgograd oblast":(48.71939, 44.50183),
  "Orel oblast":(52.96508, 36.07849),
  "Pskov oblast":(57.8136, 28.3496),
  "Rostov oblast":(47.23135, 39.72328),
  "Republic of Buriatia":(54.54, 112.348699),
  "Republic of Mordovia":(54.20, 44.319669),
  "Republic of Dagestan":(42.26, 47.095742),
}

# Default location: somehwere in Russia
LOCATION_DEF=(61.52401,105.31875600000001)



CSSE2_HEADER=('FIPS,Admin2,Province_State,Country_Region,Last_Update,Lat,Long_,'
              'Confirmed,Deaths,Recovered,Active,Combined_Key')

