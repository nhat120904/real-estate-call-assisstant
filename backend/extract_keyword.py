"""
At the command line, only need to run once to install the package via pip:
$ pip install google-generativeai
"""

import google.generativeai as palm

palm.configure(api_key="AIzaSyAhSJ1YVKEZMkwe5yEElP8US8l14EHHQJg")

defaults = {
  'model': 'models/text-bison-001',
  'temperature': 0.2,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
  'max_output_tokens': 1024,
  'stop_sequences': [],
  'safety_settings': [{"category":"HARM_CATEGORY_DEROGATORY","threshold":1},{"category":"HARM_CATEGORY_TOXICITY","threshold":1},{"category":"HARM_CATEGORY_VIOLENCE","threshold":2},{"category":"HARM_CATEGORY_SEXUAL","threshold":2},{"category":"HARM_CATEGORY_MEDICAL","threshold":2},{"category":"HARM_CATEGORY_DANGEROUS","threshold":2}],
}
input = '2 bedroom apartment in central Ho Chi Minh City with a budget of 2 billion and 300 million VND'
def extract_keyword(input):
  prompt = f"""input: I'm interested in purchasing a 3-storey house with basic furniture in a particular district of Ho Chi Minh City, preferably District 1. My budget is open to negotiation but ideally between 4 billion and 6 billion VND. I'm looking for a house with an area of around 50 square meters, with a tolerance of about 5 square meters. I have a preference for houses that face the south or west direction. Could you provide me with some options that meet these criteria?
  output: address: ["District 1", "Ho Chi Minh"] 
  price: [4000000000, 6000000000] 
  property_type: ["house"]
  area: [~50] 
  bedrooms: null
  bathrooms: null
  house_direction: ["south", "west"]
  description: null
  floors: [3]
  installment_payment: null
  furniture: ["furnished"]
  balcony_direction: null
  input: Looking for apartment, Hanoi, flexible budget, around 80m², ideas?
  output: address: ["Hanoi"] 
  price: null 
  property_type: ["apartment"]
  area: [~80] 
  bedrooms: null
  bathrooms: null
  house_direction: null
  description: null
  floors: null
  installment_payment: null
  furniture: null
  balcony_direction: null
  input: Interested in a house in Saigon, around 60m², prefer west-facing. Any options?
  output: address: ["Ho Chi Minh"] 
  price: null 
  property_type: ["house"]
  area: [~60] 
  bedrooms: null
  bathrooms: null
  house_direction: ["west]
  description: null
  floors: null
  installment_payment: null
  furniture: null
  balcony_direction: null
  input: Want to buy house in Danang, budget around 2.5 billion VND, south-facing. Suggestions?
  output: address: ["Danang"] 
  price: [~2500000000]
  property_type: ["house"]
  area: null
  bedrooms: null
  bathrooms: null
  house_direction: ["south"]
  description: null
  floors: null
  installment_payment: null
  furniture: null
  balcony_direction: null
  input: Looking for a 2 bedroom apartment in the riverside area with an installment payment plan that will fit in my monthly budget of 20 million VND
  output: address: null
  price: [null]
  property_type: ["apartment"]
  area: null
  bedrooms: [2]
  bathrooms: null
  house_direction: null
  description: ["riverside"]
  floors: null
  installment_payment: [~20000000]
  furniture: null
  balcony_direction: null
  input: Looking for a 2 bedroom apartment in Hanoi, 2 billion VND price range, no furniture
  output: address: ["Hanoi"] 
  price: [~2000000000]
  property_type: ["apartment"]
  area: null
  bedrooms: [2]
  bathrooms: null
  house_direction: null
  description: null
  floors: null
  installment_payment: null
  furniture: ["unfurnished"]
  balcony_direction: null
  input: looking for an apartment in Saigon in the center, at least 50m² with full furniture
  output: address: ["Ho Chi Minh"] 
  price: null 
  property_type: ["apartment"]
  area: [>50] 
  bedrooms: null
  bathrooms: null
  house_direction: null
  description: ["center"]
  floors: null
  installment_payment: null
  furniture: ["full"]
  balcony_direction: null
  input: I'm interested in a 3 bedroom, 2 bathroom, 150m2 apartment in District 2 with a price range of 2 billion to 3 billion VND. Do you have anything that fits my budget?
  output: address: ["District 2", "Ho Chi Minh"] 
  price: [2000000000, 3000000000] 
  property_type: ["apartment"]
  area: [150] 
  bedrooms: [3]
  bathrooms: [2]
  house_direction: null
  description: null
  floors: null
  installment_payment: null
  furniture: null
  balcony_direction: null
  input: I’m interested in an apartment in Hanoi. My budget is 1.5 billion VND.
  output: address: ["Hanoi"] 
  price: [<1500000000]
  property_type: ["apartment"]
  area: null
  bedrooms: null
  bathrooms: null
  house_direction: null
  description: null
  floors: null
  installment_payment: null
  furniture: null
  balcony_direction: null
  input: I’m interested in a 2 bedroom apartment in Ho Chi Minh. My budget is 3 billion VND. I want the balcony face north
  output: address: ["Ho Chi Minh"] 
  price: [<3000000000]
  property_type: ["apartment"]
  area: null
  bedrooms: [2]
  bathrooms: null
  house_direction: null
  description: null
  floors: null
  installment_payment: null
  furniture: null
  balcony_direction: ["north"]
  input: 1-bedroom apartment in central Saigon with a budget of 2 billion and 300 million VND
  output: address: ["Ho Chi Minh"] 
  price: [<2300000000]
  property_type: ["apartment"]
  area: null
  bedrooms: [1]
  bathrooms: null
  house_direction: null
  description: ["central"]
  floors: null
  installment_payment: null
  furniture: null
  balcony_direction: null
  input: Looking for a 2 bedroom apartment with a balcony and garden in district 2
  output: address: ["District 2"] 
  price: null 
  property_type: ["apartment"]
  area: null
  bedrooms: [2]
  bathrooms: null
  house_direction: null
  description: ["balcony", "garden"]
  floors: null
  installment_payment: null
  furniture: null
  balcony_direction: null
  input: I’m interested in a 3 bedroom apartment in Hoang Mai district with a balcony facing the lake. My budget is 2 billion VND.
  output: address: ["Hoang Mai"] 
  price: [<2000000000]
  property_type: ["apartment"]
  area: null
  bedrooms: [3]
  bathrooms: null
  house_direction: null
  description: ["balcony", "lake"]
  floors: null
  installment_payment: null
  furniture: null
  balcony_direction: ["lake"]
  input: find me a 3-storey house with 3 bedrooms in Mai Dich ward, Cau Giay district for up to 4 billion VND with full furniture
  output: address: ["Mai Dich", "Cau Giay"] 
  price: [<4000000000]
  property_type: ["house"]
  area: null
  bedrooms: null
  bathrooms: null
  house_direction: null
  description: null
  floors: [3]
  installment_payment: null
  furniture: ["furnished"]
  balcony_direction: null
  input: I want to find apartments in Hanoi with a gym and swimming pool.
  output: address: ["Hanoi"] 
  price: null
  property_type: ["apartment"]
  area: null
  bedrooms: null
  bathrooms: null
  house_direction: null
  description: ["gym", "swimming pool"]
  floors: null
  installment_payment: null
  furniture: null
  balcony_direction: null
  input: Show me flats for installment payment under 10 million VND in Da Nang.
  output: address: ["Danang"] 
  price: null
  property_type: ["apartment"]
  area: null
  bedrooms: null
  bathrooms: null
  house_direction: null
  description: null
  floors: null
  installment_payment: [<10000000]
  furniture: null
  balcony_direction: null
  input: a 1 bedroom condo with a budget of 2.5 billion VND
  output: address: null
  price: [<2500000000]
  property_type: ["condo"]
  area: null
  bedrooms: [1]
  bathrooms: null
  house_direction: null
  description: null
  floors: null
  installment_payment: null
  furniture: null
  balcony_direction: null
  input: 500m2 house in D6, Binh Thanh, 14m deep, 10m wide. Price: 40 billion.
  output: address: ["D6", "Binh Thanh"] 
  price: [<40000000000]
  property_type: ["house"]
  area: [500]
  bedrooms: null
  bathrooms: null
  house_direction: null
  description: null
  floors: null
  installment_payment: null
  furniture: null
  balcony_direction: null
  input: I'm looking for a 2 bedroom house in the Hoan Kiem district in Hanoi with a budget of 4 billion VND.
  output: address: ["Hoan Kiem", "Hanoi"] 
  price: [<4000000000]
  property_type: ["house"]
  area: null
  bedrooms: [2]
  bathrooms: null
  house_direction: null
  description: null
  floors: null
  installment_payment: null
  furniture: null
  balcony_direction: null
  input: Find me a 1 bedroom apartment for 1.5 billion VND in Hanoi.
  output: address: ["Hanoi"] 
  price: [<1500000000]
  property_type: ["apartment"]
  area: null
  bedrooms: [1]
  bathrooms: null
  house_direction: null
  description: null
  floors: null
  installment_payment: null
  furniture: null
  balcony_direction: null
  input: I am looking for an apartment in Binh Thanh District, Ho Chi Minh City. My budget is 2 billion VND.
  output: address: ["Binh Thanh", "Ho Chi Minh"] 
  price: [<2000000000]
  property_type: ["apartment"]
  area: null
  bedrooms: null
  bathrooms: null
  house_direction: null
  description: null
  floors: null
  installment_payment: null
  furniture: null
  balcony_direction: null
  input: Search for 1Bed/1Bathroom apartments in District 1
  output: address: ["District 1"] 
  price: null
  property_type: ["apartment"]
  area: null
  bedrooms: [1]
  bathrooms: [1]
  house_direction: null
  description: null
  floors: null
  installment_payment: null
  furniture: null
  balcony_direction: null
  input: Show me houses with 3 bedrooms, 3 baths, a pool, and a gym for rent in Da Nang
  output: address: ["Da Nang"] 
  price: null
  property_type: ["house"]
  area: null
  bedrooms: [3]
  bathrooms: [3]
  house_direction: null
  description: ["pool", "gym"]
  floors: null
  installment_payment: null
  furniture: null
  balcony_direction: null
  input: Show me condos for rent in Da Nang with a view of the ocean
  output: address: ["Da Nang"] 
  price: null
  property_type: ["condo"]
  area: null
  bedrooms: null
  bathrooms: null
  house_direction: null
  description: ["ocean"]
  floors: null
  installment_payment: null
  furniture: null
  balcony_direction: null
  input: I want to find a flat in Nha Trang that is less than 20 million VND per month.
  output: address: ["Nha Trang"] 
  price: null
  property_type: ["apartment"]
  area: null
  bedrooms: null
  bathrooms: null
  house_direction: null
  description: null
  floors: null
  installment_payment: [<20000000]
  furniture: null
  balcony_direction: null
  input: show me all apartment listings in Hanoi
  output: address: ["Hanoi"] 
  price: null
  property_type: ["apartment"]
  area: null
  bedrooms: null
  bathrooms: null
  house_direction: null
  description: null
  floors: null
  installment_payment: null
  furniture: null
  balcony_direction: null
  input: How many flats are there in District 1?
  output: address: ["District 1"]
  price: null
  property_type: ["apartment"]
  area: null
  bedrooms: null
  bathrooms: null
  house_direction: null
  description: null
  floors: null
  installment_payment: null
  furniture: null
  balcony_direction: null
  input: hello, I want to find a house in Dinh Cong ward with 3 bedrooms, basic furniture and face north. Oh I also want it to near the Dinh Cong school
  output: address: ["Dinh Cong"] 
  price: null
  property_type: ["house"]
  area: null
  bedrooms: [3]
  bathrooms: null
  house_direction: ["north"]
  description: ["Dinh Cong School"]
  floors: null
  installment_payment: null
  furniture: ["furnished"]
  balcony_direction: null
  input: What is the average price of a 3 bedroom house in Hai Phong?
  output: address: ["Hai Phong"] 
  price: null
  property_type: ["house"]
  area: null
  bedrooms: [3]
  bathrooms: null
  house_direction: null
  description: null
  floors: null
  installment_payment: null
  furniture: null
  balcony_direction: null
  input: Hello, I'm looking to buy a house on installment payments in Nha Trang, I can pay about 20 million/month
  output: address: ["Nha Trang"] 
  price: [null]
  property_type: ["house"]
  area: null
  bedrooms: null
  bathrooms: null
  house_direction: null
  description: null
  floors: null
  installment_payment: [~20000000]
  furniture: null
  balcony_direction: null
  input: I'm in the market for a new house and have some specific preferences. I'm interested in a condo property with 2 bedrooms and 1 bathroom. A northwest-facing house would be preferable for consistent lighting. I'm looking for properties around 1,000 square feet in Hanoi. My budget is around 10 billion, and I'm considering properties with installment payment plans. If any of the houses are available furnished and come with an east-facing balcony, that would be a great fit. Can you provide me with choices that meet these criteria? Thank you.
  output: address: ["Hanoi"]
  price: [~10000000000]
  property_type: ["condo"]
  area: [1000] 
  bedrooms: [2]
  bathrooms: [1]
  house_direction: ["northwest"]
  description: ["downtown"]
  floors: null
  installment_payment: null
  furniture: ["furnished"]
  balcony_direction: ["east"]
  input: I'm currently in the market to purchase a house, and I have some specific criteria in mind. I'm looking for a single-family home property with 3 bedrooms and 2 bathrooms. The house should ideally be south-facing for good natural light. I'm interested in properties around 180 square feet in the Oakwood neighborhood. My budget is approximately 5 billion VND, and I'm also considering properties with installment payment plans. If any of the houses come with unfurnished options and a west-facing balcony, that would be a plus. Could you provide me with options that fit these requirements? Thank you.
  output: address: ["Oakwood"] 
  price: [<5000000000]
  property_type: ["house"]
  area: [180] 
  bedrooms: [3]
  bathrooms: [2]
  house_direction: ["south"]
  description: null
  floors: null
  installment_payment: null
  furniture: ["unfurnished"]
  balcony_direction: ["west"]
  input: I'm interested in purchasing a house that meets certain criteria. I'm specifically looking for a single-family home with 3 bedrooms and 2 bathrooms. A west-facing orientation would be ideal for afternoon sun. I'm targeting properties around 180 square feet in the Willowbrook neighborhood. My budget is approximately 3.5 billion, and I'm open to properties with flexible installment payment options. If any of the houses offer a garage and a pool, that would be fantastic. Could you help me explore options that align with these requirements? Thank you
  output: address: ["Willowbrook"] 
  price: [<3500000000]
  property_type: ["house"]
  area: [180] 
  bedrooms: [3]
  bathrooms: [2]
  house_direction: ["west"]
  description: ["garage", "pool"]
  floors: null
  installment_payment: null
  furniture: null
  balcony_direction: null
  input: Hi my name is Nhat
  output: address: null
  price: null
  property_type: null
  area: null
  bedrooms: null
  bathrooms: null
  house_direction: null
  description: null
  floors: null
  installment_payment: null
  furniture: null
  balcony_direction: null
  input: I'am so handsome
  output: address: null
  price: null
  property_type: null
  area: null
  bedrooms: null
  bathrooms: null
  house_direction: null
  description: null
  floors: null
  installment_payment: null
  furniture: null
  balcony_direction: null
  input: hi how are you?
  output: address: null
  price: null
  property_type: null
  area: null
  bedrooms: null
  bathrooms: null
  house_direction: null
  description: null
  floors: null
  installment_payment: null
  furniture: null
  balcony_direction: null
  input: Is Hoan Kiem Lake in Hanoi?
  output: address: null
  price: null
  property_type: null
  area: null
  bedrooms: null
  bathrooms: null
  house_direction: null
  description: null
  floors: null
  installment_payment: null
  furniture: null
  balcony_direction: null
  input: I want to buy a house in Thinh Liet ward, Hoang Mai district Hanoi with 4 bedrooms. I can pay for the maximum price of 5 billion VND. I want my house to have a small garden, with no furniture
  output: address: ["Thinh Liet", "Hoang Mai", "Hanoi"] 
  price: [<5000000000]
  property_type: ["house"]
  area: null
  bedrooms: [4]
  bathrooms: null
  house_direction: null
  description: ["garden"]
  floors: null
  installment_payment: null
  furniture: ["unfurnished"]
  balcony_direction: null
  input: I want to find a house with good security
  output: address: null
  price: null
  property_type: null
  area: null
  bedrooms: null
  bathrooms: null
  house_direction: null
  description: ["security"]
  floors: null
  installment_payment: null
  furniture: null
  balcony_direction: null
  input: I want to find apartments in Hanoi with a gym and swimming pool.
  output: address: ["Hanoi"] 
  price: null
  property_type: ["apartment"]
  area: null
  bedrooms: null
  bathrooms: null
  house_direction: null
  description: ["gym", "swimming pool"]
  floors: null
  installment_payment: null
  furniture: null
  balcony_direction: null
  input: Show me flats for installment payments under 10 million VND in Da Nang.
  output: address: ["Danang"] 
  price: null
  property_type: ["apartment"]
  area: null
  bedrooms: null
  bathrooms: null
  house_direction: null
  description: null
  floors: null
  installment_payment: [<10000000]
  furniture: null
  balcony_direction: null
  input: I want to find a flat for rent in Nha Trang that is less than 20 million VND per month.
  output: address: ["Nha Trang"] 
  price: null
  property_type: ["apartment"]
  area: null
  bedrooms: null
  bathrooms: null
  house_direction: null
  description: null
  floors: null
  installment_payment: [<20000000]
  furniture: null
  balcony_direction: null
  input: hey I want a house in Long Bien with a swimming pool, house face northwest and balcony face south. I also want 3 bedrooms and 2 bathrooms. my budget is 6 billion
  output: address: ["Long Bien"] 
  price: [<6000000000]
  property_type: ["house"]
  area: null
  bedrooms: [3]
  bathrooms: [2]
  house_direction: ["northwest"]
  description: ["swimming pool"]
  floors: null
  installment_payment: null
  furniture: null
  balcony_direction: ["south"]
  input: I want to buy a 4-storey house in the central of Hanoi
  output: address: ["Hanoi"] 
  price: null
  property_type: ["house"]
  area: null
  bedrooms: null
  bathrooms: null
  house_direction: null
  description: ["central"]
  floors: [4]
  installment_payment: null
  furniture: null
  balcony_direction: null
  input: hi
  output: address: null
  price: null
  property_type: null
  area: null
  bedrooms: null
  bathrooms: null
  house_direction: null
  description: null
  floors: null
  installment_payment: null
  furniture: null
  balcony_direction: null
  input: how much is a PS5?
  output: address: null
  price: null
  property_type: null
  area: null
  bedrooms: null
  bathrooms: null
  house_direction: null
  description: null
  floors: null
  installment_payment: null
  furniture: null
  balcony_direction: null
  input: I want to buy a house
  output: address: null
  price: null
  property_type: ["house"]
  area: null
  bedrooms: null
  bathrooms: null
  house_direction: null
  description: null
  floors: null
  installment_payment: null
  furniture: null
  balcony_direction: null
  input: what is your address?
  output: address: null
  price: null
  property_type: null
  area: null
  bedrooms: null
  bathrooms: null
  house_direction: null
  description: null
  floors: null
  installment_payment: null
  furniture: null
  balcony_direction: null
  input: Do you know any house in Hanoi that has 2 bedrooms and 2 bathrooms? Oh also I want my house near the school and balcony face north
  output: address: ["Hanoi"] 
  price: null
  property_type: ["house"]
  area: null
  bedrooms: [2]
  bathrooms: [2]
  house_direction: ["north"]
  description: ["school"]
  floors: null
  installment_payment: null
  furniture: null
  balcony_direction: ["north"]
  input: any house or apartment in Hanoi?
  output: address: ["Hanoi"]
  price: null
  property_type: ["house", "apartment"]
  area: null
  bedrooms: null
  bathrooms: null
  house_direction: null
  description: null
  floors: null
  installment_payment: null
  furniture: null
  balcony_direction: null
  input: the house must have 2 bathrooms in min
  output: address: null
  price: null
  property_type: ["house"]
  area: null
  bedrooms: null
  bathrooms: [>2]
  house_direction: null
  description: null
  floors: null
  installment_payment: null
  furniture: null
  balcony_direction: null
  input: {input}
  output:"""

  response = palm.generate_text(
    **defaults,
    prompt=prompt
  )
  return response.result