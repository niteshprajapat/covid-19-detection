from covid import Covid
from datetime import datetime as dt


def covidupdatesworldwide():
    worldwide_total_active_cases =Covid().get_total_active_cases()
    worldwide_total_confirmed_cases =Covid().get_total_confirmed_cases()
    worldwide_total_recovered_cases =Covid().get_total_recovered()
    worldwide_total_death =Covid().get_total_deaths()
    
    print("        WORLDWIDE COVID INFORMATION\n")
    print("TOTAL ACTIVE CASES    :" + str(worldwide_total_active_cases))
    print("TOTAL CONFIRMED CASES :" +str(worldwide_total_confirmed_cases))
    print("TOTAL RECOVERED       :" + str(worldwide_total_recovered_cases))
    print("TOTAL DEATH           :" + str(worldwide_total_death))
    
def covidupdatesspecificcountry(i_country):
    specific_country_covid_info = Covid().get_status_by_country_name(i_country)
    
    country_total_actives_cases = specific_country_covid_info['active']
    country_total_confirmed_cases = specific_country_covid_info['confirmed']
    country_total_recovered = specific_country_covid_info['recovered']
    country_total_deaths= specific_country_covid_info['deaths']
    updated_time_epoch =specific_country_covid_info['last_update']
    data_updated_at =dt.fromtimestamp(updated_time_epoch/1000)
    
    print("\n" +i_country + " COVID INFORMATION\n")
    print("TOTAL ACTIVE CASES    :"+ str(country_total_actives_cases))
    print("TOTAL CONFIRMED CASES :" + str(country_total_confirmed_cases))
    print("TOTAL RECOVERED       :" +str(country_total_recovered))
    print("TOTAL DEATH           :" +str(country_total_deaths))
    print("LAST UPDATED AT       :" +str(data_updated_at))
    
if __name__ == '__main__':
    covidupdatesworldwide()
    country =input("ENTER THE COUNTRY'S NAME : ")
    covidupdatesspecificcountry(country)
