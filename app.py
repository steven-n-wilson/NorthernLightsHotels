import os
import psycopg2
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

developer = os.getenv("DEVELOPER", "Northern Lights Dev Team")
environment = os.getenv("ENVIRONMENT", "development")

def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="flask_db",
        user="postgres",
        password="1123",
        port=5432
        )

    return conn

@app.route("/")
def index():

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute('SELECT * FROM hotel_chain;')
    hotel_chain = cur.fetchall()

    cur.close()
    conn.close()

    return render_template("index.html", hotel_chain = hotel_chain)

@app.route("/admin", methods=['GET', 'POST'])
def admin():

    if request.method == 'POST' and 'form1' in request.form:

        # Get data from the form
        hotel_id = request.form['hotel_id']
        room_number = request.form['room_number']
        capacity = request.form['capacity']
        isExtendable = request.form['isextendable']
        isAvailable = request.form['isAvailable']
        outdoor_view = "'" + request.form['outdoor_view'] + "'"
        price = request.form['price']

        problems = request.form['problems']
        problems_list = ['"%s"' % problem.strip() for problem in problems.split(",")]
        problems_string = "'{" + ', '.join(problems_list) + "}'"

        amenities = request.form['amenities']
        amenities_list = ['"%s"' % amenity.strip() for amenity in amenities.split(",")]
        amenities_string = "'{" + ', '.join(amenities_list) + "}'"

        # SQL query to insert data to flask_db
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(f"INSERT INTO room (hotel_id, room_number, capacity, isExtendable, outdoor_view, price, problems, amenities, isAvailable) VALUES ({hotel_id}, {room_number}, {capacity}, {isExtendable}, {outdoor_view}, {price}, {problems_string}, {amenities_string},{isAvailable})")

        conn.commit()
        cur.close()
        conn.close()

        return redirect('/admin')
        
    elif request.method == 'POST' and 'form2' in request.form:

        # Get data from the form
        room_id = request.form['room_id']
        new_hotel_id = request.form['new_hotel_id']
        new_room_number = request.form['new_room_number']
        new_capacity = request.form['new_capacity']
        new_isExtendable = request.form['new_isextendable']
        new_outdoor_view = "'" + request.form['new_outdoor_view'] + "'"
        new_price = request.form['new_price']

        new_problems = request.form['new_problems']
        new_problems_list = ['"%s"' % problem.strip() for problem in new_problems.split(",")]
        new_problems_string = "'{" + ', '.join(new_problems_list) + "}'"

        new_amenities = request.form['new_amenities']
        new_amenities_list = ['"%s"' % amenity.strip() for amenity in new_amenities.split(",")]
        new_amenities_string = "'{" + ', '.join(new_amenities_list) + "}'"

        new_isAvailable= request.form['new_isAvailable']

        # SQL query to update data from flask_db
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(f"UPDATE room SET hotel_id={new_hotel_id}, room_number={new_room_number}, \
        capacity={new_capacity},isExtendable={new_isExtendable}, price={new_price}, outdoor_view={new_outdoor_view}, \
        problems={new_problems_string}, amenities={new_amenities_string}, isAvailable={new_isAvailable}  WHERE room_id={room_id}")
        
        conn.commit()
        cur.close()
        conn.close()

        return redirect('/admin')

    elif request.method == 'POST' and 'form3' in request.form:
        room_id = request.form['room_id']

        # SQL query to delete data from flask_db
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(f"DELETE FROM room WHERE room_id={room_id}")
        
        conn.commit()
        cur.close()
        conn.close()

        return redirect('/admin')
    
    elif request.method == 'POST' and 'form4' in request.form:

        # Get data from the form
        hotel_id = request.form['hotel_id']
        owner_name = "'" + request.form['owner_name'] + "'"
        star_rating = request.form['star_rating']
        number_of_rooms = request.form['number_of_rooms']
        phone_number = "'" + request.form['phone_number'] + "'"
        email_address = "'" + request.form['email_address'] + "'"

        # SQL query to insert data to flask_db
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(f"INSERT INTO hotel (hotel_id, owner_name, star_rating, number_of_rooms, phone_number, email_address) VALUES ({hotel_id}, {owner_name}, {star_rating}, {number_of_rooms}, {phone_number}, {email_address})")

        conn.commit()
        cur.close()
        conn.close()

        return redirect('/admin')
        
    elif request.method == 'POST' and 'form5' in request.form:

        # Get data from the form
        hotel_id = request.form['hotel_id']
        new_owner_name = "'" + request.form['new_owner_name'] + "'"
        new_star_rating = request.form['new_star_rating']
        new_number_of_rooms = request.form['new_number_of_rooms']
        new_phone_number = "'" + request.form['new_phone_number'] + "'"
        new_email_address = "'" + request.form['new_email_address'] + "'"

        # SQL query to update data from flask_db
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(f"UPDATE hotel SET owner_name={new_owner_name}, \
        star_rating={new_star_rating},number_of_rooms={new_number_of_rooms}, phone_number={new_phone_number}, \
        email_address={new_email_address} WHERE hotel_id={hotel_id}")
        
        conn.commit()
        cur.close()
        conn.close()

        return redirect('/admin')

    elif request.method == 'POST' and 'form6' in request.form:
        hotel_id = request.form['hotel_id']

        # SQL query to delete data from flask_db
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(f"DELETE FROM hotel WHERE hotel_id={hotel_id}")
        
        conn.commit()
        cur.close()
        conn.close()

        return redirect('/admin')

    elif request.method == 'POST' and 'form7' in request.form:

        # Get data from the form
        first_name = "'" + request.form['first_name'] + "'"
        last_name = "'" + request.form['last_name'] + "'"
        emp_role = "'" + request.form['emp_role'] + "'"
        hotel_id = request.form['hotel_id']
        street = "'" + request.form['street'] + "'"
        city = "'" + request.form['city'] + "'"
        state_or_province = "'" + request.form['state_or_province'] + "'" 
        postal_code = "'" + request.form['postal_code'] + "'" 

        # SQL query to insert data to flask_db
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(f"INSERT INTO employee (first_name,last_name, emp_role, hotel_id,street,city, state_or_province,postal_code) VALUES ({first_name},{last_name}, {emp_role}, {hotel_id},{street},{city}, {state_or_province},{postal_code})")

        conn.commit()
        cur.close()
        conn.close()

        return redirect('/admin')
        
    elif request.method == 'POST' and 'form8' in request.form:

        # Get data from the form
        emp_id = request.form['emp_id']
        new_first_name = "'" + request.form['new_first_name'] + "'"
        new_last_name = "'" + request.form['new_last_name'] + "'"
        new_emp_role = "'" + request.form['new_emp_role'] + "'"
        new_hotel_id = request.form['new_hotel_id']
        new_street = "'" + request.form['new_street'] + "'"
        new_city = "'" + request.form['new_city'] + "'"
        new_state_or_province = "'" + request.form['new_state_or_province'] + "'" 
        new_postal_code = "'" + request.form['new_postal_code'] + "'" 

        # SQL query to update data from flask_db
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(f"UPDATE employee SET first_name={new_first_name}, \
        last_name={new_last_name},emp_role={new_emp_role}, street={new_street}, \
        city={new_city},state_or_province={new_state_or_province},postal_code={new_postal_code} WHERE emp_id={emp_id}")
        
        conn.commit()
        cur.close()
        conn.close()

        return redirect('/admin')

    elif request.method == 'POST' and 'form9' in request.form:
        emp_id = request.form['emp_id']

        # SQL query to delete data from flask_db
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(f"DELETE FROM employee WHERE emp_id={emp_id}")
        
        conn.commit()
        cur.close()
        conn.close()

        return redirect('/admin')
    
    elif request.method == 'POST' and 'form10' in request.form:

        # Get data from the form
        customer_id = request.form['customer_id']
        first_name = "'" + request.form['first_name'] + "'"
        last_name = "'" + request.form['last_name'] + "'"
        date_of_registration = "'" + request.form['date_of_registration'] + "'"

        customer_address = request.form['customer_address']
        customer_address_list = ['"%s"' % address.strip() for address in customer_address.split(",")]
        customer_address_string = "'{" + ', '.join(customer_address_list) + "}'"

        # SQL query to insert data to flask_db
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(f"INSERT INTO customer (customer_id,first_name,last_name,customer_address,date_of_registration) VALUES ({customer_id},{first_name},{last_name},{customer_address_string},{date_of_registration})")

        conn.commit()
        cur.close()
        conn.close()

        return redirect('/admin')
        
    elif request.method == 'POST' and 'form11' in request.form:

        # Get data from the form
        customer_id = request.form['customer_id']
        first_name = "'" + request.form['new_first_name'] + "'"
        last_name = "'" + request.form['new_last_name'] + "'"
        date_of_registration = "'" + request.form['new_date_of_registration'] + "'"

        customer_address = request.form['new_customer_address']
        customer_address_list = ['"%s"' % address.strip() for address in customer_address.split(",")]
        customer_address_string = "'{" + ', '.join(customer_address_list) + "}'"

        # SQL query to update data from flask_db
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(f"UPDATE customer SET first_name={first_name}, \
        last_name={last_name},date_of_registration={date_of_registration}, customer_address={customer_address_string} \
        WHERE customer_id={customer_id}")
        
        conn.commit()
        cur.close()
        conn.close()

        return redirect('/admin')

    elif request.method == 'POST' and 'form12' in request.form:
        customer_id = request.form['customer_id']

        # SQL query to delete data from flask_db
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(f"DELETE FROM customer WHERE customer_id={customer_id}")
        
        conn.commit()
        cur.close()
        conn.close()

        return redirect('/admin')

    return render_template("admin.html")

