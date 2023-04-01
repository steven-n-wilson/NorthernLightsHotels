import os
import psycopg2
from psycopg2.extras import execute_values

conn = psycopg2.connect(
        host="localhost",
        database="flask_db",
        user="postgres",
        password="1123",
        port=5432
    )

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this create the tables

cur.execute('DROP TABLE IF EXISTS hotel_chain;')
cur.execute('CREATE TABLE hotel_chain ( name varchar(40) PRIMARY KEY,'
                                        'office_address text[6] NOT NULL,'
                                        'number_of_hotels int NOT NULL,'
                                        'phone_number varchar(12),'
                                        'email_address varchar(50));'
                                    )

cur.execute('DROP TABLE IF EXISTS hotel;')
cur.execute('CREATE TABLE hotel ( hotel_id int PRIMARY KEY,'
                                'owner_name varchar(40) NOT NULL,'
                                'star_rating int NOT NULL,'
                                'number_of_rooms int NOT NULL,'
                                'phone_number varchar(20),'
                                'email_address varchar(30));'
                            )

cur.execute('DROP TABLE IF EXISTS rent;')
cur.execute('CREATE TABLE rent (rent_id serial PRIMARY KEY,'
                                'booking_id int NOT NULL,'
                                'room_id int NOT NULL,'
                                'rent_date varchar(15),'
                                'customer_id int NOT NULL);')                                   

cur.execute('DROP TABLE IF EXISTS booking;')
cur.execute('CREATE TABLE booking ( booking_id serial PRIMARY KEY,'
                                    'room_number int NOT NULL,'
                                    'book_date varchar(15));'
                                    )    

cur.execute('DROP TABLE IF EXISTS customer;')
cur.execute('CREATE TABLE customer ( customer_id serial PRIMARY KEY,'
                                    'first_name varchar(20),'
                                    'last_name varchar(20),'
                                    'customer_address text[6],'
                                    'date_of_registration varchar(15));'
                                    )  

cur.execute('DROP TABLE IF EXISTS room;')
cur.execute('CREATE TABLE room ( room_id serial PRIMARY KEY,'
                                    'hotel_id int NOT NULL,'
                                    'room_number int NOT NULL,'
                                    'capacity int NOT NULL,'
                                    'isExtendable BOOLEAN NOT NULL,'
                                    'outdoor_view varchar(15),'
                                    'price decimal NOT NULL,'
                                    'problems text[],'
                                    'amenities text[],'
                                    'isAvailable BOOLEAN NOT NULL);'
                                    )  

cur.execute('DROP TABLE IF EXISTS hotel_addresses;')
cur.execute('CREATE TABLE hotel_addresses ( hotel_id int PRIMARY KEY,'
                                    'street varchar(70),'
                                    'city varchar(25),'
                                    'state_or_province varchar(25),'
                                    'country varchar(15),'
                                    'postal_code varchar(15));'
                                    ) 

cur.execute('DROP TABLE IF EXISTS employee;')
cur.execute('CREATE TABLE employee ( emp_id serial PRIMARY KEY,'
                                    'first_name varchar(20),'
                                    'last_name varchar(20),'
                                    'emp_role varchar(20),'
                                    'hotel_id int NOT NULL,'
                                    'street varchar(70),'
                                    'city varchar(20),'
                                    'state_or_province varchar(25),'
                                    'postal_code varchar(15),'
                                    'manager_id int REFERENCES employee(emp_id));'
                                    )

cur.execute('DROP TABLE IF EXISTS check_in;')
cur.execute('CREATE TABLE check_in ( SIN serial PRIMARY KEY,'
                                    'rent_date varchar(15),'
                                    'check_out_date varchar(15),'
                                    'reservation_type varchar(15));'
                                    ) 

cur.execute('DROP TABLE IF EXISTS archive;')
cur.execute('CREATE TABLE archive ( SIN serial PRIMARY KEY,'
                                    'book_date varchar(15),'
                                    'rent_date varchar(15));'
                                    ) 

cur.execute('DROP TABLE IF EXISTS payment;')
cur.execute('CREATE TABLE payment ( payment_id serial PRIMARY KEY,'
                                    'customer_id int NOT NULL,'
                                    'first_name varchar(10),'
                                    'last_name varchar(10),'
                                    'card_number varchar(20),'
                                    'date_of_expiration varchar(10),'
                                    'amount int NOT NULL);'
                                    ) 


# -- 1st Trigger for manager_id
# cur.execute("""
# CREATE OR REPLACE FUNCTION if_manager()
# RETURNS TRIGGER AS
# $$
# BEGIN
#     IF emp_role = 'manager'
#         INSERT INTO employee(manager_id)
#         VALUES (NEW.manager_id);
#     END IF;
#     RETURN NEW;
# END;
# $$ 
# """)


# Insert data into the table

