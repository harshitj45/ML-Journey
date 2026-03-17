# Convert "25" string to int
a = "25"
a_int = int(a)

# Convert 3.99 float to int
b = 3.99
b_int = int(b)

# Convert 100 int to float
c = 100
c_float = float(c)

# Convert 0 to bool
d = 0
d_bool = bool(d)

# Convert "" to bool
e = ""
e_bool = bool(e)

# Print results with types
print("String to Int:", a_int, type(a_int))
print("Float to Int:", b_int, type(b_int))
print("Int to Float:", c_float, type(c_float))
print("0 to Bool:", d_bool, type(d_bool))
print('"" to Bool:', e_bool, type(e_bool))