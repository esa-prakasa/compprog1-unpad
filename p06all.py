# Deklarasi sebuah variabel Dictionary
empty = { } # Dictionary kosong
# Dictionary dengan satu key/value 
person = { "name": "John Smith" }
print(person)
# Dictionary dengan dua key/value
customer = {
    "name": "Alice",
    "age": 26
    } 
print(customer)

#===================================#
#===================================#

# Menyimpan sebuah List dalam 
# sebuah Dictionary
data = { "sports": [ "baseball", "football", "hockey", "soccer" ] }

# Akses key terlebih dahulu, selanjutnya
# indeks pada key tersebut
print( data["sports"][0]) 

#===================================#
#===================================#

#Menyimpan Dictionary dalam List
data = [ "John", "Jane", { "name": "Dennis" } ]

#Menampilkan item ke-0 dalam List
print( data[0] ) 

#Menampilkan item ke-2 dalam List. Item berupa Dictionary
print( data[2] ) 

#Menampilkan Dictionary dengan Key "name"
print( data[2]["name"] ) 

#===================================#
#===================================#

