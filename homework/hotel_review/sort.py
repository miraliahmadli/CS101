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
    
def sort_hotels(database, criteria, reverse):
    # Implement your code here
    def comp(review1, review2):
        for crit in criteria:
            if crit == 'reviews':
                if not reverse:
                    if review1[crit]['very bad'] == review2[crit]['very bad']:
                        if review1[crit]['bad'] == review2[crit]['bad']:
                            if review1[crit]['soso'] == review2[crit]['soso']:
                                if review1[crit]['good'] == review2[crit]['good']:
                                    if review1[crit]['very good'] == review2[crit]['very good']:
                                        continue
                                    else:
                                        return review1[crit]['very good'] < review2[crit]['very good']
                                else:
                                    return review1[crit]['good'] < review2[crit]['good']
                            else:
                                return review1[crit]['soso'] > review2[crit]['soso']
                        else:
                            return review1[crit]['bad'] > review2[crit]['bad']
                    else:
                        return review1[crit]['very bad'] > review2[crit]['very bad']
                else:
                    if review1[crit]['very good'] == review2[crit]['very good']:
                        if review1[crit]['good'] == review2[crit]['good']:
                            if review1[crit]['soso'] == review2[crit]['soso']:
                                if review1[crit]['bad'] == review2[crit]['bad']:
                                    if review1[crit]['very bad'] == review2[crit]['very bad']:
                                        continue
                                    else:
                                        return review1[crit]['very bad'] < review2[crit]['very bad']
                                else:
                                    return review1[crit]['bad'] < review2[crit]['bad']
                            else:
                                return review1[crit]['soso'] > review2[crit]['soso']
                        else:
                            return review1[crit]['good'] > review2[crit]['good']
                    else:
                        return review1[crit]['very good'] > review2[crit]['very good']
            elif crit == 'hotel_name':
                if reverse:
                    return review1[crit] > review2[crit]
                return review1[crit] < review2[crit]
            else:
                if review1[crit] == review2[crit]:
                    continue
                else:
                    if reverse:
                        return review1[crit] > review2[crit]
                    return review1[crit] < review2[crit]
        return True
    
    new_db = database[:]
    # for hotel in new_db:
    #     print(hotel)
    for i in range(len(new_db) - 1):
        for j in range(len(new_db) - i - 1):
            rev1, rev2 = new_db[j], new_db[j + 1]
            # print(f"comparing {rev1['hotel_name']} {rev2['hotel_name']}")
            # print("RESULT: ", comp(rev1, rev2))
            if not comp(rev1, rev2):
                new_db[j], new_db[j + 1] = new_db[j + 1], new_db[j]
    
    sorted_list = []
    for hotel_review in new_db:
        sorted_list.append(hotel_review['hotel_name'])
    return sorted_list


def main():
    # Creating the example hotel list
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
    
    # Test your implementations
    # criteria = ['reviews']
    # criteria = ['hotel_name']
    # criteria = ['average_rating', 'number_of_reviews']
    criteria = ['number_of_reviews', 'average_rating']
    
    sorted_list = sort_hotels(hotel_review_database, criteria, True)
    print(sorted_list)

if __name__ == "__main__":
    main()
