import random
list_data = [1,2,3]
data1 = [20,75,81,90]
data2 = [23,65,87,90,31,34,26,74]
data3 = [77,22,55,88,11,99]

print("List data: ", list_data)

#fungsi 1
undian = random.choice(list_data)
print("\nhasil undian: ", undian)

rata1 = sum(data1)/len(data1)
rata2 = sum(data2)/len(data2)
rata3 = sum(data3)/len(data3)

#fungsi 2
import math
cheil_rata1 = math.ceil(rata1)
cheil_rata2 = math.ceil(rata2)
cheil_rata3 = math.ceil(rata3)

#fungsi 3
import math
floor_rata1 = math.floor(rata1)
floor_rata2 = math.floor(rata2)
floor_rata3 = math.floor(rata3)

if undian == 1:
    print(data1)
    print("Rata-rata data: ", rata1)
    print("Pembulatan rata-rata ke atas: ", cheil_rata1)
    print("pembulatan rata-rata ke bawah: ", floor_rata1)
elif undian == 2:
    print(data2)
    print("Rata-rata data: ", rata2)
    print("Pembulatan rata-rata ke atas: ", cheil_rata2)
    print("pembulatan rata-rata ke bawah: ", floor_rata2)
else:
    print(data3)
    print("Rata-rata data: ", rata3)
    print("Pembulatan rata-rata ke atas: ", cheil_rata3)
    print("pembulatan rata-rata ke bawah: ", floor_rata3)