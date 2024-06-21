import dask.dataframe as dd
from dask.distributed import Client
client = Client(n_workers=4)
print(client)

df = dd.read_csv('Prueba Monitoreo de Aire.csv')
df_computed = df.compute()

mean_values = df_computed.mean()
print("Mean values:")
print(mean_values)

print(client.dashboard_link)

print(df_computed)