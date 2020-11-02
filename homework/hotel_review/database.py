def init_database(hotel_name):
    # Implement your code here
    hotel_review_database = []
    hotels = []
    for hotel in hotel_name:
        if hotel in hotels:
            continue
        hotel_review = {
            'hotel_name': hotel,
            'reviews':  
                {'very bad': 0, 
                'bad': 0, 
                'soso': 0, 
                'good': 0, 
                'very good': 0},
            'average_rating': None,
            'number_of_reviews': 0,
        }
        hotel_review_database.append(hotel_review)
        hotels.append(hotel)
    
    return hotel_review_database
    

def main():
    hotel_name = ['Apple Hotel', 'Banana Hotel']
    
    hotel_review_database = init_database(hotel_name)
    
    print("Initialized hotel review database:\n", hotel_review_database)
    

if __name__ == "__main__":
    main()
