from html.parser import HTMLParser
import pandas as pd 
import numpy as np

# Pate đoạn html có thẻ select option vào đây 
ht_ml = """
<select name="ctl00$MainContent$Cbohangxe" onchange="javascript:setTimeout('__doPostBack(\'ctl00$MainContent$Cbohangxe\',\'\')', 0)" id="MainContent_Cbohangxe" class="form-control">
	<option selected="selected" value="">--- Cần lựa chọn hãng xe ---</option>
	<option value="ACURA">ACURA</option>
	<option value="AUDI">AUDI</option>
	<option value="BMW">BMW</option>
	<option value="CHEVROLET">CHEVROLET</option>
	<option value="FIAT">FIAT</option>
	<option value="FORD">FORD</option>
	<option value="HONDA">HONDA</option>
	<option value="HYUNDAI">HYUNDAI</option>
	<option value="ISUZU">ISUZU</option>
	<option value="KIA">KIA</option>
	<option value="LANDROVER">LAND ROVER</option>
	<option value="LEXUS">LEXUS</option>
	<option value="MAZDA">MAZDA</option>
	<option value="MERCEDES-BENZ">MERCEDES-BENZ</option>
	<option value="MINICOOPER">MINI COOPER</option>
	<option value="MITSUBISHI">MITSUBISHI</option>
	<option value="NISSAN">NISSAN</option>
	<option value="PEUGEOT">PEUGEOT</option>
	<option value="PORSCHE">PORSCHE</option>
	<option value="RENAULT">RENAULT</option>
	<option value="SAMSUNG">SAMSUNG</option>
	<option value="SUZUKI">SUZUKI</option>
	<option value="THACO">THACO</option>
	<option value="TOYOTA">TOYOTA</option>
	<option value="VOLKSWAGEN">VOLKSWAGEN</option>
</select>
"""

my_array = []


class MyHTMLParser(HTMLParser):
    is_option_tag = False
    ar = []
    def handle_starttag(self, tag, attrs):
        if tag == 'option':
            self.is_option_tag = True
            for attr in attrs:
                if attr[0] == 'value':
                    self.ar.append(attr[1])

    def handle_endtag(self, tag):
        if tag == 'option':
            self.is_option_tag = False

    def handle_data(self, data):
        if self.is_option_tag == True:
            self.ar.append(data)
            my_array.append(self.ar)
            self.ar = []


parser = MyHTMLParser()


parser.feed(ht_ml)
arr = np.array(my_array)
pd.DataFrame(arr).to_csv("file.csv")

print(my_array)

print('oke')

