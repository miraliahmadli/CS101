def init_database(hotel_name):
    # Copy your code from (Task 3.1)
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
    
def add_review(database, hotel_name, review):
    # Implement your code here
    score = {'very bad': 1.0, 
            'bad': 2.0, 
            'soso': 3.0, 
            'good': 4.0, 
            'very good': 5.0}

    if review not in score.keys():
        return database

    hotel_exists = False
    for hotel_review in database:
        if hotel_review['hotel_name'] == hotel_name:
            hotel_exists = True
            hotel_review['reviews'][review] += 1
            hotel_review['number_of_reviews'] += 1
            if hotel_review['number_of_reviews'] == 1:
                hotel_review['average_rating'] = score[review]
            else:
                avg = hotel_review['average_rating']
                avg *= (hotel_review['number_of_reviews'] - 1)
                avg += score[review]
                avg /= hotel_review['number_of_reviews']
                hotel_review['average_rating'] = avg
            break
    
    if not hotel_exists:
        hotel_review = {
            'hotel_name': hotel_name,
            'reviews':  
                {'very bad': 0, 
                'bad': 0, 
                'soso': 0, 
                'good': 0, 
                'very good': 0},
            'average_rating': score[review],
            'number_of_reviews': 1,
            }
        hotel_review['reviews'][review] += 1
        database.append(hotel_review)
    return database

    

def main():
    hotel_name = ['Apple Hotel']
    
    hotel_review_database = init_database(hotel_name)
    print("Initialized hotel review database:\n", hotel_review_database)
    
    hotel_review_database = add_review(hotel_review_database, 'Apple Hotel', 'good')
    print("Updated hotel review database:\n", hotel_review_database)
    
    hotel_review_database = add_review(hotel_review_database, 'Apple Hotel', 'very bad')
    print("Updated hotel review database:\n", hotel_review_database)
    
    hotel_review_database = add_review(hotel_review_database, 'Apple Hotel', 'great')
    print("Updated hotel review database:\n", hotel_review_database)
    
    hotel_review_database = add_review(hotel_review_database, 'Banana Hotel', 'soso')
    print("Updated hotel review database:\n", hotel_review_database)

if __name__ == "__main__":
    main()
