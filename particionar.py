import pandas as pd
import pyarrow as pa

chunksize = 900000
i = 1
with pd.read_csv("MICRODADOS_ENEM_2020.csv", encoding="ISO-8859-1", sep = ';', chunksize=chunksize) as reader:
    for chunk in reader:
        chunk.to_parquet('MICRODADOS_ENEM_2020_{}.parquet'.format(i))
        i += 1