# Employee:
execute_values(cur,
    'INSERT INTO employee (first_name, last_name, emp_role, hotel_id, street, city, state_or_province,postal_code) VALUES %s',
    [('Edgar','Acosta','room service/cleanup',2293202,'993 Peg Shop Court','Ottawa','Ontario','E4P-3P4'),
	('Rick','Jensen','check in service',2293202,'993 Peg Shop Court','Ottawa','Ontario','E4P-3P4'),
	('Steven','Wilson','manager',2293202,'993 Peg Shop Court','Ottawa','Ontario','E4P-3P4'),

	('Mark','Isidro','room service/cleanup',4119615,'48 Wetland Road','Ottawa','Ontario','N4L-0B4'),
	('Amado','Hieu','check in service',4119615,'48 Wetland Road','Ottawa','Ontario','N4L-0B4'),
	('Marcela','Marcus','manager',4119615,'48 Wetland Road','Ottawa','Ontario','N4L-0B4'),

	('Perlita','Haran','room service/cleanup',8170894,'7 W. Law Drive','Burlington','Vermont','67432'),
	('Theo','Lucero','check in service',8170894,'7 W. Law Drive','Burlington','Vermont','67432'),
	('Soraya','Casilda','manager',8170894,'7 W. Law Drive','Burlington','Vermont','67432'),

	('Aaron','Smith','room service/cleanup',1103371,'550 Globe Rd.','Toronto','Ontario','K2K-0C0'),
	('Randal','Winona','check in service',1103371,'550 Globe Rd.','Toronto','Ontario','K2K-0C0'),
	('Vincent','Pierce','manager',1103371,'550 Globe Rd.','Toronto','Ontario','K2K-0C0'),

	('Kinley','Whitney','room service/cleanup',6768926,'8 Corona Lane','Vancouver','British Columbia','V8B-2L6'),
	('Jacquelyn','Smith','check in service',6768926,'8 Corona Lane','Vancouver','British Columbia','V8B-2L6'),
	('Jesse','Oneida','manager',6768926,'8 Corona Lane','Vancouver','British Columbia','V8B-2L6'),

	('Ernest','Merla','room service/cleanup',6809581,'78 Peninsula Street','Montreal','Quebec','H9S-0E9'),
	('Maddie','Fred','check in service',6809581,'78 Peninsula Street','Montreal','Quebec','H9S-0E9'),
	('Blake','Paul','manager',6809581,'78 Peninsula Street','Montreal','Quebec','H9S-0E9'),

	('Chad','Ellis','room service/cleanup',5986244,'50 Clove Lane','Vancouver','British Columbia','T9S-3A5'),
	('Tyson','Tyrell','check in service',5986244,'50 Clove Lane','Vancouver','British Columbia','T9S-3A5'),
	('Bart','Issac','manager',5986244,'50 Clove Lane','Vancouver','British Columbia','T9S-3A5'),

	('Terry','Westly','room service/cleanup',3410170,'34 N. Sutor Dr','Winnipeg','Manitoba','R5H-1E0'),
	('Sheldon','Don','check in service',3410170,'34 N. Sutor Dr','Winnipeg','Manitoba','R5H-1E0'),
	('Nathan','Gilmore','manager',3410170,'34 N. Sutor Dr','Winnipeg','Manitoba','R5H-1E0'),

	('Corey','Wilson','room service/cleanup',4334270,'585 Gray Road','Montreal','Quebec','G6B-2T1'),
	('Liam','Matthews','check in service',4334270,'585 Gray Road','Montreal','Quebec','G6B-2T1'),
	('Arturo','Sanchez','manager',4334270,'585 Gray Road','Montreal','Quebec','G6B-2T1'),

	('Marcel','Jerold','room service/cleanup',9623723,'63 Ivory Rd','Baltimore','Maryland','03853'),
	('Harold','Izaiah','check in service',9623723,'63 Ivory Rd','Baltimore','Maryland','03853'),
	('Rowley','Sylvester','manager',9623723,'63 Ivory Rd','Baltimore','Maryland','03853'),

	('Cedric','Warwick','room service/cleanup',6824294,'6 Kent Rd','Washington','District of Columbia','88256'),
	('Blythe','Cara','check in service',6824294,'6 Kent Rd','Washington','District of Columbia','88256'),
	('Rodolfo','Liza','manager',6824294,'6 Kent Rd','Washington','District of Columbia','88256'),

	('Mavec','Collins','room service/cleanup',9840412,'224 W. Lavender Circle','Newark','New Jersey','08472'),
	('Sean','Ester','check in service',9840412,'224 W. Lavender Circle','Newark','New Jersey','08472'),
	('Caridad','Lopez','manager',9840412,'224 W. Lavender Circle','Newark','New Jersey','08472'),

	('John','Coolidge','room service/cleanup',7243660,'1 Summit St','Chicago','Illinois','76738'),
	('Cesar','Marcelino','check in service',7243660,'1 Summit St','Chicago','Illinois','76738'),
	('Taylor','Leatrice','manager',7243660,'1 Summit St','Chicago','Illinois','76738'),

	('Alex','Hudson','room service/cleanup',5125040,'19 Gravel St','Chicago','Illinois','87873'),
	('Tyler','McCormick','check in service',5125040,'19 Gravel St','Chicago','Illinois','87873'),
	('Adam','Bank','manager',5125040,'19 Gravel St','Chicago','Illinois','87873'),

	('Grey','Brant','room service/cleanup',4977925,'808 Duchess St','Newark','New Jersey','52869'),
	('Collin','McCarbhail','check in service',4977925,'808 Duchess St','Newark','New Jersey','52869'),
	('Jacob','Norris','manager',4977925,'808 Duchess St','Newark','New Jersey','52869'),

	('Arnold','Switzer','room service/cleanup',9793288,'23 Garnet Road','Baltimore','Maryland','77368'),
	('Megan','Jon','check in service',9793288,'23 Garnet Road','Baltimore','Maryland','77368'),
	('Ivan','Morrison','manager',9793288,'23 Garnet Road','Baltimore','Maryland','77368'),

	('Eric','Danilo','room service/cleanup',4891957,'691 Tower Drive','Cleveland','Ohio','99357'),
	('Amanda','Jude','check in service',4891957,'691 Tower Drive','Cleveland','Ohio','99357'),
	('Jim','Casarubias','manager',4891957,'691 Tower Drive','Cleveland','Ohio','99357'),

	('Silas','Tate','room service/cleanup',7772350,'33 Haven Rd','New York','New Jersey','33876'),
	('Loreen','Dannet','check in service',7772350,'33 Haven Rd','New York','New Jersey','33876'),
	('Alicia','Winthrop','manager',7772350,'33 Haven Rd','New York','New Jersey','33876'),

	('Ezra','Hawthorne','room service/cleanup',3367760,'1 Tarkiln Hill St','Kelowna','British Columbia','E5B-2R2'),
	('Monica','Miriam','check in service',3367760,'1 Tarkiln Hill St','Kelowna','British Columbia','E5B-2R2'),
	('Bernice','Blaze','manager',3367760,'1 Tarkiln Hill St','Kelowna','British Columbia','E5B-2R2'),

	('Sydney','Carly','room service/cleanup',3295605,'87 Beech Dr','Calgary','Alberta','T9E-3E7'),
	('Sheryl','McGrady','check in service',3295605,'87 Beech Dr','Calgary','Alberta','T9E-3E7'),
	('Nelly','Curry','manager',3295605,'87 Beech Dr','Calgary','Alberta','T9E-3E7'),

	('Michael','Winter','room service/cleanup',6885722,'58 Winter Road','Calgary','Alberta','T4S-0B9'),
	('Liv','Sharla','check in service',6885722,'58 Winter Road','Calgary','Alberta','T4S-0B9'),
	('Amancio','Gutierrez','manager',6885722,'58 Winter Road','Calgary','Alberta','T4S-0B9'),

	('Thomas','Ross','room service/cleanup',8927171,'70 Copper St','Saskatoon','Saskatchewan','S9H-2V2'),
	('Alonso','Entrerios','check in service',8927171,'70 Copper St','Saskatoon','Saskatchewan','S9H-2V2'),
	('Eugene','Sergio','manager',8927171,'70 Copper St','Saskatoon','Saskatchewan','S9H-2V2'),

	('Camille','Mariel','room service/cleanup',5057696,'3 North Maiden','Regina','Saskatchewan','H3X-1X2'),
	('Merilee','Merrick','check in service',5057696,'3 North Maiden','Regina','Saskatchewan','H3X-1X2'),
	('Teofilo','Alarcon','manager',5057696,'3 North Maiden','Regina','Saskatchewan','H3X-1X2'),

	('Winslow','Presley','room service/cleanup',1791025,'67 Atlantic Dr','Toronto','Ontario','N9V-2H1'),
	('Ronald','Santos','check in service',1791025,'67 Atlantic Dr','Toronto','Ontario','N9V-2H1'),
	('Donald','Grant','manager',1791025,'67 Atlantic Dr','Toronto','Ontario','N9V-2H1'),

	('Roy','Coleman','room service/cleanup',8002651,'78 Gem Avenue','Montgomery','Alabama','65836'),
	('Trish','Michaels','check in service',8002651,'78 Gem Avenue','Montgomery','Alabama','65836'),
	('Hallie','Selasie','manager',8002651,'78 Gem Avenue','Montgomery','Alabama','65836'),

	('Gerard','Visser','room service/cleanup',1893428,'31 Del Monte St','Birmingham','Alabama','28773'),
	('Nicolas','Cage','check in service',1893428,'31 Del Monte St','Birmingham','Alabama','28773'),
	('Lois','Simpson','manager',1893428,'31 Del Monte St','Birmingham','Alabama','28773'),

	('Mackenzie','Clark','room service/cleanup',7778568,'280 Paradise Rd','Atlanta','Georgia','96745'),
	('James','Wilma','check in service',7778568,'31 Del Monte St','Birmingham','Alabama','28773'),
	('Sanford','Hernando','manager',7778568,'31 Del Monte St','Birmingham','Alabama','28773'),

	('Clark','Paca','room service/cleanup',1669786,'9 Grotto St','Halifax','Nova Scotia','E6G-0B5'),
	('William','Power','check in service',1669786,'9 Grotto St','Halifax','Nova Scotia','E6G-0B5'),
	('Jasmine','Carmel','manager',1669786,'9 Grotto St','Halifax','Nova Scotia','E6G-0B5'),

	('Jaye','Watson','room service/cleanup',8791885,'382 Winding Way','Dallas','Texas','67485'),
	('Felix','Alisha','check in service',8791885,'382 Winding Way','Dallas','Texas','67485'),
	('Christine','Colton','manager',8791885,'382 Winding Way','Dallas','Texas','67485'),

	('Gabriel','Price','room service/cleanup',9413435,'13 Penn Dr','Dallas','Texas','29567'),
	('Percy','Smith','check in service',9413435,'13 Penn Dr','Dallas','Texas','29567'),
	('Juan','Casanueva','manager',9413435,'13 Penn Dr','Dallas','Texas','29567'),

	('Alec','Dezi','room service/cleanup',9933506,'181 Bay Drive','Fort Lauderdale','Florida','85742'),
	('Alexa','Edwyn','check in service',9933506,'181 Bay Drive','Fort Lauderdale','Florida','85742'),
	('Timothy','Zac','manager',9933506,'181 Bay Drive','Fort Lauderdale','Florida','85742'),

	('Mark','Omar','room service/cleanup',2512675,'3 Mayflower St','New Orleans','Louisiana','79475'),
	('Noah','Abarca','check in service',2512675,'3 Mayflower St','New Orleans','Louisiana','79475'),
	('Eric','Hayes','manager',2512675,'3 Mayflower St','New Orleans','Louisiana','79475'),

	('Steven','Crew','room service/cleanup',1010187,'5 Nicolls St','Miami','Florida','19374'),
	('Cindy','Nicanor','check in service',1010187,'5 Nicolls St','Miami','Florida','19374'),
	('Carol','Stafford','manager',1010187,'5 Nicolls St','Miami','Florida','19374'),

	('Andy','Alfreda','room service/cleanup',8496001,'31 Barley St','Orlando','Florida','97738'),
	('Phil','Gauthier','check in service',8496001,'31 Barley St','Orlando','Florida','97738'),
	('Valerie','Lauderdale','manager',8496001,'31 Barley St','Orlando','Florida','97738'),

	('Jess','Orson','room service/cleanup',3202411,'61 Greenrose Street','Houston','Texas','18576'),
	('Josephine','Seton','check in service',3202411,'61 Greenrose Street','Houston','Texas','18576'),
	('Bryon','Salina','manager',3202411,'61 Greenrose Street','Houston','Texas','18576'),

	('Tom','Solomon','room service/cleanup',9615817,'15 Mammoth Ave','Biloxi','Mississippi','08674'),
	('Pauline','Smith','check in service',9615817,'15 Mammoth Ave','Biloxi','Mississippi','08674'),
	('Mark','Sanchez','manager',9615817,'15 Mammoth Ave','Biloxi','Mississippi','08674'),

	('Silvio','Rodriguez','room service/cleanup',5894110,'42 Lower Ave','Austin','Texas','18476'),
	('Katy','Renie','check in service',5894110,'42 Lower Ave','Austin','Texas','18476'),
	('Clara','Martinez','manager',5894110,'42 Lower Ave','Austin','Texas','18476'),

	('Greg','Houston','room service/cleanup',3371676,'77 Laurel Rd','Edmonton','Alberta','T1M-3J1'),
	('Dimitri','Monique','check in service',3371676,'77 Laurel Rd','Edmonton','Alberta','T1M-3J1'),
	('George','Marcus','manager',3371676,'77 Laurel Rd','Edmonton','Alberta','T1M-3J1'),

	('Claude','Williams','room service/cleanup',8926680,'49 Mill Rd','Quebec City','Quebec','J8L-1A5'),
	('Ike','Tyke','check in service',8926680,'49 Mill Rd','Quebec City','Quebec','J8L-1A5'),
	('Lindsay','Morris','manager',8926680,'49 Mill Rd','Quebec City','Quebec','J8L-1A5'),

	('Angel','Santos','room service/cleanup',9581598,'327 Wrangler Ave','Iqaluit','Nunavut','J1N-0E5'),
	('Jeanne','Careen','check in service',9581598,'327 Wrangler Ave','Iqaluit','Nunavut','J1N-0E5'),
	('James','Lilibet','manager',9581598,'327 Wrangler Ave','Iqaluit','Nunavut','J1N-0E5'),

	('Aubrey','Pip','room service/cleanup',6244341,'39 Oak Meadow St','Edmonton','Alberta','T9X-0X6'),
	('Tyler','Grant','check in service',6244341,'39 Oak Meadow St','Edmonton','Alberta','T9X-0X6'),
	('Graham','Cracker','manager',6244341,'39 Oak Meadow St','Edmonton','Alberta','T9X-0X6'),

	('Lesley','Smith','room service/cleanup',3170033,'9 E. Water Lane','Yellowknife','Northwest Territories','A1X-0P7'),
	('Sam','Wes','check in service',3170033,'9 E. Water Lane','Yellowknife','Northwest Territories','A1X-0P7'),
	('Gerald','Miller','manager',3170033,'9 E. Water Lane','Yellowknife','Northwest Territories','A1X-0P7'),
    ('Darcy','McGee','room service/cleanup',4270962,'12 Sherman Drive','Whitehorse','Yukon','A1L-2L3'),
	('Ben','Nowell','check in service',4270962,'12 Sherman Drive','Whitehorse','Yukon','A1L-2L3'),
	('Tom','Rojan','manager',4270962,'12 Sherman Drive','Whitehorse','Yukon','A1L-2L3'),

	('Edmond','Blair','room service/cleanup',3723682,'38 Dogwood St','Anchorage','Alaska','05837'),
	('Sharon','Roman','check in service',3723682,'38 Dogwood St','Anchorage','Alaska','05837'),
	('Thomas','Esguerra','manager',3723682,'38 Dogwood St','Anchorage','Alaska','05837'),

	('Tony','Peralta','room service/cleanup',2412724,'3 Pine Road','Kelowna','British Columbia','V1N-3H4'),
	('Quinton','Zed','check in service',2412724,'3 Pine Road','Kelowna','British Columbia','V1N-3H4'),
	('Ted','Marley','manager',2412724,'3 Pine Road','Kelowna','British Columbia','V1N-3H4')])

