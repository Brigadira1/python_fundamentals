import sys

empty_string_size = sys.getsizeof("")
print(f"The size of an empty string in bytes is: {empty_string_size} ")

one_ascii_symbol_size = sys.getsizeof("!")
print(f"The size in bytes of one ASCII character is: {one_ascii_symbol_size}")

one_cyrillic_symbol_size = sys.getsizeof("д")
print(f"The size of one cyrillic symbol in bytes is: {one_cyrillic_symbol_size}")

two_mixed = sys.getsizeof("sф")
print(f"The size of one ASCII and one cyrillic symbols in bytes is: {two_mixed}")

two_cyrillic_symbol_size = sys.getsizeof("дс")
print(f"The size of two cyrillic symbols in bytes is: {two_cyrillic_symbol_size}")

five_ascii_symbol_size = sys.getsizeof("!!!!!")
print(f"The size of five ASCII symbols in bytes is: {five_ascii_symbol_size}")


five_five_mixed = sys.getsizeof("!!!!!ддддд")
print(f"Five ASCII + five cyrillic symbols in bytes is: {five_five_mixed}")

chinese_character = sys.getsizeof('\u9109')
print(f"One chinese character in bytes is: {chinese_character}")

icon_character = '🐍'
size = sys.getsizeof(icon_character)
print(f"The size of the {icon_character} in bytes is: {size}")

icon_ascii_mixed = '🐍!'
print(f"Icon character + one ASCII character size in bytes is: {sys.getsizeof(icon_ascii_mixed)}")

# ord() function takes a letter/symbol as a string and returns its Unicode code in integer
c = ord('\u9109')

# chr() function takes an integer value and displays the character based on its location in the Unicode table
symbol = chr(37129)

print(c)
print(symbol)

a = "hello"
b = "world"

print(f"Ids of a[4] and b[1] are: {id(a[4])} and {id(b[1])}") # shows that only one string 'o' exists in memory


