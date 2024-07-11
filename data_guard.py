
CURRENT_LINE = '07'

def left(s,chars):
    return s[:chars]

def right(s,chars):
    return s[-chars:]

def mid(s,start,end):
    return s[start:end+1]


class Validation():

    def check(serial_number):
        is_valid = False

        # Make sure Serial Number has the correct format
        if len(serial_number)==14 and left(serial_number,6).isnumeric() and right(serial_number,6).isnumeric() and not mid(test_val, 6, 7).isnumeric() and mid(test_val, 8, 9) == CURRENT_LINE:
            is_valid = True

        return is_valid


if __name__ == '__main__':

    # Test good
    test_val = '240711BM070001'
    print(left(test_val, 6))
    print(right(test_val, 6))
    print(mid(test_val, 6, 7))
    print( Validation.check(test_val) )

    # Test fail
    test_val_2 = '240711BM070001_Backsheet_1234567890'
    print( Validation.check(test_val_2) )