# Hotel Addresses :
execute_values(cur,
    'INSERT INTO hotel_addresses (hotel_id,street,city,state_or_province,country,postal_code) VALUES %s',
    [(2293202,'7028 Riverside Drive','Ottawa','Ontario','CAN','K7C 0E1'),
	(4119615,'500 Opus Avenue','Ottawa','Ontario','CAN','K9F 8V1'),
	(8170894,'4837 Selah Way','Burlington','Vermont','USA','03755'),
	(1103371,'52 Myrtle Lane','Toronto','Ontario','CAN','M4W 0R7'),
	(6768926,'154 Lookout Drive','Vancouver','British Columbia','CAN','V5K 1P3'),
	(6809581,'724 Riverview Street','Montreal','Quebec','CAN','H2Y 1W7'),
	(5986244,'2 Harrison Street','Vancouver','British Columbia','CAN','V5K 1W5'),
	(3410170,'9676 Randall Mill Road','Winnipeg','Manitoba','CAN','R2C 1R2'),
	(4334270,'67 Bridgeway Avenue','Montreal','Quebec','CAN','H1Z 1J2'),
	(9623723,'9000 Moon Parkway','Baltimore','Maryland','USA','27710'),
	(6824294,'4521 Rhode Street','Washington','District of Columbia','USA','20036'),
	(9840412,'2842 Picnic Street','Newark','New Jersey','USA','07107'),
	(7243660,'4202 University Drive','Chicago','Illinois','USA','80035'),
	(5125040,'3259 West Drive','Chicago','Illinois','USA','81818'),
	(4977925,'7890 Country Avenue','Newark','New Jersey','USA','07998'),
	(9793288,'5678 Motor Drive','Baltimore','Maryland','USA','27680'),
	(4891957,'2341 Lakeview Avenue','Cleveland','Ohio','USA','44115'),
	(7772350,'4863 Slough Parkway','New York','New Jersey','USA','07898'),
	(3367760,'7896 Parker Way','Kelowna','British Columbia','CAN','Y2K 2U9'),
	(3295605,'7450 Flea Road','Calgary','Alberta','CAN','C1A 5F9'),
	(6885722,'3812 Cockroach Way','Calgary','Alberta','CAN','C2B 4I8'),
	(8927171,'1100 Condor Street','Saskatoon','Saskatchewan','CAN','F2R 7B4'),
	(5057696,'2525 Eagleview Avenue','Regina','Saskatchewan','CAN','G81 3H0'),
	(1791025,'2900 Younge Street','Toronto','Ontario','CAN','M8Y 1G9'),
	(8002651,'8800 Sprat Way','Montgomery','Alabama','USA','36710'),
	(1893428,'643 Locust Street','Birmingham','Alabama','USA','34277'),
	(7778568,'351 Delta Way','Atlanta','Georgia','USA','30338'),
	(1669786,'210 Lobster Road','Halifax','Nova Scotia','CAN','J1J 4K1'),
	(8791885,'9750 Hospitality Road','Dallas','Texas','USA','75500'),
	(9413435,'651 Rodeo Avenue','Dallas','Texas','USA','74480'),
	(9933506,'3300 Beach Way','Fort Lauderdale','Florida','USA','36800'),
	(2512675,'1414 Carnaval Street','New Orleans','Louisiana','USA','70358'),
	(1010187,'323 Surf Road','Miami','Florida','USA','34080'),
	(8496001,'1880 Yacht Avenue','Orlando','Florida','USA','37900'),
	(3202411,'275 Insurgentes Avenue','Houston','Texas','USA','77800'),
	(9615817,'100 River Way','Biloxi','Mississippi','USA','39201'),
	(5894110,'757 Rose Street','Austin','Texas','USA','35954'),
	(3371676,'750 Igloo Street','Edmonton','Alberta','CAN','C1A 5F9'),
	(8926680,'400 Duplessis Street','Quebec City','Quebec','CAN','G1T 5L1'),
	(9581598,'150 Manitou Road','Iqaluit','Nunavut','CAN','X1D 5D2'),
	(6244341,'78 Radisson Avenue','Edmonton','Alberta','CAN','C5G 9X3'),
	(3170033,'202 Caribou Road','Yellowknife','Northwest Territories','CAN','Y7A 2Q4'),
	(4270962,'397 Via Borealis','Whitehorse','Yukon','CAN','W3I 0B7'),
	(3723682,'372 Husky Street','Anchorage','Alaska','USA','99504'),
	(2412724,'500 Alpine Road','Kelowna','British Columbia','CAN','Y0I 4M3')])
  
