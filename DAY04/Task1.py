#task01: count the number of errors
file = open("log.txt", "w")

file.write("System started\n")
file.write("Error: connection failed\n")
file.write("Login successful\n")
file.write("Error: timeout occurred\n")

file.close()

print("File created")
