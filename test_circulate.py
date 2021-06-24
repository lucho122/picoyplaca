from main import canCirculate # The code to test

class TestsCases: 
    # Monday | 1, 2 cannot circulate.
    def test1_GivenValidLicensePlateInvalidTime_WhenICheck_ReturnsFalse(self):
        assert canCirculate("13/12/2021", "09:00", "PCJ-9023") == False

    # Monday | 1, 2 cannot circulate.
    def test2_GivenValidLicensePlateValidTime_WhenICheck_ReturnsTrue(self):
        assert canCirculate("13/12/2021", "10:00", "PCJ-9023") == True

    # Tuesday | 3, 4 cann)ot circulate.
    def test3_GivenInvalidLicensePlateInvalidTime_WhenICheck_ReturnsFalse(self):
        assert canCirculate("14/12/2021", "09:00", "PCJ-9023") == False

    # Tuesday | 3, 4 cannot circulate.
    def test4_GivenInvalidLicensePlateValidTime_WhenICheck_ReturnsFalse(self):    
        assert canCirculate("14/12/2021", "10:00", "PCJ-9023") == False

    # Sunday | Everyone can circulate at any hour.
    def test5_GivenInvalidLicensePlateInvalidTime_WhenICheck_ReturnsTrue(self):
        assert canCirculate("12/12/2021", "09:00", "PCJ-9023") == True

    # Sunday | Everyone can circulate at any hour.
    def test6_GivenInvalidLicensePlateValidTime_WhenICheck_ReturnsTrue(self):
        assert canCirculate("12/12/2021", "10:00", "PCJ-9023") == True