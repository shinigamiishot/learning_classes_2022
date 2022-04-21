from data.city import City

def test_city():
    c = City(zip_code=1230, city_name="Liesing")
    assert c.zip_code == 1230
    assert c.city_name == "Liesing"
