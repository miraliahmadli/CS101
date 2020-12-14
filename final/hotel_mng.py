class Hotel:
    def init(self, hotel_name):
        # TASK 1, 5pt
        ###### Start of your code ######
        self.hotel_name = hotel_name
        self.reviews = {'very bad': 0, 
                        'bad': 0, 
                        'soso': 0, 
                        'good': 0, 
                        'very good': 0}
        self.average_rating = None
        self.number_of_reviews = 0
        self.score = {'very bad': 1.0, 
                        'bad': 2.0, 
                        'soso': 3.0, 
                        'good': 4.0, 
                        'very good': 5.0}
        ####### End of your code #######
        pass
    def add_review(self, review):
        # TASK 2, 5pt
        ###### Start of your code ######
        if review not in self.reviews.keys():
            return
        self.reviews[review] += 1
        self.number_of_reviews += 1
        if self.number_of_reviews == 1:
            self.average_rating = self.score[review]
        else:
            avg = self.average_rating
            avg *= (self.number_of_reviews - 1)
            avg += self.score[review]
            avg /= self.number_of_reviews
            self.average_rating = avg
        ####### End of your code #######
        pass
    
    def delete_review(self, review):
        # TASK 3, 10pt
        ###### Start of your code ######
        if review not in self.reviews.keys() or self.reviews[review] == 0:
            return
        self.reviews[review] -= 1
        self.number_of_reviews -= 1
        if self.number_of_reviews == 0:
            self.average_rating = None
        else:
            avg = self.average_rating
            avg *= (self.number_of_reviews + 1)
            avg -= self.score[review]
            avg /= self.number_of_reviews
            self.average_rating = avg
        ####### End of your code #######
        pass

    
def main():

    print('###########TASK1 EXAMPLE############')
    hotel_name = 'Apple Hotel'
    hotel = Hotel()
    hotel.init(hotel_name)
    print("hotel_name:\n", hotel.hotel_name)
    print("reviews:\n", hotel.reviews)
    print("average_rating:\n", hotel.average_rating)
    print("number_of_reviews:\n", hotel.number_of_reviews)
    print('\n\n')
    
    print('###########TASK2 EXAMPLE############')
    hotel.add_review('good')
    print("reviews:\n", hotel.reviews)
    print("Number of reviews:\n", hotel.number_of_reviews)
    print("Average rating:\n", hotel.average_rating)
    print('\n')
    hotel.add_review('soso')
    print("reviews:\n", hotel.reviews)
    print("Number of reviews:\n", hotel.number_of_reviews)
    print("Average rating:\n", hotel.average_rating)
    print('\n\n')
    
    print('###########TASK3 EXAMPLE############')
    hotel.delete_review('good')
    print("reviews:\n", hotel.reviews)
    print("Number of reviews:\n", hotel.number_of_reviews)
    print("Average rating:\n", hotel.average_rating)
    
if __name__ == "__main__":
    main()
