<h1 align="center">Fletcher_checksum</h1>

Implementation of fletcher-16, fletcher-32, and fletcher-64 checksums in Python3 for working with string and bytes data.

### Description

The Fletcher checksum is an algorithm for computing a position-dependent checksum devised by John G. Fletcher (1934–2012) at Lawrence Livermore Labs in the late 1970s. The objective of the Fletcher checksum was to provide error-detection properties approaching those of a cyclic redundancy check but with the lower computational effort associated with summation techniques.

### API

This library has functions for working with string and byte data (which also allows you to calculate the checksum for your files).
 An example of usage is shown below.
 
 ```python
 
# Importing classes with static methods for working with strings and bytes
from FletcherChecksumLib import FletcherChecksumStr, FletcherChecksumBytes

# Example of using string input
test_string_input = 'Hello, world!'
checksum_result = FletcherChecksumStr.get_fletcher16(test_string_input)
print(checksum_result)

>>>   { 
>>>     'Fletcher16_dec': 29069,
>>>     'Fletcher16_hex': '0x718d' 
>>>   }

# Example of using bytes input
test_bytes_input = b'\xd0\x91\xd0\xb0\xd0\xb9\xd1\x82\xd1\x8b'
checksum_result = FletcherChecksumBytes.get_fletcher32(test_bytes_input)
print(checksum_result)

>>>   { 
>>>     'Fletcher32_dec': 670893849,
>>>     'Fletcher32_hex': '0x27fd0719'
>>>   }

# Example of using file(bytes) input
test_file_input = open('test.txt', 'rb')
test_bytes_input = test_file_input.read()
checksum_result = FletcherChecksumBytes.get_fletcher64(test_bytes_input)
print(checksum_result)

>>>   { 
>>>     'Fletcher64_dec': 35532264440969,
>>>     'Fletcher64_hex': '0x205100000489'
>>>   }

 ```
