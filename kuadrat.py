bilangan1 = [2, 4, 5, 10]
bilangan2 = [1, 3, 6, 9]

def kuadrat(nums):
    for num in nums:
        hasil = num*num
        print(str(num)+'^2 = '+str(hasil))

kuadrat(bilangan1)
print('---------------')
kuadrat(bilangan2)