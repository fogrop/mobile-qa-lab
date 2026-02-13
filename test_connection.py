def test_connection(driver):
    # Просто проверяем, что сессия создалась и приложение открыто
    print(f"Успех! Мы в приложении: {driver.current_package}")
    assert driver.current_package is not None