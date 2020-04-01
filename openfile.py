opening/creating and writing to a text file
2| f = open("covid30Mar.txt", "w+") # open file in writing and reading mode
3| f.write("this is a test")
4| f.close( )
5| # reading from a text file
6| f = open("test.txt", "r")
7| data = f.read( )
8| f.close( )
9| print(data