from Pages.HomePage import HomePage

def check_availability_single_room(driver):
    home = HomePage(driver)
    home.open() \
        .open_check_in_calendar() \
        .next_month() \
        .pick_day(11) \
        .open_check_out_calendar() \
        .next_month() \
        .pick_day(15)
    return home






# def check_availability_double_room(driver):
#     home = HomePage(driver)
#     home.open() \
#         .open_check_in_calendar() \
#         .next_month() \
#         .pick_day(11) \
#         .open_check_out_calendar() \
#         .next_month() \
#         .pick_day(15)
#
# def check_availability_suite_room(driver):
#     home = HomePage(driver)
#     home.open() \
#         .open_check_in_calendar() \
#         .next_month() \
#         .pick_day(11) \
#         .open_check_out_calendar() \
#         .next_month() \
#         .pick_day(15)

#     1. User wybiera check in date ( random )
#     2. User wybiera check out date (random )
#     3. user wybiera single room
#     4. sprawdza cenne
#     5. Sprawdza udogodnienia tv , wifi, safe
#     6.



#     1. User wybiera check in date ( random )
#     2. User wybiera check out date (random )
#     3. user wybiera double room
#     4. sprawdza cenne
#     5. Sprawdza udogodnienia tv , radio, safe



#     1. User wybiera check in date ( random )
#     2. User wybiera check out date (random )
#     3. user wybiera suite room room
#     4. sprawdza cenne
#     5. Sprawdza udogodnienia radio, wifi, safe