# Hotel :
execute_values(cur,
    'INSERT INTO hotel (hotel_id,owner_name, star_rating, number_of_rooms, phone_number, email_address) VALUES %s',
    [	(2293202,'Wilson Hotels',5,5,'18007835626','riverside@wilson.com'),
	(4119615,'Wilson Hotels',4,7,'18002572001','hotels@wilson.com'),
	(8170894,'Wilson Hotels',4,5,'18006490808','hannover@wilson.com'),
	(1103371,'Wilson Hotels',4,5,'18004181120','myrtle@wilson.com'),
	(6768926,'Wilson Hotels',5,8,'18004929235','lookout@wilson.com'),
	(6809581,'Wilson Hotels',4,7,'18009134385','riverview@wilson.com'),
	(5986244,'Wilson Hotels',5,5,'180040409083','harrison@wilson.com'),
	(3410170,'Wilson Hotels',5,7,'18005923510','winnipeg@wilson.com'),
	(4334270,'Wilson Hotels',5,8,'18884076432','bridgeway@wilson.com'),
	(9623723,'Goodnite Hostels',5,5,'1800700100','hostels@goodnite.com'),
	(6824294,'Goodnite Hostels',5,7,'1800419806','dc@goodnite.com'),
	(9840412,'Goodnite Hostels',5,5,'18008244274','picnic@goodnite.com'),
	(7243660,'Goodnite Hostels',3,7,'18000875820','university@goodnite.com'),
	(5125040,'Goodnite Hostels',4,5,'18005423027','west@goodnite.com'),
	(4977925,'Goodnite Hostels',4,5,'18001236743','country@goodnite.com'),
	(9793288,'Goodnite Hostels',3,5,'18006785024','motor@goodnite.com'),
	(4891957,'Goodnite Hostels',2,5,'18008739854','cleveland@goodnite.com'),
	(7772350,'Goodnite Hostels',2,5,'1800462543','newyork@goodnite.com'),
	(3367760,'Goodnite Hostels',5,5,'18007774890','kelowna@goodnite.com'),
	(3295605,'Bugsfree Inn',5,7,'18006543215','inn@bugsfree.com'),
	(6885722,'Bugsfree Inn',4,7,'18007892010','cockroach@bugsfree.com'),
	(8927171,'Bugsfree Inn',4,7,'1800484800','saskatoon@bugsfree.com'),
	(5057696,'Bugsfree Inn',4,7,'18008887777','regina@bugsfree.com'),
	(1791025,'Bugsfree Inn',3,7,'18001112222','buggy@bugsfree.com'),
	(8002651,'Bugsfree Inn',3,5,'18007402482','montgomery@bugsfree.com'),
	(1893428,'Bugsfree Inn',3,5,'18005543320','birmingham@bugsfree.com'),
	(7778568,'Bugsfree Inn',4,7,'18004632377','atlanta@bugsfree.com'),
	(1669786,'Bugsfree Inn',4,5,'18004529900','halifax@bugsfree.com'),

	(8791885,'Southern BnB',5,8,'18002389601','bnb@southern.com'),
	(9413435,'Southern BnB',5,7,'18003498712','rodeo@southern.com'),
	(9933506,'Southern BnB',5,9,'18006018410','lauderdale@southern.com'),
	(2512675,'Southern BnB',5,8,'18007877454','neworleans@southern.com'),
	(1010187,'Southern BnB',5,7,'18008334884','miami@southern.com'),
	(8496001,'Southern BnB',5,8,'18007036955','orlando@southern.com'),
	(3202411,'Southern BnB',5,7,'18006556125','houston@southern.com'),
	(9615817,'Southern BnB',4,5,'18005238263','biloxi@southern.com'),
	(5894110,'Southern BnB',4,5,'18005140558','austin@southern.com'),
	
	(3371676,'Truenorth Lodge',5,7,'1800080874','lodge@truenorth.com'),
	(8926680,'Truenorth Lodge',5,10,'18004407066','quebec@truenorth.com'),
	(9581598,'Truenorth Lodge',5,5,'18003662279','iqaluit@truenorth.com'),
	(6244341,'Truenorth Lodge',4,7,'18004993511','radisson@truenorth.com'),
	(3170033,'Truenorth Lodge',5,7,'18009687905','yellowknife@truenorth.com'),
	(4270962,'Truenorth Lodge',5,8,'18007050508','whitehorse@truenorth.com'),
	(3723682,'Truenorth Lodge',5,5,'18003386431','alaska@truenorth.com'),
	(2412724,'Truenorth Lodge',5,5,'1800783649','kelowna@truenorth.com')])

