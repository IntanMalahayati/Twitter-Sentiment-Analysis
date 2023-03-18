import twint
c = twint.Config()
c.Search = '"sunscreen" lang:id'    #keyword
c.Limit = 25000
c.Store_csv = True
c.Output = 'tweet_all.csv'
twint.run.Search(c)

