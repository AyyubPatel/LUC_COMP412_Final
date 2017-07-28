import datetime
from Stephanie.Modules.base_module import BaseModule
import base64, datetime, hashlib, hmac, urllib.request, json


class CurrentTimeModule(BaseModule):
    def __init__(self, *args):
        super(CurrentTimeModule, self).__init__(*args)


    def ask_current_time(self):
        self.assistant.say("Sure, What city would you like to know about?")
        user_city = self.assistant.listen().decipher()
        self.assistant.say("What country is it?")
        user_country = self.assistant.listen().decipher()
        if user_country =='Afghanistan':
            code = 'AF'
        elif user_country =='Aland Islands':
            code = 'AX'
        elif user_country =='Albania':
            code = 'AL'
        elif user_country =='Algeria':
            code = 'DZ'
        elif user_country =='American Samoa':
            code = 'AS'
        elif user_country =='Andorra':
            code = 'AD'
        elif user_country =='Angola':
            code = 'AO'
        elif user_country =='Anguilla':
            code = 'AI'
        elif user_country =='Antarctica':
            code = 'AQ'
        elif user_country =='Antigua and Barbuda':
            code = 'AG'
        elif user_country =='Argentina':
            code = 'AR'
        elif user_country =='Armenia':
            code = 'AM'
        elif user_country =='Aruba':
            code = 'AW'
        elif user_country =='Australia':
            code = 'AU'
        elif user_country =='Austria':
            code = 'AT'
        elif user_country =='Azerbaijan':
            code = 'AZ'
        elif user_country =='Bahamas':
            code = 'BS'
        elif user_country =='Bahrain':
            code = 'BH'
        elif user_country =='Bangladesh':
            code = 'BD'
        elif user_country =='Barbados':
            code = 'BB'
        elif user_country =='Belarus':
            code = 'BY'
        elif user_country =='Belgium':
            code = 'BE'
        elif user_country =='Belize':
            code = 'BZ'
        elif user_country =='Benin':
            code = 'BJ'
        elif user_country =='Bermuda':
            code = 'BM'
        elif user_country =='Bhutan':
            code = 'BT'
        elif user_country =='Bolivia':
            code = 'BO'
        elif user_country =='Bonaire, Saint Eustatius and Saba':
            code = 'BQ'
        elif user_country =='Bosnia and Herzegovina':
            code = 'BA'
        elif user_country =='Botswana':
            code = 'BW'
        elif user_country =='Bouvet Island':
            code = 'BV'
        elif user_country =='Brazil':
            code = 'BR'
        elif user_country =='British Indian Ocean Territory':
            code = 'IO'
        elif user_country =='British Virgin Islands':
            code = 'VG'
        elif user_country =='Brunei':
            code = 'BN'
        elif user_country =='Bulgaria':
            code = 'BG'
        elif user_country =='Burkina Faso':
            code = 'BF'
        elif user_country =='Burundi':
            code = 'BI'
        elif user_country =='Cambodia':
            code = 'KH'
        elif user_country =='Cameroon':
            code = 'CM'
        elif user_country =='Canada':
            code = 'CA'
        elif user_country =='Cape Verde':
            code = 'CV'
        elif user_country =='Cayman Islands':
            code = 'KY'
        elif user_country =='Central African Republic':
            code = 'CF'
        elif user_country =='Chad':
            code = 'TD'
        elif user_country =='Chile':
            code = 'CL'
        elif user_country =='China':
            code = 'CN'
        elif user_country =='Christmas Island':
            code = 'CX'
        elif user_country =='Cocos Islands':
            code = 'CC'
        elif user_country =='Colombia':
            code = 'CO'
        elif user_country =='Comoros':
            code = 'KM'
        elif user_country =='Cook Islands':
            code = 'CK'
        elif user_country =='Costa Rica':
            code = 'CR'
        elif user_country =='Croatia':
            code = 'HR'
        elif user_country =='Cuba':
            code = 'CU'
        elif user_country =='Curaçao':
            code = 'CW'
        elif user_country =='Cyprus':
            code = 'CY'
        elif user_country =='Czech Republic':
            code = 'CZ'
        elif user_country =='Democratic Republic of the Congo':
            code = 'CD'
        elif user_country =='Denmark':
            code = 'DK'
        elif user_country =='Djibouti':
            code = 'DJ'
        elif user_country =='Dominica':
            code = 'DM'
        elif user_country =='Dominican Republic':
            code = 'DO'
        elif user_country =='East Timor':
            code = 'TL'
        elif user_country =='Ecuador':
            code = 'EC'
        elif user_country =='Egypt':
            code = 'EG'
        elif user_country =='El Salvador':
            code = 'SV'
        elif user_country =='Equatorial Guinea':
            code = 'GQ'
        elif user_country =='Eritrea':
            code = 'ER'
        elif user_country =='Estonia':
            code = 'EE'
        elif user_country =='Ethiopia':
            code = 'ET'
        elif user_country =='Falkland Islands':
            code = 'FK'
        elif user_country =='Faroe Islands':
            code = 'FO'
        elif user_country =='Fiji':
            code = 'FJ'
        elif user_country =='Finland':
            code = 'FI'
        elif user_country =='France':
            code = 'FR'
        elif user_country =='French Guiana':
            code = 'GF'
        elif user_country =='French Polynesia':
            code = 'PF'
        elif user_country =='French Southern Territories':
            code = 'TF'
        elif user_country =='Gabon':
            code = 'GA'
        elif user_country =='Gambia':
            code = 'GM'
        elif user_country =='Georgia':
            code = 'GE'
        elif user_country =='Germany':
            code = 'DE'
        elif user_country =='Ghana':
            code = 'GH'
        elif user_country =='Gibraltar':
            code = 'GI'
        elif user_country =='Greece':
            code = 'GR'
        elif user_country =='Greenland':
            code = 'GL'
        elif user_country =='Grenada':
            code = 'GD'
        elif user_country =='Guadeloupe':
            code = 'GP'
        elif user_country =='Guam':
            code = 'GU'
        elif user_country =='Guatemala':
            code = 'GT'
        elif user_country =='Guernsey':
            code = 'GG'
        elif user_country =='Guinea':
            code = 'GN'
        elif user_country =='Guinea-Bissau':
            code = 'GW'
        elif user_country =='Guyana':
            code = 'GY'
        elif user_country =='Haiti':
            code = 'HT'
        elif user_country =='Heard Island and McDonald Islands':
            code = 'HM'
        elif user_country =='Honduras':
            code = 'HN'
        elif user_country =='Hong Kong':
            code = 'HK'
        elif user_country =='Hungary':
            code = 'HU'
        elif user_country =='Iceland':
            code = 'IS'
        elif user_country =='India':
            code = 'IN'
        elif user_country =='Indonesia':
            code = 'ID'
        elif user_country =='Iran':
            code = 'IR'
        elif user_country =='Iraq':
            code = 'IQ'
        elif user_country =='Ireland':
            code = 'IE'
        elif user_country =='Isle of Man':
            code = 'IM'
        elif user_country =='Israel':
            code = 'IL'
        elif user_country =='Italy':
            code = 'IT'
        elif user_country =='Ivory Coast':
            code = 'CI'
        elif user_country =='Jamaica':
            code = 'JM'
        elif user_country =='Japan':
            code = 'JP'
        elif user_country =='Jersey':
            code = 'JE'
        elif user_country =='Jordan':
            code = 'JO'
        elif user_country =='Kazakhstan':
            code = 'KZ'
        elif user_country =='Kenya':
            code = 'KE'
        elif user_country =='Kiribati':
            code = 'KI'
        elif user_country =='Kosovo':
            code = 'XK'
        elif user_country =='Kuwait':
            code = 'KW'
        elif user_country =='Kyrgyzstan':
            code = 'KG'
        elif user_country =='Laos':
            code = 'LA'
        elif user_country =='Latvia':
            code = 'LV'
        elif user_country =='Lebanon':
            code = 'LB'
        elif user_country =='Lesotho':
            code = 'LS'
        elif user_country =='Liberia':
            code = 'LR'
        elif user_country =='Libya':
            code = 'LY'
        elif user_country =='Liechtenstein':
            code = 'LI'
        elif user_country =='Lithuania':
            code = 'LT'
        elif user_country =='Luxembourg':
            code = 'LU'
        elif user_country =='Macao':
            code = 'MO'
        elif user_country =='Macedonia':
            code = 'MK'
        elif user_country =='Madagascar':
            code = 'MG'
        elif user_country =='Malawi':
            code = 'MW'
        elif user_country =='Malaysia':
            code = 'MY'
        elif user_country =='Maldives':
            code = 'MV'
        elif user_country =='Mali':
            code = 'ML'
        elif user_country =='Malta':
            code = 'MT'
        elif user_country =='Marshall Islands':
            code = 'MH'
        elif user_country =='Martinique':
            code = 'MQ'
        elif user_country =='Mauritania':
            code = 'MR'
        elif user_country =='Mauritius':
            code = 'MU'
        elif user_country =='Mayotte':
            code = 'YT'
        elif user_country =='Mexico':
            code = 'MX'
        elif user_country =='Micronesia':
            code = 'FM'
        elif user_country =='Moldova':
            code = 'MD'
        elif user_country =='Monaco':
            code = 'MC'
        elif user_country =='Mongolia':
            code = 'MN'
        elif user_country =='Montenegro':
            code = 'ME'
        elif user_country =='Montserrat':
            code = 'MS'
        elif user_country =='Morocco':
            code = 'MA'
        elif user_country =='Mozambique':
            code = 'MZ'
        elif user_country =='Myanmar':
            code = 'MM'
        elif user_country =='Namibia':
            code = 'NA'
        elif user_country =='Nauru':
            code = 'NR'
        elif user_country =='Nepal':
            code = 'NP'
        elif user_country =='Netherlands':
            code = 'NL'
        elif user_country =='Netherlands Antilles':
            code = 'AN'
        elif user_country =='New Caledonia':
            code = 'NC'
        elif user_country =='New Zealand':
            code = 'NZ'
        elif user_country =='Nicaragua':
            code = 'NI'
        elif user_country =='Niger':
            code = 'NE'
        elif user_country =='Nigeria':
            code = 'NG'
        elif user_country =='Niue':
            code = 'NU'
        elif user_country =='Norfolk Island':
            code = 'NF'
        elif user_country =='North Korea':
            code = 'KP'
        elif user_country =='Northern Mariana Islands':
            code = 'MP'
        elif user_country =='Norway':
            code = 'NO'
        elif user_country =='Oman':
            code = 'OM'
        elif user_country =='Pakistan':
            code = 'PK'
        elif user_country =='Palau':
            code = 'PW'
        elif user_country =='Palestinian Territory':
            code = 'PS'
        elif user_country =='Panama':
            code = 'PA'
        elif user_country =='Papua New Guinea':
            code = 'PG'
        elif user_country =='Paraguay':
            code = 'PY'
        elif user_country =='Peru':
            code = 'PE'
        elif user_country =='Philippines':
            code = 'PH'
        elif user_country =='Pitcairn':
            code = 'PN'
        elif user_country =='Poland':
            code = 'PL'
        elif user_country =='Portugal':
            code = 'PT'
        elif user_country =='Puerto Rico':
            code = 'PR'
        elif user_country =='Qatar':
            code = 'QA'
        elif user_country =='Republic of the Congo':
            code = 'CG'
        elif user_country =='Reunion':
            code = 'RE'
        elif user_country =='Romania':
            code = 'RO'
        elif user_country =='Russia':
            code = 'RU'
        elif user_country =='Rwanda':
            code = 'RW'
        elif user_country =='Saint Barthelemy':
            code = 'BL'
        elif user_country =='Saint Helena':
            code = 'SH'
        elif user_country =='Saint Kitts and Nevis':
            code = 'KN'
        elif user_country =='Saint Lucia':
            code = 'LC'
        elif user_country =='Saint Martin':
            code = 'MF'
        elif user_country =='Saint Pierre and Miquelon':
            code = 'PM'
        elif user_country =='Saint Vincent and the Grenadines':
            code = 'VC'
        elif user_country =='Samoa':
            code = 'WS'
        elif user_country =='San Marino':
            code = 'SM'
        elif user_country =='Sao Tome and Principe':
            code = 'ST'
        elif user_country =='Saudi Arabia':
            code = 'SA'
        elif user_country =='Senegal':
            code = 'SN'
        elif user_country =='Serbia':
            code = 'RS'
        elif user_country =='Serbia and Montenegro':
            code = 'CS'
        elif user_country =='Seychelles':
            code = 'SC'
        elif user_country =='Sierra Leone':
            code = 'SL'
        elif user_country =='Singapore':
            code = 'SG'
        elif user_country =='Sint Maarten':
            code = 'SX'
        elif user_country =='Slovakia':
            code = 'SK'
        elif user_country =='Slovenia':
            code = 'SI'
        elif user_country =='Solomon Islands':
            code = 'SB'
        elif user_country =='Somalia':
            code = 'SO'
        elif user_country =='South Africa':
            code = 'ZA'
        elif user_country =='South Georgia and the South Sandwich Islands':
            code = 'GS'
        elif user_country =='South Korea':
            code = 'KR'
        elif user_country =='South Sudan':
            code = 'SS'
        elif user_country =='Spain':
            code = 'ES'
        elif user_country =='Sri Lanka':
            code = 'LK'
        elif user_country =='Sudan':
            code = 'SD'
        elif user_country =='Suriname':
            code = 'SR'
        elif user_country =='Svalbard and Jan Mayen':
            code = 'SJ'
        elif user_country =='Swaziland':
            code = 'SZ'
        elif user_country =='Sweden':
            code = 'SE'
        elif user_country =='Switzerland':
            code = 'CH'
        elif user_country =='Syria':
            code = 'SY'
        elif user_country =='Taiwan':
            code = 'TW'
        elif user_country =='Tajikistan':
            code = 'TJ'
        elif user_country =='Tanzania':
            code = 'TZ'
        elif user_country =='Thailand':
            code = 'TH'
        elif user_country =='Togo':
            code = 'TG'
        elif user_country =='Tokelau':
            code = 'TK'
        elif user_country =='Tonga':
            code = 'TO'
        elif user_country =='Trinidad and Tobago':
            code = 'TT'
        elif user_country =='Tunisia':
            code = 'TN'
        elif user_country =='Turkey':
            code = 'TR'
        elif user_country =='Turkmenistan':
            code = 'TM'
        elif user_country =='Turks and Caicos Islands':
            code = 'TC'
        elif user_country =='Tuvalu':
            code = 'TV'
        elif user_country =='U.S. Virgin Islands':
            code = 'VI'
        elif user_country =='Uganda':
            code = 'UG'
        elif user_country =='Ukraine':
            code = 'UA'
        elif user_country =='United Arab Emirates':
            code = 'AE'
        elif user_country =='United Kingdom':
            code = 'GB'
        elif user_country =='United States':
            code = 'US'
        elif user_country =='United States Minor Outlying Islands':
            code = 'UM'
        elif user_country =='Uruguay':
            code = 'UY'
        elif user_country =='Uzbekistan':
            code = 'UZ'
        elif user_country =='Vanuatu':
            code = 'VU'
        elif user_country =='Vatican':
            code = 'VA'
        elif user_country =='Venezuela':
            code = 'VE'
        elif user_country =='Vietnam':
            code = 'VN'
        elif user_country =='Wallis and Futuna':
            code = 'WF'
        elif user_country =='Western Sahara':
            code = 'EH'
        elif user_country =='Yemen':
            code = 'YE'
        elif user_country =='Zambia':
            code = 'ZM'
        elif user_country =='Zimbabwe':
            code = 'ZW'
        connection = urllib.request.urlopen('http://vip.timezonedb.com/v2/get-time-zone?key=<your_key>&format=json&by=city&city=%s&country=%s'
                            % (
                                   user_city,
                                   code
                               ))
        js = connection.read()
        data = json.loads(js)
        if data['status'] == 'FAILED':
            self.assistant.say(data['message'])
        else:
            tme = data['zones'][0]['formatted']
            st = data['zones'][0]['regionName']
            cnt = data['zones'][0]['countryName']
            ct = data['zones'][0]['cityName']
            self.assistant.say("The time in %s %s %s is %s"
                               % (
                                   ct,
                                   st,
                                   cnt,
                                   tme
                               ))