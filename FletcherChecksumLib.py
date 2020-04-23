# -----------------------------------------------------
#                                                     #
#             Fletcher’s Checksum Library             #
#   Checksum in the current version of the library:   #
#                                                     #
#                 Fletcher – 16: YES                  #
#                 Fletcher – 32: YES                  #
#                 Fletcher – 64: YES                  #
#                                                     #
#        Possible input values for calculations:      #
#                                                     #
#                     STRING: YES                     #
#                     BYTES: YES                      #
#                                                     #
# -----------------------------------------------------


class FletcherChecksumStr:
    """
    This class contains static methods for working with STRING values as input parameters.
    """

    @staticmethod
    def get_fletcher16(data: str) -> dict:
        """
        Accepts a string as input.
        Returns the Fletcher16 checksum value in decimal and hexadecimal format.
        8-bit implementation (16-bit checksum)
        """
        sum1, sum2 = int(), int()
        data = data.encode()
        for index in range(len(data)):
            sum1 = (sum1 + data[index]) % 255
            sum2 = (sum2 + sum1) % 255
        result = (sum2 << 8) | sum1
        return {"Fletcher16_dec": result, "Fletcher16_hex": hex(result)}

    @staticmethod
    def get_fletcher32(data: str) -> dict:
        """
        Accepts a string as input.
        Returns the Fletcher32 checksum value in decimal and hexadecimal format.
        16-bit implementation (32-bit checksum)
        """
        sum1, sum2 = int(), int()
        data = data.encode()
        for index in range(len(data)):
            sum1 = (sum1 + data[index]) % 65535
            sum2 = (sum2 + sum1) % 65535
        result = (sum2 << 16) | sum1
        return {"Fletcher32_dec": result, "Fletcher32_hex": hex(result)}

    @staticmethod
    def get_fletcher64(data: str) -> dict:
        """
        Accepts a string as input.
        Returns the Fletcher64 checksum value in decimal and hexadecimal format.
        32-bit implementation (64-bit checksum)
        """
        sum1, sum2 = int(), int()
        data = data.encode()
        for index in range(len(data)):
            sum1 = (sum1 + data[index]) % 4294967295
            sum2 = (sum2 + sum1) % 4294967295
        result = (sum2 << 32) | sum1
        return {"Fletcher64_dec": result, "Fletcher64_hex": hex(result)}


class FletcherChecksumBytes:
    """
    This class contains static methods for working with BYTES values as input parameters.
    """

    @staticmethod
    def get_fletcher16(data: bytes) -> dict:
        """
        Accepts bytes as input.
        Returns the Fletcher16 checksum value in decimal and hexadecimal format.
        8-bit implementation (16-bit checksum)
        """
        sum1, sum2 = int(), int()
        for index in range(len(data)):
            sum1 = (sum1 + data[index]) % 255
            sum2 = (sum2 + sum1) % 255
        result = (sum2 << 8) | sum1
        return {"Fletcher16_dec": result, "Fletcher16_hex": hex(result)}

    @staticmethod
    def get_fletcher32(data: bytes) -> dict:
        """
        Accepts bytes as input.
        Returns the Fletcher32 checksum value in decimal and hexadecimal format.
        16-bit implementation (32-bit checksum)
        """
        sum1, sum2 = int(), int()
        for index in range(len(data)):
            sum1 = (sum1 + data[index]) % 65535
            sum2 = (sum2 + sum1) % 65535
        result = (sum2 << 16) | sum1
        return {"Fletcher32_dec": result, "Fletcher32_hex": hex(result)}

    @staticmethod
    def get_fletcher64(data: bytes) -> dict:
        """
        Accepts bytes as input.
        Returns the Fletcher64 checksum value in decimal and hexadecimal format.
        32-bit implementation (64-bit checksum)
        """
        sum1, sum2 = int(), int()
        for index in range(len(data)):
            sum1 = (sum1 + data[index]) % 4294967295
            sum2 = (sum2 + sum1) % 4294967295
        result = (sum2 << 32) | sum1
        return {"Fletcher64_dec": result, "Fletcher64_hex": hex(result)}

