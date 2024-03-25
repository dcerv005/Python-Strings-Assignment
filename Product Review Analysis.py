#Question 1 
keywords = ["good", "excellent", "bad", "poor", "average"]
reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]
#Task 1
counter = 0
new_list=[]
for review in reviews:    
    a = review.lower().find(keywords[counter])
    new_review = review.replace(review[a:(a+len(keywords[counter]))], keywords[counter].upper())
    new_list.append(new_review)
    counter +=1    
print(new_list)

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "average", "horrible", "awful", "disappointing", "subpar"]
#Task 2
def tally_count():
    for review in reviews:
        for i in range(len(positive_words)):
            
            if positive_words[i] in review:
                positive_count=review.lower().count(positive_words[i].lower())
                print(f"In the review, '{review}': There is/are {positive_count} positive word(s)")
            elif negative_words[i] in review.lower():
                negative_count=review.lower().count(negative_words[i])
                print(f"In the review, '{review}': There is/are {negative_count} negative word(s)")

tally_count()
#Task 3
def summary():
    for review in reviews:
        a =review.find(" ", 30)
        print(review[0:a] + "...")

summary()

