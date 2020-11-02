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
    
def extract_hotels(database, conditions):
    # Implement your code here
    extracted = []
    for hotel_review in database:
        if hotel_review['average_rating'] >= conditions['average_rating'] and\
            hotel_review['number_of_reviews'] >= conditions['number_of_reviews']:
            extracted.append(hotel_review['hotel_name'])
    return extracted
    

def main():
    hotel_name = ['Apple Hotel', 'Banana Hotel', 'Cherry Hotel', 'Date Hotel']
    hotel_review_database = init_database(hotel_name)
    
    apple_reviews = ['very bad'] * 0 + ['bad'] * 1 + ['soso'] * 3 + ['good'] * 5 + ['very good'] * 3
    for review in apple_reviews:
        hotel_review_database = add_review(hotel_review_database, 'Apple Hotel', review)
        
    
    banana_reviews = ['very bad'] * 3 + ['bad'] * 3 + ['soso'] * 1 + ['good'] * 1 + ['very good'] * 0
    for review in banana_reviews:
        hotel_review_database = add_review(hotel_review_database, 'Banana Hotel', review)
    
    cherry_reviews = ['very bad'] * 0 + ['bad'] * 0 + ['soso'] * 1 + ['good'] * 1 + ['very good'] * 2
    for review in cherry_reviews:
        hotel_review_database = add_review(hotel_review_database, 'Cherry Hotel', review)
        
    date_reviews = ['very bad'] * 0 + ['bad'] * 1 + ['soso'] * 1 + ['good'] * 2 + ['very good'] * 2
    for review in date_reviews:
        hotel_review_database = add_review(hotel_review_database, 'Date Hotel', review)
    
    conditions = {'average_rating': 3.5, 'number_of_reviews': 5}
    answer = extract_hotels(hotel_review_database, conditions)
    print(answer)
    
    
if __name__ == "__main__":
    main()
