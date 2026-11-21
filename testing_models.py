import duckdb

con = duckdb.connect("job_market_analysis/dev.duckdb")
count = con.sql('SUMMARIZE SELECT * FROM jobnet_ads')
print(count)