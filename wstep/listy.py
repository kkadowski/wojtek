# ''' 
# Listy - typ sekwencyjny - mutable
# K>K> 2023-10-11
# v. 1.0
# '''

# # l1 = [ 2, 3, 6, 3, 1 ]
# # print(type(l1))
# # print(l1)

# # l2 = [ 2, 9.4, "Anna" ]
# # print(l2)

# l3 = [ [1,2,3], [ "Anna", "Szymon" ], 2, 4.5, 9, 8, 7 ]
# # print(l3)
# # print(l3[1])
# # print(l3[-1])

# #slicing
# print(l3[0:4:2])   #[start:end:step]
# print(l3[::-1])     #odwórci listę (tylko wypisując!)
# # l3 = l3[::-1]       # lista zostanie odwrócona
# # print(l3)

# print(l3[-2:-5:-1])
# print(l3[1][0])


# for ele in l3:  # wyświetlanie lementów listy
#     print(ele)
    
# #Element numer to wartość

# for i in range(len(l3)):  #wyświetlanie po indeksie elementów listy
#     print(f"Element {i} to {l3[i]}")
    
# for i in range(1,4,1):
#     print(f"Element {i} to {l3[i]}")

# # acaca
    

tekst = "abcdabc"
for i in range(len(tekst)):
    if tekst[i] in list(tekst)[i+1:]:
        print(i) 


print(list(tekst))