# Rooms
execute_values(cur,
    'INSERT INTO room (hotel_id, room_number, capacity, isExtendable, outdoor_view, price, problems, amenities,isAvailable) VALUES %s',
    [(2293202,101,1,'no','street',50,'{"Leaky faucet"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(2293202,102,2,'no','river',100,'{"none"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(2293202,103,2,'no','street',100,'{"Leaky faucet"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(2293202,201,2,'yes','street',100,'{"none"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(2293202,202,7,'no','river',300,'{"none"}','{"Shower","TV","Internet","Free towels,sauna,room service"}','yes'),
	(4119615,101,1,'no','street',50,'{"Leaky faucet","bedbugs"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(4119615,102,2,'yes','street',100,'{"none"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(4119615,201,2,'no','street',100,'{"Leaky faucet"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(4119615,202,4,'no','river',200,'{"none"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(4119615,301,7,'no','street',300,'{"Stained carpet"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(4119615,302,7,'no','street',300,'{"none"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(4119615,400,7,'no','street',300,'{"none"}','{"Shower","TV","Internet","Free towels", "sauna", "room service"}','yes'),
	(8170894,101,1,'no','street',50,'{"bedbugs"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(8170894,102,2,'no','forest',100,'{"none"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(8170894,201,2,'no','street',100,'{"stained carpet"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(8170894,202,4,'no','street',200,'{"none"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(8170894,300,7,'no','street',300,'{"none"}','{"Shower","TV","Internet","Free towels","sauna","room service"}','yes'),
	(1103371,101,1,'no','street',50,'{"bedbugs"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(1103371,102,2,'yes','street',100,'{"bedbugs"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(1103371,201,2,'yes','street',100,'{"none"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(1103371,202,4,'no','street',200,'{"bedbugs"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(1103371,300,7,'no','street',300,'{"leaky shower"}','{"Shower","TV","Internet","Free towels","sauna","room service"}','yes'),
	(6768926,101,1,'no','street',50,'{"leaky shower"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(6768926,102,2,'no','coast',100,'{"none"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(6768926,103,2,'yes','forest',150,'{"none"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(6768926,201,2,'no','coast',100,'{"none"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(6768926,202,4,'no','coast',200,'{"none"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(6768926,203,4,'yes','street',200,'{"none"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(6768926,301,7,'no','forest',300,'{"none"}','{"Shower","TV","Internet","Free towels","sauna","room service"}','yes'),
	(6768926,302,7,'no','coast',300,'{"none"}','{"Shower","TV","Internet","Free towels","sauna","room service"}','yes'),
	(6809581,101,1,'no','street',50,'{"leaky shower","bedbugs"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(6809581,102,2,'no','street',100,'{"bedbugs"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(6809581,201,2,'no','street',100,'{"leaky faucet"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(6809581,202,2,'no','street',100,'{"leaky faucet"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(6809581,203,4,'yes','street',250,'{"leaky faucet"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(6809581,301,7,'no','street',300,'{"leaky faucet"}','{"Shower","TV","Internet","Free towels","sauna","room service"}','yes'),
	(6809581,302,7,'no','street',300,'{"none"}','{"Shower","TV","Internet","Free towels","sauna","room service"}','yes'),
	(5986244,101,1,'yes','Coast',50,'{"none"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(5986244,102,2,'no','street',100,'{"none"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(5986244,201,2,'yes','coast',100,'{"none"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(5986244,202,4,'no','street',200,'{"none"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(5986244,300,7,'no','coast',300,'{"none"}','{"Shower","TV","Internet","Free towels","sauna","room service"}','yes'),
	(3410170,101,1,'no','street',50,'{"none"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(3410170,102,2,'no','park',100,'{"none"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(3410170,201,2,'no','street',100,'{"none"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(3410170,202,2,'yes','park',100,'{"none"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(3410170,301,4,'no','street',200,'{"none"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(3410170,302,4,'no','park',200,'{"none"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(3410170,400,7,'no','park',300,'{"none"}','{"Shower","TV","Internet","Free towels","sauna","room service"}','yes'),
	(4334270,101,1,'no','street',50,'{"none"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(4334270,102,1,'no','street',50,'{"none"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(4334270,103,2,'no','river',100,'{"none"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(4334270,201,2,'yes','street',150,'{"none"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(4334270,202,4,'no','river',100,'{"none"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(4334270,203,4,'yes','river',150,'{"none"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(4334270,301,7,'no','street',300,'{"none"}','{"Shower","TV","Internet","Free towels","sauna","room service"}','yes'),
	(4334270,302,7,'no','river',300,'{"none"}','{"Shower","TV","Internet","Free towels","sauna","room service"}','yes'),

	(9623723,101,1,'no','street',50,'{"none"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(9623723,102,2,'no','street',200,'{"none"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(9623723,201,2,'no','street',200,'{"none"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(9623723,202,4,'yes','street',250,'{"none"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(9623723,300,7,'no','street',300,'{"none"}','{"Shower","TV","Internet","Free towels","sauna","room service"}','yes'),
	(6824294,101,1,'no','none',50,'{"none"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(6824294,102,1,'yes','street',50,'{"none"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(6824294,201,2,'no','street',100,'{"none"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(6824294,202,2,'yes','street',150,'{"none"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(6824294,301,4,'no','street',200,'{"none"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(6824294,302,4,'no','street',200,'{"none"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(6824294,400,7,'no','street',300,'{"none"}','{"Shower","TV","Internet","Free towels","sauna","room service"}','yes'),
	(9840412,101,1,'yes','park',50,'{"none"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(9840412,102,2,'no','park',100,'{"none"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(9840412,201,2,'yes','park',150,'{"none"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(9840412,202,4,'no','park',200,'{"none"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(9840412,300,7,'no','park',300,'{"none"}','{"Shower","TV","Internet","Free towels","sauna","room service"}','yes'),
	(7243660,101,1,'no','none',50,'{"bedbugs","stained carpet","leaky shower"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(7243660,102,1,'no','street',50,'{"bedbugs","stained carpet","cracked wall"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(7243660,201,2,'no','alleyway',100,'{"bedbugs","leaky faucet"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(7243660,202,2,'no','alleyway',100,'{"bedbugs","stained carpet"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(7243660,301,4,'no','none',200,'{"bedbugs","smelly bathroom"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(7243660,302,4,'no','street',200,'{"bedbugs","stained carpet"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(7243660,400,7,'no','street',300,'{"bedbugs"}','{"Shower","TV","Internet","Free towels","room service"}','yes'),
	(5125040,101,1,'yes','street',50,'{"stained carpet"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(5125040,102,2,'no','street',100,'{"leaky shower"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(5125040,201,2,'yes','street',150,'{"leaky faucet"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(5125040,202,4,'no','street',100,'{"stained carpet"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(5125040,300,7,'no','street',300,'{"none"}','{"Shower","TV","Internet","Free towels","sauna","room service"}','yes'),
	(4977925,101,1,'no','street',50,'{"stained carpet"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(4977925,102,2,'no','park',100,'{"leaky faucet"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(4977925,201,2,'no','street',100,'{"stained carpet"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(4977925,202,4,'no','park',200,'{"stained carpet"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(4977925,300,7,'no','park',300,'{"none"}','{"Shower","TV","Internet","Free towels","sauna","room service"}','yes'),
	(9793288,101,1,'no','park',50,'{"bedbugs","stained carpet","leaky shower"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(9793288,102,2,'no','street',100,'{"stained carpet","leaky shower"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(9793288,201,2,'no','park',100,'{"bedbugs","leaky shower"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(9793288,202,4,'no','river',200,'{"bedbugs","stained carpet"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(9793288,300,7,'no','park',300,'{"leaky shower"}','{"Shower","TV","Internet","Free towels","sauna","room service"}','yes'),
	(4891957,101,1,'no','alleyway',50,'{"bedbugs","stained carpet","leaky shower","smelly bathroom"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(4891957,102,2,'no','street',100,'{"bedbugs","stained carpet","leaky shower","smelly bathroom"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(4891957,201,2,'no','alleyway',100,'{"bedbugs","stained carpet","leaky shower","smelly bathroom"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(4891957,202,4,'no','alleyway',200,'{"bedbugs","stained carpet","leaky shower","smelly bathroom"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(4891957,300,7,'no','park',300,'{"bedbugs","smelly bathroom"}','{"Shower","TV","Internet","Free towels","room service"}','yes'),
	(7772350,101,1,'no','alleyway',50,'{"bedbugs","stained carpet","leaky shower","smelly bathroom"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(7772350,102,2,'no','street',100,'{"bedbugs","stained carpet","leaky shower","smelly bathroom"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(7772350,201,2,'no','alleyway',100,'{"bedbugs","stained carpet","leaky shower","smelly bathroom"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(7772350,202,4,'no','alleyway',200,'{"bedbugs","stained carpet","leaky shower","smelly bathroom"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(7772350,300,7,'no','park',300,'{"bedbugs"}','{"Shower","TV","Internet","Free towels","room service"}','yes'),
	(3367760,101,1,'yes','park',50,'{"none"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(3367760,102,2,'yes','mountain',100,'{"none"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(3367760,201,2,'yes','mountain',150,'{"none"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(3367760,202,4,'yes','mountain',250,'{"none"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(3367760,300,7,'no','mountain',300,'{"none"}','{"Shower","TV","Internet","Free towels","sauna","room service"}','yes'),

	(3295605,101,1,'no','park',50,'{"none"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(3295605,102,1,'yes','street',50,'{"none"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(3295605,201,2,'no','park',100,'{"none"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(3295605,202,2,'yes','park',150,'{"none"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(3295605,301,4,'yes','park',250,'{"none"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(3295605,302,4,'yes','park',250,'{"none"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(3295605,400,7,'no','park',300,'{"none"}','{"Shower","TV","Internet","Free towels","sauna","room service"}','yes'),
	(6885722,101,1,'yes','street',50,'{"stained carpet"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(6885722,102,2,'no','street',100,'{"cockroaches"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(6885722,201,2,'no','street',100,'{"stained carpet"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(6885722,202,2,'no','street',100,'{"stained carpet"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(6885722,301,4,'no','street',200,'{"stained carpet"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(6885722,302,4,'yes','street',250,'{"stained carpet"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(6885722,400,7,'no','street',300,'{"none"}','{"Shower","TV","Internet","Free towels","sauna","room service"}','yes'),
	(8927171,101,1,'no','street',50,'{"bedbugs"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(8927171,102,1,'no','street',50,'{"stained carpet"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(8927171,201,2,'yes','street',150,'{"stained carpet"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(8927171,202,2,'no','street',100,'{"stained carpet"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(8927171,301,4,'yes','street',250,'{"stained carpet"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(8927171,302,4,'no','street',200,'{"stained carpet"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(8927171,400,7,'no','street',300,'{"none"}','{"Shower","TV","Internet","Free towels","sauna","room service"}','yes'),
	(5057696,101,1,'no','street',50,'{"stained carpet"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(5057696,102,1,'yes','park',50,'{"leaky faucet"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(5057696,201,2,'no','river',100,'{"stained carpet"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(5057696,202,2,'no','street',100,'{"leaky shower"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(5057696,301,4,'no','river',200,'{"smelly bathroom"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(5057696,302,4,'no','park',200,'{"none"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(5057696,400,7,'no','river',300,'{"none"}','{"Shower","TV","Internet","Free towels","sauna","room service"}','yes'),
	(1791025,101,1,'no','street',50,'{"stained carpet","bedbugs"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(1791025,102,1,'no','street',50,'{"stained carpet","cockroaches"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(1791025,201,2,'no','alleyway',100,'{"stained carpet","leaky faucet"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(1791025,202,2,'no','street',100,'{"stained carpet","smelly bathroom"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(1791025,301,4,'no','street',200,'{"stained carpet","bedbugs"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(1791025,302,4,'no','street',200,'{"stained carpet","leaky shower"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(1791025,400,7,'no','street',300,'{"stained carpet"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(8002651,101,1,'no','alleyway',50,'{"stained carpet","bedbugs","smelly bathroom"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(8002651,102,2,'no','street',100,'{"stained carpet","bedbugs"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(8002651,201,2,'no','street',100,'{"stained carpet","bedbugs"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(8002651,202,4,'no','street',200,'{"stained carpet","bedbugs"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(8002651,300,7,'no','street',300,'{"stained carpet"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(1893428,101,1,'no','alleyway',50,'{"stained carpet","locusts","smelly bathroom"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(1893428,102,2,'no','park',100,'{"stained carpet","bedbugs"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(1893428,201,2,'no','alleyway',100,'{"stained carpet","bedbugs","smelly bathroom"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(1893428,202,4,'no','alleyway',200,'{"stained carpet","bedbugs","smelly bathroom"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(1893428,300,7,'no','street',300,'{"stained carpet"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(7778568,101,1,'no','park',50,'{"stained carpet","smelly bathroom"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(7778568,102,1,'no','street',50,'{"smelly bathroom"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(7778568,201,2,'no','park',100,'{"leaky faucet"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(7778568,202,2,'no','park',100,'{"leaky shower"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(7778568,301,4,'no','river',200,'{"none"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(7778568,302,4,'no','park',200,'{"none"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(7778568,400,7,'no','park',300,'{"none"}','{"Shower","TV","Internet","Free towels","sauna","room service"}','yes'),
	(1669786,101,1,'no','park',50,'{"stained carpet","smelly bathroom"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(1669786,102,2,'no','street',100,'{"stained carpet"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(1669786,201,2,'yes','park',150,'{"smelly bathroom"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(1669786,202,4,'no','park',200,'{"none"}','{"Shower","TV","Internet","Free towels"}','yes'),
	(1669786,300,7,'no','river',300,'{"none"}','{"Shower","TV","Internet","Free towels","sauna","room service"}','yes'),

	(8791885,101,1,'no','street',50,'{"none"}','{"Shower","TV","Internet","Free towels","Free breakfast"}','yes'),
	(8791885,102,1,'yes','river',50,'{"none"}','{"Shower","TV","Internet","Free towels","Free breakfast"}','yes'),
	(8791885,201,2,'no','meadow',100,'{"none"}','{"Shower","TV","Internet","Free towels","Free breakfast"}','yes'),
	(8791885,202,2,'yes','park',150,'{"none"}','{"Shower","TV","Internet","Free towels","Free breakfast"}','yes'),
	(8791885,301,4,'yes','street',200,'{"none"}','{"Shower","TV","Internet","Free towels","Free breakfast"}','yes'),
	(8791885,302,4,'yes','park',200,'{"none"}','{"Shower","TV","Internet","Free towels","Free breakfast"}','yes'),
	(8791885,401,7,'no','street',300,'{"none"}','{"Shower","TV","Internet","Free towels","Free breakfast"}','yes'),
	(8791885,402,7,'no','lake',300,'{"none"}','{"Shower","TV","Internet","Free towels","Free breakfast","sauna","room service"}','yes'),
	(9413435,101,1,'no','street',50,'{"none"}','{"Shower","TV","Internet","Free towels","Free breakfast"}','yes'),
	(9413435,102,1,'yes','street',50,'{"none"}','{"Shower","TV","Internet","Free towels","Free breakfast"}','yes'),
	(9413435,201,2,'no','park',100,'{"none"}','{"Shower","TV","Internet","Free towels","Free breakfast"}','yes'),
	(9413435,202,2,'yes','street',150,'{"none"}','{"Shower","TV","Internet","Free towels","Free breakfast"}','yes'),
	(9413435,301,4,'no','street',200,'{"none"}','{"Shower","TV","Internet","Free towels","Free breakfast"}','yes'),
	(9413435,302,4,'yes','river',250,'{"none"}','{"Shower","TV","Internet","Free towels","Free breakfast"}','yes'),
	(9413435,400,7,'no','lake',300,'{"none"}','{"Shower","TV","Internet","Free towels","Free breakfast","sauna","room service"}','yes'),
	(9933506,101,1,'no','street',50,'{"none"}','{"Shower","TV","Internet","Free towels","Free breakfast"}','yes'),
	(9933506,102,1,'no','beach',50,'{"none"}','{"Shower","TV","Internet","Free towels","Free breakfast"}','yes'),
	(9933506,103,1,'yes','beach',50,'{"none"}','{"Shower","TV","Internet","Free towels","Free breakfast"}','yes'),
	(9933506,201,2,'no','street',100,'{"none"}','{"Shower","TV","Internet","Free towels","Free breakfast"}','yes'),
	(9933506,202,2,'yes','beach',150,'{"none"}','{"Shower","TV","Internet","Free towels","Free breakfast"}','yes'),
	(9933506,203,4,'yes','beach',250,'{"none"}','{"Shower","TV","Internet","Free towels","Free breakfast"}','yes'),
	(9933506,301,7,'no','street',300,'{"none"}','{"Shower","TV","Internet","Free towels","Free breakfast","sauna","room service"}','yes'),
	(9933506,302,7,'no','beach',300,'{"none"}','{"Shower","TV","Internet","Free towels","Free breakfast","sauna","room service"}','yes'),
	(9933506,303,7,'no','beach',300,'{"none"}','{"Shower","TV","Internet","Free towels","Free breakfast","sauna","room service"}','yes'),
	(2512675,101,1,'no','street',50,'{"none"}','{"Shower","TV","Internet","Free towels","Free breakfast"}','yes'),
	(2512675,102,1,'yes','street',50,'{"none"}','{"Shower","TV","Internet","Free towels","Free breakfast"}','yes'),
	(2512675,201,2,'no','street',100,'{"none"}','{"Shower","TV","Internet","Free towels","Free breakfast"}','yes'),
	(2512675,202,2,'yes','river',150,'{"none"}','{"Shower","TV","Internet","Free towels","Free breakfast"}','yes'),
	(2512675,301,4,'yes','river',250,'{"none"}','{"Shower","TV","Internet","Free towels","Free breakfast"}','yes'),
	(2512675,302,4,'no','street',200,'{"none"}','{"Shower","TV","Internet","Free towels","Free breakfast"}','yes'),
	(2512675,401,7,'no','street',300,'{"none"}','{"Shower","TV","Internet","Free towels","Free breakfast"}','yes'),
	(2512675,402,7,'no','river',300,'{"none"}','{"Shower","TV","Internet","Free towels","Free breakfast","sauna","room service"}','yes'),
	(1010187,101,1,'no','street',50,'{"none"}','{"Shower","TV","Internet","Free towels","Free breakfast"}','yes'),
	(1010187,102,1,'yes','street',50,'{"none"}','{"Shower","TV","Internet","Free towels","Free breakfast"}','yes'),
	(1010187,201,2,'no','street',100,'{"none"}','{"Shower","TV","Internet","Free towels","Free breakfast"}','yes'),
	(1010187,202,2,'yes','street',150,'{"none"}','{"Shower","TV","Internet","Free towels","Free breakfast"}','yes'),
	(1010187,301,4,'no','street',200,'{"none"}','{"Shower","TV","Internet","Free towels","Free breakfast"}','yes'),
	(1010187,302,4,'yes','street',250,'{"none"}','{"Shower","TV","Internet","Free towels","Free breakfast"}','yes'),
	(1010187,400,7,'no','street',300,'{"none"}','{"Shower","TV","Internet","Free towels","Free breakfast","sauna","room service"}','yes'),
	(8496001,101,1,'no','beach',50,'{"none"}','{"Shower","TV","Internet","Free towels","Free breakfast"}','yes'),
	(8496001,102,1,'yes','street',50,'{"none"}','{"Shower","TV","Internet","Free towels","Free breakfast"}','yes'),
	(8496001,201,2,'no','bach',100,'{"none"}','{"Shower","TV","Internet","Free towels","Free breakfast"}','yes'),
	(8496001,202,2,'yes','street',150,'{"none"}','{"Shower","TV","Internet","Free towels","Free breakfast"}','yes'),
	(8496001,301,4,'no','beach',200,'{"none"}','{"Shower","TV","Internet","Free towels","Free breakfast"}','yes'),
	(8496001,302,4,'yes','street',250,'{"none"}','{"Shower","TV","Internet","Free towels","Free breakfast"}','yes'),
	(8496001,401,7,'no','beach',300,'{"none"}','{"Shower","TV","Internet","Free towels","Free breakfast","sauna","room service"}','yes'),
	(8496001,402,7,'no','beach',300,'{"none"}','{"Shower","TV","Internet","Free towels","Free breakfast","sauna","room service"}','yes'),
	(3202411,101,1,'no','street',50,'{"none"}','{"Shower","TV","Internet","Free towels","Free breakfast"}','yes'),
	(3202411,102,1,'yes','street',50,'{"none"}','{"Shower","TV","Internet","Free towels","Free breakfast"}','yes'),
	(3202411,201,2,'no','street',100,'{"none"}','{"Shower","TV","Internet","Free towels","Free breakfast"}','yes'),
	(3202411,202,2,'yes','park',150,'{"none"}','{"Shower","TV","Internet","Free towels","Free breakfast"}','yes'),
	(3202411,301,4,'no','street',200,'{"none"}','{"Shower","TV","Internet","Free towels","Free breakfast"}','yes'),
	(3202411,302,4,'yes','outdoor pool',250,'{"none"}','{"Shower","TV","Internet","Free towels","Free breakfast"}','yes'),
	(3202411,400,7,'no','outdoor pool',300,'{"none"}','{"Shower","TV","Internet","Free towels","Free breakfast","sauna","room service"}','yes'),
	(9615817,101,1,'yes','street',50,'{"leaky faucet"}','{"Shower","TV","Internet","Free towels","Free breakfast"}','yes'),
	(9615817,102,2,'no','river',100,'{"none"}','{"Shower","TV","Internet","Free towels","Free breakfast"}','yes'),
	(9615817,201,2,'yes','river',150,'{"bedbugs"}','{"Shower","TV","Internet","Free towels","Free breakfast"}','yes'),
	(9615817,202,4,'yes','street',250,'{"none"}','{"Shower","TV","Internet","Free towels","Free breakfast"}','yes'),
	(9615817,300,7,'no','river',300,'{"none"}','{"Shower","TV","Internet","Free towels","Free breakfast","sauna","room service"}','yes'),
	(5894110,101,1,'yes','street',50,'{"leaky faucet"}','{"Shower","TV","Internet","Free towels","Free breakfast"}','yes'),
	(5894110,102,2,'yes','street',150,'{"leaky faucet"}','{"Shower","TV","Internet","Free towels","Free breakfast"}','yes'),
	(5894110,201,2,'no','street',100,'{"smelly bathroom"}','{"Shower","TV","Internet","Free towels","Free breakfast"}','yes'),
	(5894110,202,4,'yes','street',250,'{"leaky faucet"}','{"Shower","TV","Internet","Free towels","Free breakfast"}','yes'),
	(5894110,300,7,'no','street',300,'{"none"}','{"Shower","TV","Internet","Free towels","Free breakfast"}','yes'),

	(3371676,101,1,'no','river',50,'{"none"}','{"Shower","TV","Internet","Free towels","Free pancakes"}','yes'),
	(3371676,102,1,'yes','street',50,'{"none"}','{"Shower","TV","Internet","Free towels","Free pancakes"}','yes'),
	(3371676,201,2,'no','park',100,'{"none"}','{"Shower","TV","Internet","Free towels","Free pancakes"}','yes'),
	(3371676,202,2,'yes','lake',150,'{"none"}','{"Shower","TV","Internet","Free towels","Free pancakes"}','yes'),
	(3371676,301,4,'no','street',200,'{"none"}','{"Shower","TV","Internet","Free towels","Free pancakes"}','yes'),
	(3371676,302,4,'yes','street',250,'{"none"}','{"Shower","TV","Internet","Free towels","Free pancakes"}','yes'),
	(3371676,400,7,'no','park',300,'{"none"}','{"Shower","TV","Internet","Free towels","Free pancakes","sauna","room service"}','yes'),
	(8926680,101,1,'yes','river',50,'{"none"}','{"Shower","TV","Internet","Free towels","Free pancakes"}','yes'),
	(8926680,101,1,'yes','river',50,'{"none"}','{"Shower","TV","Internet","Free towels","Free pancakes"}','yes'),
	(8926680,201,2,'yes','street',100,'{"none"}','{"Shower","TV","Internet","Free towels","Free pancakes"}','yes'),
	(8926680,202,2,'yes','river',100,'{"none"}','{"Shower","TV","Internet","Free towels","Free pancakes"}','yes'),
	(8926680,301,4,'yes','park',250,'{"none"}','{"Shower","TV","Internet","Free towels","Free pancakes"}','yes'),
	(8926680,302,4,'yes','street',250,'{"none"}','{"Shower","TV","Internet","Free towels","Free pancakes"}','yes'),
	(8926680,401,7,'no','river',300,'{"none"}','{"Shower","TV","Internet","Free towels","Free pancakes","sauna","room service"}','yes'),
	(8926680,402,7,'no','street',300,'{"none"}','{"Shower","TV","Internet","Free towels","Free pancakes","sauna","room service"}','yes'),
	(8926680,501,7,'no','river',300,'{"none"}','{"Shower","TV","Internet","Free towels","Free pancakes","sauna","room service"}','yes'),
	(8926680,502,7,'no','river',300,'{"none"}','{"Shower","TV","Internet","Free towels","Free pancakes","sauna","room service"}','yes'),
	(9581598,101,1,'no','street',50,'{"none"}','{"Shower","TV","Internet","Free towels","Free pancakes"}','yes'),
	(9581598,102,2,'yes','street',150,'{"none"}','{"Shower","TV","Internet","Free towels","Free pancakes"}','yes'),
	(9581598,201,2,'no','sea',100,'{"none"}','{"Shower","TV","Internet","Free towels","Free pancakes"}','yes'),
	(9581598,202,4,'yes','sea',250,'{"none"}','{"Shower","TV","Internet","Free towels","Free pancakes"}','yes'),
	(9581598,300,7,'no','sea',300,'{"none"}','{"Shower","TV","Internet","Free towels","Free pancakes","sauna","room service"}','yes'),
	(6244341,101,1,'no','street',50,'{"leaky shower"}','{"Shower","TV","Internet","Free towels","Free pancakes"}','yes'),
	(6244341,102,2,'yes','street',100,'{"leaky faucet"}','{"Shower","TV","Internet","Free towels","Free pancakes"}','yes'),
	(6244341,201,2,'no','street',100,'{"leaky shower"}','{"Shower","TV","Internet","Free towels","Free pancakes"}','yes'),
	(6244341,202,2,'yes','street',150,'{"leaky faucet"}','{"Shower","TV","Internet","Free towels","Free pancakes"}','yes'),
	(6244341,301,4,'no','street',200,'{"stained carpet"}','{"Shower","TV","Internet","Free towels","Free pancakes"}','yes'),
	(6244341,302,4,'yes','street',250,'{"stained carpet"}','{"Shower","TV","Internet","Free towels","Free pancakes"}','yes'),
	(6244341,400,7,'no','street',300,'{"none"}','{"Shower","TV","Internet","Free towels","Free pancakes","sauna","room service"}','yes'),
	(3170033,101,1,'no','street',50,'{"none"}','{"Shower","TV","Internet","Free towels","Free pancakes"}','yes'),
	(3170033,102,2,'yes','mountain',100,'{"none"}','{"Shower","TV","Internet","Free towels","Free pancakes"}','yes'),
	(3170033,201,2,'yes','mountain',150,'{"none"}','{"Shower","TV","Internet","Free towels","Free pancakes"}','yes'),
	(3170033,202,2,'no','street',100,'{"none"}','{"Shower","TV","Internet","Free towels","Free pancakes"}','yes'),
	(3170033,301,4,'no','mountain',200,'{"none"}','{"Shower","TV","Internet","Free towels","Free pancakes"}','yes'),
	(3170033,302,4,'yes','street',250,'{"none"}','{"Shower","TV","Internet","Free towels","Free pancakes"}','yes'),
	(3170033,400,7,'no','mountain',300,'{"none"}','{"Shower","TV","Internet","Free towels","Free pancakes","sauna","room service"}','yes'),
	(4270962,101,1,'no','street',50,'{"none"}','{"Shower","TV","Internet","Free towels","Free pancakes"}','yes'),
	(4270962,102,2,'yes','mountain',100,'{"none"}','{"Shower","TV","Internet","Free towels","Free pancakes"}','yes'),
	(4270962,201,2,'no','street',100,'{"none"}','{"Shower","TV","Internet","Free towels","Free pancakes"}','yes'),
	(4270962,202,4,'yes','mountain',250,'{"none"}','{"Shower","TV","Internet","Free towels","Free pancakes"}','yes'),
	(4270962,301,4,'yes','street',250,'{"none"}','{"Shower","TV","Internet","Free towels","Free pancakes"}','yes'),
	(4270962,302,7,'no','mountain',300,'{"none"}','{"Shower","TV","Internet","Free towels","Free pancakes","sauna","room service"}','yes'),
	(4270962,401,7,'no','street',300,'{"none"}','{"Shower","TV","Internet","Free towels","Free pancakes","sauna","room service"}','yes'),
	(4270962,402,7,'no','mountain',300,'{"none"}','{"Shower","TV","Internet","Free towels","Free pancakes","sauna","room service"}','yes'),
	(3723682,101,1,'no','street',50,'{"none"}','{"Shower","TV","Internet","Free towels","Free pancakes"}','yes'),
	(3723682,102,2,'yes','mountain',150,'{"none"}','{"Shower","TV","Internet","Free towels","Free pancakes"}','yes'),
	(3723682,201,2,'no','street',100,'{"none"}','{"Shower","TV","Internet","Free towels","Free pancakes"}','yes'),
	(3723682,202,4,'yes','mountain',250,'{"none"}','{"Shower","TV","Internet","Free towels","Free pancakes"}','yes'),
	(3723682,300,7,'no','mountain',300,'{"none"}','{"Shower","TV","Internet","Free towels","Free pancakes","sauna","room service"}','yes'),
	(2412724,101,1,'no','forest',50,'{"none"}','{"Shower","TV","Internet","Free towels","Free pancakes"}','yes'),
	(2412724,102,2,'no','mountain',100,'{"none"}','{"Shower","TV","Internet","Free towels","Free pancakes"}','yes'),
	(2412724,201,2,'no','forest',100,'{"none"}','{"Shower","TV","Internet","Free towels","Free pancakes"}','yes'),
	(2412724,202,4,'no','mountain',200,'{"none"}','{"Shower","TV","Internet","Free towels","Free pancakes"}','yes'),
	(2412724,300,7,'no','forest',300,'{"none"}','{"Shower","TV","Internet","Free towels","Free pancakes","sauna","room service"}','yes')])

conn.commit()

cur.close()
conn.close()