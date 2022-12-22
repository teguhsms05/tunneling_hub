from selenium import webdriver
from .models import *
import csv, time, os

class AccessDomain(object):
    
    def __init__(self, domain, group_domain):
        self.domain = domain
        self.group_domain = group_domain
        
    # ubs-indonesia.net
    def cpanel_ubs(self, domainGroup,domainCpanel, domainCredential):
        print ('domainGroup ', domainGroup)
        print ('domainCpanel ', domainCpanel)
        print ('domainCredential ', domainCredential)

        web = webdriver.Chrome('/Users/teguhsms/Downloads/chromedriver')
        web.get(domainGroup['cpanelUsed'])
        print (domainCredential['user'], domainCredential['pass'])
        time.sleep(5)
        username_input = web.find_element_by_name("user")
        password_input = web.find_element_by_name("pass")
        username_input.send_keys(domainCredential['user'])
        password_input.send_keys(domainCredential['pass'])

        login_button = web.find_element_by_xpath("//*[@id='login_submit']")
        login_button.click()
        time.sleep(5)

        zone = web.find_element_by_id('item_zone_editor')
        zone.click()
        time.sleep(5)

        # manage_for_ubs = web.find_element_by_id('manage_for_'+domainCpanel)
        # print ('action manage')
        # manage_for_ubs.click()
        # time.sleep(5)

        # add_record_btn = web.find_element_by_xpath('//*[@id="search_add_record_btn"]')
        # add_record_btn.click()
        # print ('action record')
        # time.sleep(5)

        # web.find_element_by_name("recordTTL_0").clear()
        # time.sleep(2)
        
        # zone_name = web.find_element_by_name("recordName_0")
        # address = web.find_element_by_name("record_a_address_0")
        # ttl = web.find_element_by_name("recordTTL_0")
        # zone_name.send_keys(self.domain)
        # address.send_keys('103.253.107.63')
        # ttl.send_keys('14400')

        # save_record = web.find_element_by_id('inline_add_record_button_0')
        # save_record.click()
        # time.sleep(5)
        
        # logout sessions
        action_to_account = web.find_element_by_xpath('//*[@id="userPrefMenu"]')
        action_to_account.click()
        time.sleep(3)
        action_to_logout = web.find_element_by_xpath('//*[@id="lnkHeaderLogout"]')
        action_to_logout.click()
        time.sleep(5)
        
        web.close()
    
    # monitoringsystems.co.id
    def cpanel_monsys(self, domainGroup,domainCpanel, domainCredential):
        print ('domainGroup ', domainGroup)
        print ('domainCpanel ', domainCpanel)
        print ('domainCredential ', domainCredential)

        web = webdriver.Chrome('/Users/teguhsms/Downloads/chromedriver')
        web.get(domainGroup['cpanelUsed'])
        print (domainCredential['user'], domainCredential['pass'])
        time.sleep(5)
        username_input = web.find_element_by_name("username")
        password_input = web.find_element_by_name("password")
        username_input.send_keys(domainCredential['user'])
        password_input.send_keys(domainCredential['pass'])

        login_button = web.find_element_by_xpath('//*[@id="login"]/form/fieldset/p[3]/input')
        login_button.click()
        time.sleep(5)
        
        zone = web.find_element_by_xpath('/html/body/div[1]/section/nav/ul/li[2]/a')
        zone.click()
        time.sleep(5)

        manage_for_monsys = web.find_element_by_xpath('/html/body/div[1]/form/table/tbody/tr[2]/td[2]/a[1]')
        manage_for_monsys.click()
        time.sleep(5)

        # add_record_btn = web.find_element_by_xpath('//*[@id="search_add_record_btn"]')
        # add_record_btn.click()
        # print ('action record')
        # time.sleep(5)

        # web.find_element_by_name("recordTTL_0").clear()
        # time.sleep(2)
    
        zone_name = web.find_element_by_name("name")
        address = web.find_element_by_name("content")
        priority = web.find_element_by_name("prio")
        ttl = web.find_element_by_name("ttl")
        zone_name.send_keys((self.domain).replace('.'+domainGroup['domainUsed'],''))
        address.send_keys('103.253.107.63')
        priority.send_keys(0)
        ttl.send_keys('14400')
        time.sleep(5)

        save_record = web.find_element_by_xpath('/html/body/div[1]/form[2]/input[2]')
        save_record.click()
        time.sleep(8)
        
        zone = web.find_element_by_xpath('/html/body/div[1]/section/nav/ul/li[2]/a')
        zone.click()
        time.sleep(5)
        
        # logout sessions
        action_to_logout = web.find_element_by_link_text('Logout')
        action_to_logout.click()
        time.sleep(7)
        
        web.close()
        
    def get_credential(self):
        with open('./domregis/confURL.csv') as regDomain:
            usr, pwd = '',''
            reader = csv.DictReader(regDomain)
            for row in reader:
                if self.group_domain in row['group_domain']:
                    usr = row.get('user')
                    pwd = row.get('pass')
                else:
                    usr = row.get('user')
                    pwd = row.get('pass')
            credential = {'user': usr, 'pass': pwd}
            return credential
        
    def domain_used(self):
        #query_domain_group = f"SELECT cpanel_domain FROM DOMAIN.DOMAIN_GROUP WHERE group_domain =  '{self.group_domain}' "
        #domainUsed = db.execute(query_domain_group).fetchone().values()
        domainUsed = GroupDomain.objects.get(group_domain=self.group_domain)
        domainGroup = {'domainUsed':domainUsed.group_domain, 'cpanelUsed': domainUsed.cpanel_domain}
        return domainGroup

    def register(self):
        domainGroup = self.domain_used()
        domainCpanel = (domainGroup['domainUsed']).replace('.','_')
        domainCredential = self.get_credential()

        # web = webdriver.Chrome('/Users/teguhsms/Downloads/chromedriver')
        # web.get(domainGroup['cpanelUsed'])
        print (domainCredential['user'], domainCredential['pass'])
        # time.sleep(5)
        
        if (domainCredential['user']=='ubsindon'):
            cpanelUbs = self.cpanel_ubs(domainGroup,domainCpanel, domainCredential)
        if (domainCredential['user']=='monitori'):
            cpanelMonsys = self.cpanel_monsys(domainGroup,domainCpanel, domainCredential)
        # username_input = web.find_element_by_name("user")
        # password_input = web.find_element_by_name("pass")
        # username_input.send_keys(domainCredential['user'])
        # password_input.send_keys(domainCredential['pass'])

        # login_button = web.find_element_by_xpath("//*[@id='login_submit']")
        # login_button.click()
        # time.sleep(5)

        # zone = web.find_element_by_id('item_zone_editor')
        # zone.click()
        # time.sleep(5)

        # manage_for_ubs = web.find_element_by_id('manage_for_'+domainCpanel)
        # print ('action manage')
        # manage_for_ubs.click()
        # time.sleep(5)

        # add_record_btn = web.find_element_by_xpath('//*[@id="search_add_record_btn"]')
        # add_record_btn.click()
        # print ('action record')
        # time.sleep(5)

        # web.find_element_by_name("recordTTL_0").clear()
        # time.sleep(2)
        
        # zone_name = web.find_element_by_name("recordName_0")
        # address = web.find_element_by_name("record_a_address_0")
        # ttl = web.find_element_by_name("recordTTL_0")
        # zone_name.send_keys(self.domain)
        # address.send_keys('103.253.107.63')
        # ttl.send_keys('14400')

        # save_record = web.find_element_by_id('inline_add_record_button_0')
        # save_record.click()
        # time.sleep(5)
        
        #logout sessions
        
        # action_to_account = web.find_element_by_xpath('//*[@id="userPrefMenu"]')
        # action_to_account.click()
        # time.sleep(3)
        # action_to_logout = web.find_element_by_xpath('//*[@id="lnkHeaderLogout"]')
        # action_to_logout.click()
        # time.sleep(5)

        # web.close()



