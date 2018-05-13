from database import HistoryRegion, Transactions, Share, create_debug_engine, create_session





de = create_debug_engine(True)
session = create_session(de)

b = []
a = ()
for row in session.query(HistoryRegion.id_buyer):
	b.append(row)	
	

print(b)