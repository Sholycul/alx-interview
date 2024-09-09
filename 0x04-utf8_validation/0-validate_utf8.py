#!/usr/bin/python3

""" UTF-8 Validation
Python script that determines is a given data set
represents a valid UTF-8 encoding.
Return True if valid, False otherwise.
Data set can contain multiple characters.
Data will be represented by a list of integers.
"""


def validUTF8(data):
    # Number of bytes remaining for a valid UTF-8 character
    continuation_bytes = 0

    # Iterate through each byte in the data list
    for byte in data:
        # We only care about the 8 least significant bits
        byte = byte & 0xFF

        # Check if we are in the middle of a multibyte sequence
        if continuation_bytes > 0:
            # Check if the current byte is a valid continuation byte
            # (starts with '10')
            if (byte >> 6) != 0b10:
                return False
            continuation_bytes -= 1
        else:
            # Determine if it's a 1-byte, 2-byte, 3-byte, or 4-byte character
            if (byte >> 7) == 0b0:
                # 1-byte character (ASCII): 0xxxxxxx
                continue
            elif (byte >> 5) == 0b110:
                # 2-byte character: 110xxxxx
                continuation_bytes = 1
            elif (byte >> 4) == 0b1110:
                # 3-byte character: 1110xxxx
                continuation_bytes = 2
            elif (byte >> 3) == 0b11110:
                # 4-byte character: 11110xxx
                continuation_bytes = 3
            else:
                # Invalid leading byte
                return False

    # All continuation bytes should be consumed at the end
    return continuation_bytes == 0