@app.route("/search")
def search():

    # Get the search information from the form
    checkin_date = request.args.get('checkin_date')
    checkout_date = request.args.get('checkout_date')
    guest_capacity = request.args.get('guest_capacity')
    area = request.args.get('area')
    price = request.args.get('price')
    reservation_type = request.args.get('reservation_type')
    hotel_chain = "'" + request.args.get('hotel_chain')+ "'"
    category = request.args.get('category')
    hotel_capacity = request.args.get('hotel_capacity')
    
    # SQL query to retrieve data from flask_db

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(f""" 
        SELECT h.hotel_id, h.owner_name, h.star_rating, h.number_of_rooms, r.room_number, r.price, r.capacity
        FROM hotel h
        JOIN room r ON h.hotel_id = r.hotel_id
        WHERE h.owner_name = {hotel_chain} AND h.star_rating <= {category} AND h.number_of_rooms >= {hotel_capacity} 
        AND r.price <= {price} AND r.capacity >= {guest_capacity}
    """)

    # cur.execute(f"SELECT * FROM room WHERE price <= {price} AND capacity = {guest_capacity}")

    # Fetch the results and return them as a list of dictionaries
    results = []
    for row in cur.fetchall():
        results.append({
            'room_number': row[2],
            'room_capacity' : row[3],
            'outdoor_view' : row[5],
            'price' : row[6]
        })

    cur.close()
    conn.close()
    
    return render_template("search_results.html", results=results)

