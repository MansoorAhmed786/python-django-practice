#io.BytesIo
import io

# Create a BytesIO object
byte_buffer = io.BytesIO()

# Write binary data to the buffer
byte_buffer.write(b'Hello, World!')

# Read binary data from the buffer
data = byte_buffer.getvalue()

print(data)  # Output: b'Hello, World!'

########################################
io.StringIO
import io

# Create a StringIO object
string_buffer = io.StringIO()

# Write text data to the buffer
string_buffer.write("Hello, World!")

# Read text data from the buffer
data = string_buffer.getvalue()

print(data)  # Output: Hello, World!
