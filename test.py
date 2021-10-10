from datetime import date, timedelta, datetime
from pymongo import MongoClient
import san
from bson.objectid import ObjectId

client = MongoClient('mongodb://localhost:27017/')
db1 = client.geeksforgeeks
data = {}

with open("IndexCoins.idx") as openfileobject:
	for line in openfileobject:
		
		id = line.strip()
		try:
			print(id)
			
			for idx in range(7):
				daystr = str(date.today() - timedelta(days = idx))

				data['time'] = daystr

				data['_id'] = ObjectId()
				
				db1.Coll_santiment_Price.insert(data)
			try:
				daa = san.get("prices/" + id,
							from_date = "2020-08-20",
							to_date = "2020-08-27",
							interval = "1d")
				print(daa)
				
			except:
				print("URL error")
				continue;		
			for idx in range(7):
				
				daystr = str(date.today() - timedelta(days=idx))
				row = daa.loc[daystr]
				priceBtc = row['priceBtc']
				priceUsd = row['priceUsd']
				volume = row['volume']
				marketcap = row['marketcap']
				print(id, daystr, priceBtc, priceUsd, volume, marketcap)
				try:
					db1.Coll_santiment_Price.update(
						{'time': daystr, 'id': id},
						{"$set": {"priceBtc": priceBtc,
								"priceUsd": priceUsd,
								"volume": volume,
								"marketcap": marketcap,
								}
						},
						upsert = True
						)
				except Exception as e:
					print(e)
		except:
			print("Error")

