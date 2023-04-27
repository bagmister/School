import motorhome_maintanence_aid as m_aid
import pytest
current_millage = 80000.0
date = "02/2023"
all_tires_year = "02/2023"

class test:
    def test_tire_replacment_all_tires_correct_value(self):
        m_aid.input = lambda: 1
        output = m_aid.tire_maintanenece(current_date=date, current_millage=current_millage)
        assert output != None     

    def test_tire_replacment_all_tires_bad_value(self):
        m_aid.input = lambda: 4
        output = m_aid.tire_maintanenece(current_date=date, current_millage=current_millage)
        with pytest.raises(TypeError):
            assert output == ValueError()

    def test_individual_tire_replacment(self):
        m_aid.input = lambda: 1
        output = m_aid.tire_maintanenece(current_date=date, current_millage=current_millage)
        assert output != None   

    def teardown_method(self, method):
        m_aid.input = input 
