from services.validator.helper import is_phone


class TestValidators:
    def test_regular_phone_number_validation(self):
        # Given: phone number
        phone_number = "01012341234"

        # When: Try to validate phone number
        # Then: validation match
        assert is_phone(phone_number) is not None

    def test_phone_base_station_number_validation(self):
        # Given: old phone numbers
        last_phone_number = "1231234"
        base_station_011 = "011" + last_phone_number
        base_station_016 = "016" + last_phone_number
        base_station_017 = "017" + last_phone_number
        base_station_018 = "018" + last_phone_number
        base_station_019 = "019" + last_phone_number

        # When: Try to validate phone number
        # Then: validation match
        assert is_phone(base_station_011) is not None
        assert is_phone(base_station_016) is not None
        assert is_phone(base_station_017) is not None
        assert is_phone(base_station_018) is not None
        assert is_phone(base_station_019) is not None

    def test_not_proper_phone_number_validation(self):
        # Given: not proper phone number
        not_phone1 = "010123451234"
        not_phone2 = "01012341234567"

        # When: Try to validate phone number
        # Then: validation does not match
        assert is_phone(not_phone1) is None
        assert is_phone(not_phone2) is None

    def test_not_phone_base_station_number_validation(self):
        # Given: not phone base station numbers
        last_phone_number = "1231234"
        not_base_station_012 = "012" + last_phone_number
        not_base_station_013 = "013" + last_phone_number
        not_base_station_014 = "014" + last_phone_number
        not_base_station_015 = "015" + last_phone_number

        # When: Try to validate phone number
        # Then: validation does not match
        assert is_phone(not_base_station_012) is None
        assert is_phone(not_base_station_013) is None
        assert is_phone(not_base_station_014) is None
        assert is_phone(not_base_station_015) is None