@app.route("/employee_admin", methods=['GET', 'POST'])
def employee_admin():

    if request.method == 'POST' and 'form1' in request.form:

        # Get data from the form
        card_name = request.form['card_name']
        card_number = "'" + request.form['card_number']+ "'"
        expiry = request.form['expiry']
        password = request.form['password']
        amount = request.form['amount']

        # SQL query to insert data to flask_db
        conn = get_db_connection()
        cur = conn.cursor()
        # cur.execute(f"INSERT INTO payment (card_name, card_number, expiry, password, amount) VALUES ({card_name}, {card_number}, {expiry}, {password}, {amount})")

        conn.commit()
        cur.close()
        conn.close()

        return redirect('/employee_admin')
        
    elif request.method == 'POST' and 'form2' in request.form:

        # Get data from the form
        booking_id = request.form['booking_id']
        room_id = request.form['room_id']
        rent_date = "'" +request.form['rent_date']+ "'"
        customer_ID = request.form['customer_ID']

        # SQL query to insert data to flask_db
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(f"INSERT INTO rent (booking_id, room_id, rent_date, customer_ID) VALUES ({booking_id}, {room_id}, {rent_date}, {customer_ID})")

        conn.commit()
        cur.close()
        conn.close()

        return redirect('/employee_admin')

    return render_template("employee_admin.html")

if __name__ == "__main__":

    debug = False

    if environment == "development" or environment == "local":
        debug = True

    app.run(host="127.0.0.1", port=3000, debug=debug)