import pytest
from inventory_management import Inventory

def test_add_stock():
    # test add_stock function
    inventory = Inventory()
    inventory.add_stock("Notebook", 15)
    inventory.add_stock("Postcard", 40)
    
    assert inventory.stock['Notebook'] == 15
    assert 'Notebook' in inventory.stock
    assert 'Postcard' in inventory.stock
    
def test_remove_stock():
    # test remove stock function along with exception
    inventory = Inventory()
    inventory.add_stock("IPad", 30)
    inventory.add_stock("IPhone", 45)
    inventory.add_stock("IPod", 3)
    inventory.remove_stock("IPod", 1)
    inventory.remove_stock("IPhone", 15)

    assert inventory.stock['IPhone'] == 30
    assert inventory.stock['IPod'] == 2
    
def test_check_availability():
    # test check_availability function
    inventory = Inventory()
    inventory.add_stock("IPad", 30)
    inventory.add_stock("IPhone", 45)
    inventory.add_stock("IPod", 3)

    assert inventory.check_availability("IPod", 2) is True
    assert inventory.check_availability("IPhone", 10) is True
    assert inventory.check_availability("Macbook", 20) is False
    
def test_remove_stock_with_insufficient_inventory():
    # rest exception situation in remove stock function
    inventory = Inventory()
    inventory.add_stock("IPad", 30)
    inventory.add_stock("IPhone", 45)
    inventory.add_stock("IPod", 3)

    with pytest.raises(ValueError) as excinfo:
        inventory.remove_stock("Macbook", 10)
    assert "Insufficient stock" in str(excinfo.value)

    with pytest.raises(ValueError) as exinfo:
        inventory.remove_stock("IPod", 10)
    assert "Insufficient stock" in str(excinfo.value)
    
def test_full_inventory_cycle():
    # test entire cycle which is add_stock -> remove_stock -> check_availibility
    inventory = Inventory()

    inventory.add_stock("Smartphone", 5)
    assert "Smartphone" in inventory.stock
    assert inventory.stock["Smartphone"] == 5

    inventory.remove_stock("Smartphone", 1)
    assert inventory.stock["Smartphone"] == 4

    assert inventory.check_availability("Smartphone", 2) is True
