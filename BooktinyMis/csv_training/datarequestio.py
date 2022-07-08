# https://www.dataquest.io/blog/settingwithcopywarning/
'''

   auctionid	bid  	bidtime	     bidder  	  bidderrate	openbid	price
0	8213034705	95.0	2.927373	jake7870	    0	       95.0	    117.5
1	8213034705	115.0	2.943484	davidbresler2	1	       95.0	    117.5
2	8213034705	100.0	2.951285	gladimacowgirl	58	       95.0	    117.5
3	8213034705	117.5	2.998947	daysrus	        10	       95.0	    117.5
4	8213060420	2.0	   0.065266	    donnie4814	     5	         1.0	120.0

As you can see, each row of our data set concerns a single bid on a specific eBay Xbox auction. Here is a brief description of each column:

auctionid — A unique identifier of each auction.
bid — The value of the bid.
bidtime — The age of the auction, in days, at the time of the bid.
bidder — eBay username of the bidder.
bidderrate – The bidder’s eBay user rating.
openbid — The opening bid set by the seller for the auction.
price — The winning bid at the close of the auction.
'''


import pandas as pd
data = pd.read_csv('I:\\data_science\\csvTraining\\xbox-3-day-auctions.csv')
data.head()
print(data)
print(data.bidder)
print('==',data[data.bidder == 'parakeet2004'])

print('gladimacowgirl')
print('==',data[data.bidder == 'gladimacowgirl'])

print("下面输出：data[data.bidder == 'parakeet2004']['bidderrate'] = 100")
data[data.bidder == 'parakeet2004']['bidderrate'] = 100


# Setting the new value
#data.loc[data.bidder == 'parakeet2004', 'bidderrate'] = 100
# Taking a look at the result
#print(data[data.bidder == 'parakeet2004']['bidderrate'])

'''
Common issue #2: Hidden chaining
Moving on to the second most common way people encounter SettingWithCopyWarning.
Let’s investigate winning bids. We will create a new dataframe to work with them, 
taking care to use loc going forward now that we have learned our lesson about 
chained assignment.

常见问题二：隐藏的连锁反应
接下来是人们遇到SettingWithCopyWarning的第二个最常见的方式。让我们调查一下中标情况。
我们将创建一个新的数据框架来处理它们，注意在今后使用loc，因为我们已经吸取了关于链式赋值的教训。
'''

data.loc[data.bidder == 'parakeet2004', ('bidderrate', 'bid')]['bid'] = 5.0
data.loc[data.bidder == 'parakeet2004', ('bidderrate', 'bid')]



# Finding the winners
winner_mask = data.bid == data.price
# Taking a peek
data.loc[winner_mask].head()
# Doing analysis
mean_win_time = data.loc[winner_mask, 'bidtime'].mean()
... # 20 lines of code
mode_open_bid = data.loc[winner_mask, 'openbid'].mode()
# Updating the username
data.loc[304, 'bidder'] = 'therealname'
print(data)


winners = data.loc[data.bid == data.price]
print('winners.head():',winners.head())

mean_win_time = winners.bidtime.mean()
... # 20 lines of code
mode_open_bid = winners.openbid.mode()
print(mode_open_bid,mean_win_time)

#winners.loc[304, 'bidder']
#winners.loc[304, 'bidder'] = 'therealname'
#print(winners.loc[304, 'bidder'])
'''

winners = data.loc[data.bid == data.price].copy()
winners.loc[304, 'bidder'] = 'therealname'
print(winners.loc[304, 'bidder'])
print(data.loc[304, 'bidder'])
'''