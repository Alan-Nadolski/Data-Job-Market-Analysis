import duckdb
file_name = "raw_data/JobIndex_2026-11-21.parquet"
meta_data = duckdb.sql(f'SUMMARIZE SELECT * FROM "raw_data/JobIndex_2026-11-21.parquet"').show(max_rows=25)
row_count = duckdb.sql(f'SELECT count(*) FROM "{file_name}"')
print(row_count)
first_rows = duckdb.sql(f'SELECT * FROM "{file_name}" LIMIT 10;')
print(first_rows)

