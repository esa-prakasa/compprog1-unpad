'''
# Deklarasi sebuah variabel Dictionary
empty = { } # Dictionary kosong
print(empty)
# Dictionary dengan satu key/value 
person = { "name": "John Smith" }
print(person)

# Dictionary dengan dua key/value
customer = {
    "name": "Alice",
    "age": 26
    } 
print(customer)
print(customer["name"])

#===================================#
#===================================#


# Menyimpan sebuah List dalam 
# sebuah Dictionary
data = { "sports": [ "baseball", "football", "hockey", "soccer" ] }

# Akses key terlebih dahulu, selanjutnya
# indeks pada key tersebut
print( data["sports"][0]) 
print( data["sports"][1:3]) 


#===================================#
#===================================#

#Menyimpan Dictionary dalam List
data = [ "John", "Jane", { "name": "Dennis" } ]

#Menampilkan item ke-0 dalam List
print( data[0] ) 

print( data[1] ) 

#Menampilkan item ke-2 dalam List. Item berupa Dictionary
print( data[2] ) 

#Menampilkan Dictionary dengan Key "name"
print( data[2]["name"] ) 
'''
#===================================#
#===================================#

# Menyimpan sebuah variabel Dictionary dalam sebuah variabel
# Dictionary yang lain
data = {
    "location": "Pantai Pangandaran",
    "visitors": { "2018": 200, "2017": 150 }
}
# Menampilkan output berupa data dengan key wins
print( data["visitors"] ) 

# Menampilkan output berupa data dengan key wins dan tahun
print( data["visitors"]["2018"] )
print( data["visitors"]["2017"] )


#===================================#
#===================================#


