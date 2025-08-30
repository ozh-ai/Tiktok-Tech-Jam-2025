import random
import time
import pandas as pd

# --- Configuration ---
num_rows_per_category = 20000
categories = ["advertisement", "irrelevant", "non_visitor"]
total_rows = num_rows_per_category * len(categories)
output_filename = "data/60000_reviews.csv"

# Common lists
first_names = ["Alex", "Jordan", "Casey", "Morgan", "Riley", "Avery", "Jamie", "Quinn", "Taylor", "Peyton"]
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]
business_names = [f"Business{i}" for i in range(1, 101)]  # 100 sample businesses
rating_categories = ["taste", "menu", "outdoor_atmosphere", "indoor_atmosphere"]

# Sentence templates
weather_options = ["sunny", "rainy", "cloudy", "windy", "stormy"]
hobby_options = ["painting", "cycling", "coding", "yoga", "photography"]
book_topics = ["history", "science fiction", "biography", "self-help", "fantasy"]
menu_items = ["pizza", "burger", "coffee", "sushi", "steak"]
opinions = ["amazing", "terrible", "overrated", "popular", "hidden gem"]

# --- Helper Functions ---
def generate_multisentence_ad(index):
    sentences = [
        f"SPECIAL OFFER! Enjoy {random.randint(10,50)}% OFF on {random.choice(menu_items)} at {random.choice(business_names)}!",
        f"Visit www.deals{random.randint(1,100)}.com for more details.",
        f"Our signature {random.choice(menu_items)} is a must-try this week.",
        f"Book now at book{random.randint(1,100)}.com to reserve your table.",
        f"Limited time offer for {random.choice(['date night', 'family dinner', 'birthday party'])}!"
    ]
    random.shuffle(sentences)
    return " ".join(sentences[:random.randint(2,4)])

def generate_multisentence_irrelevant():
    sentences = [
        f"The sky is {random.choice(weather_options)} today and it made me think about {random.choice(book_topics)}.",
        f"I spent the afternoon {random.choice(hobby_options)}, which was more interesting than reviewing restaurants.",
        f"My favorite food is {random.choice(menu_items)}, but I haven't tried {random.choice(business_names)}.",
        f"I also read about {random.choice(book_topics)}, totally unrelated to this place."
    ]
    random.shuffle(sentences)
    return " ".join(sentences[:random.randint(2,4)])

def generate_multisentence_non_visitor():
    sentences = [
        f"I haven't visited {random.choice(business_names)}, but heard it is {random.choice(opinions)}.",
        f"My friend told me the experience was {random.choice(opinions)}.",
        f"From what I saw online, it looks {random.choice(opinions)}.",
        f"I would need to go there personally to leave a proper review."
    ]
    random.shuffle(sentences)
    return " ".join(sentences[:random.randint(2,4)])

def generate_review(category, index):
    review = {}

    review["business_name"] = random.choice(business_names)
    review["author_name"] = f"{random.choice(first_names)} {random.choice(last_names)}"
    review["rating_category"] = random.choice(rating_categories)
    
    # Photo path based on rating_category and business_name
    business_slug = review["business_name"].lower().replace(" ", "_")
    review["photo"] = f"dataset/{review['rating_category']}/{business_slug}_{review['author_name'].lower().replace(' ','_')}.png"

    # Text and rating
    review["label"] = category
    if category == "advertisement":
        review["text"] = generate_multisentence_ad(index)
        review["rating"] = random.choices([1,5], weights=[0.2,0.8])[0]
    elif category == "irrelevant":
        review["text"] = generate_multisentence_irrelevant()
        review["rating"] = random.randint(2,5)
    else:  # non_visitor
        review["text"] = generate_multisentence_non_visitor()
        review["rating"] = random.randint(1,3)

    return review

# --- Main Generation ---
all_reviews = []
for category in categories:
    for i in range(num_rows_per_category):
        all_reviews.append(generate_review(category, i))
    print(f"Generated {num_rows_per_category} reviews for {category}")

# Shuffle reviews
random.shuffle(all_reviews)

# Convert to DataFrame with desired column order
df = pd.DataFrame(all_reviews, columns=[
    "business_name", "author_name", "text", "photo", "rating", "rating_category", "label"
])
df.to_csv(output_filename, index=False)
print(f"CSV file '{output_filename}' created successfully!")
