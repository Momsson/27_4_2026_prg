import numpy as np

data = np.load("pacienti.npy")

print("Tvar pole:", data.shape)
print("Prvních 5 řádků:\n", data[:5])
mean = np.mean(data, axis=0)
std = np.std(data, axis=0)

print("\nPrumer (systolický, diastolický, tep):", mean)
print("Směrodatné odchylky:", std)


hypertenze = data[data[:, 0] >= 140]

print("\nPočet pacientů s hypertenzí:", len(hypertenze))

if len(hypertenze) > 0:
    avg_sys = np.mean(hypertenze[:, 0])
    print("Průměrný systolický tlak (hypertenze):", avg_sys)

pulzni_tlak = data[:, 0] - data[:, 1]
data_ext = np.column_stack((data, pulzni_tlak))

print("\nData s pulzním tlakem:\n", data_ext[:5])

idx_max_tep = np.argmax(data[:, 2])
pacient_max_tep = data[idx_max_tep]

print("\nIndex pacienta s nejvyšším tepem:", idx_max_tep)
print("Záznam pacienta:", pacient_max_tep)