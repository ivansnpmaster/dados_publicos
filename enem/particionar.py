import pandas as pd

chunksize = 400000
i = 0
with pd.read_csv("MICRODADOS_ENEM_2020.csv", encoding = "ISO-8859-1", sep = ';', chunksize = chunksize) as reader:
    for chunk in reader:
        i += 1
        chunk.to_parquet('2020/MICRODADOS_ENEM_2020_{}.parquet'.format("0" + str(i) if len(str(i)) == 1 else i))