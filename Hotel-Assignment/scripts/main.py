from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

app = Flask(__name__)

@app.route("/")
def create_check_in():

    check_in_date = request.json['date']
    date = check_in(rent_date = check_in_date)
    db.session.add(date)
    db.session.commit()
    return

def create_check_out():

    check_out = request.json['date']
    date = check_in(check_out_date = check_out)
    db.session.add(date)
    db.session.commit()
    return

def check_reservation_type():
    #check if it is a booking or a rental
    reservation = request.json['reservation']
    reserve = check_in(reservation_type = reservation)
    db.session.add(reserve)
    db.session.commit()
    return

@app.route('/hotel')
def search():
    
        check_in_date = request.args.get['rent_date']
        check_out = request.args.get['check_out_date']
        room_capacity = request.args.get['capacity']
        area = request.args.get['country']
        room_price = request.args.get['price']
        hotel_chain_name = request.args.get['owner_name']
        rating = request.args.get['star_rating']
        num_of_rooms = request.args.get['number_of_rooms']

        query = hotel.query.join(hotel_addresses).join(room).join(check_in)

        if check_in_date:
            query = query.filter(check_in.rent_date == check_in_date)

        if check_out:
                query = query.filter(check_in.check_out_date == check_out)

        if room_capacity:
            query = query.filter(room.capacity == room_capacity)

        if room_price:
            query = query.filter(room.price == room_price)

        if area:
            query = query.filter(hotel_addresses == area)

        if hotel_chain_name:
            query = query.filter(hotel.owner_name == hotel_chain_name)

        if rating:
            query = query.filter(hotel.star_rating == rating)

        if num_of_rooms:
            query = query.filter(hotel.number_of_rooms == num_of_rooms)

        return render_template('FILENAME WITH DATABASE HERE', hotel=hotel)
   