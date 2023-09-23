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

def generate_text(input): 
  prompt = """input: I want to find a house with 2 floors in Hanoi with price under 5 billion VND. Don't need to have furniture
address: ["Hanoi"]  
price: [<5000000000] 
property_type: ["house"] 
area: null 
bedrooms: null 
bathrooms: null 
house_direction: null 
description: null 
floors: [2]
installment_payment: null 
furniture: ["unfurnished"] 
balcony_direction: null 
output: {
    "query": {
      "bool": {
        "must": [
          {
            "match": {
              "property_type": "house"
            }
          },
          {
            "range": {
              "price": {
                "lte": 5000000000
              }
            }
          },
          {
            "match": {
              "floors": {
                "query": 2
              }
            }
          },
          {
            "match": {
              "address": {
                "query": "Hanoi"
              }
            }
          },
          {
            "match": {
              "furniture": "unfurnished"
            }
          }
        ]
      }
    }
  }
input: I'm looking for a house in Ho Chi Minh City with at least 3 bedrooms.
address: ["Ho Chi Minh"]  
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

output: {
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "address": {
            "query": "Ho Chi Minh City",
            "operator": "and"
           }
          }
        },
        {
          "match": {
            "property_type": "house"
          }
        },
        {
          "range": {
            "bedrooms": {
              "gte": 3
            }
          }
        }
      ]
    }
  }
}

input: I want to find apartments in Hanoi with a gym and swimming pool.
address: ["Hanoi"] 
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
output: {
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "address": {
              "query": "Hanoi",
              "operator": "and"
            }
          }
        },
        {
          "match": { 
            "property_type": "apartment" 
          } 
        },
        {
          "match": {
            "description": "gym"
          }
        },
        {
          "match": {
            "description": "swimming pool"
          }
        }
      ]
    }
  }
}
input: Show me flats for installment payments under 10 million VND in Da Nang.
address: ["Danang"] 
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
output: {
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "property_type": "apartment"
          }
        },
        {
          "match": {
            "address": {
              "query": "Da Nang",
              "operator": "and"
            }
          }
        },
        {
          "range": {
            "installment_payment": {
              "lte": 10000000
            }
          }
        }
      ]
    }
  }
}

input: Search for 1Bed/1Bathroom apartments in District 1
address: ["District 1"]  
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
output: {
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "bedrooms": {
              "query": 1,
              "operator": "and"
            }
          }
        },
        {
          "match": {
            "bathrooms": {
              "query": 1,
              "operator": "and"
            }
          }
        },
        {
          "match": {
            "address": {
              "query": "District 1",
              "operator": "and"
            }
          }
        },
        {
          "match": {
            "property_type": {
              "query": "apartment"
            }
          }
        }
      ]
    }
  }
}
input: Show me houses with 3 bedrooms, 3 baths, a pool, and a gym for rent in Da Nang
address: ["Da Nang"]  
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
output: {
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "property_type": "house"
          }
        },
        {
          "match": {
            "bedrooms": {
              "query": 3,
            }
          }
        },
        {
          "match": {
            "bathrooms": {
              "query": 3,
            }
          }
        },
        {
          "match": {
            "description": "pool"
          }
        },
        {
          "match": {
            "description": "gym"
          }
        },
        {
          "match": {
            "address": {
              "query": "Da Nang",
              "operator": "and"
            }
          }
        }
      ]
    }
  }
}
input: Show me condos for rent in Da Nang with a view of the ocean
address: ["Da Nang"]  
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
output: {
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "property_type": "condo"
          }
        },
        {
          "match": {
            "location": {
              "query": "Da Nang",
              "operator": "and"
            }
          }
        },
        {
          "match": {
            "description": "ocean view"
          }
        }
      ]
    }
  }
}
input: What is the average price of a 3 bedroom house in Hai Phong?
address: ["Hai Phong"]  
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
output: {
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "bedrooms": {
              "query": "3"
            }
          }
        },
        {
          "match": {
            "address": {
              "query": "Hai Phong",
              "operator": "and"
            }
          }
        }
      ]
    }
  },
  "aggs": {
    "prices": {
      "avg": {
        "field": "price"
      }
    }
  }
}
input: I want to find a flat for rent in Nha Trang that is less than 20 million VND per month.
address: ["Nha Trang"]  
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
output: {
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "property_type": "apartment"
          }
        },
        {
          "range": {
            "installment_payment": {
              "lte": 20000000
            }
          }
        },
        {
          "match": {
            "location": {
              "query": "Nha Trang",
              "operator": "and"
            }
          }
        }
      ]
    }
  }
}
input: Show me condos for rent in Da Nang with a view of the ocean
address: ["Da Nang"]  
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

output: {
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "property_type": "condo"
          }
        },
        {
          "match": {
            "location": {
              "query": "Da Nang",
              "operator": "and"
            }
          }
        },
        {
          "match": {
            "description": "ocean"
          }
        }
      ]
    }
  }
}
input: Show me flats for installment payments under 10 million VND in Da Nang.
address: ["Danang"] 
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
output: {
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "property_type": "apartment"
          }
        },
        {
          "match": {
            "address": {
              "query": "Da Nang",
              "operator": "and"
            }
          }
        },
        {
          "range": {
            "installment_payment": {
              "lte": 10000000
            }
          }
        }
      ]
    }
  }
}
input: i want a 4 bedrooms house in Ha Noi with a budget of 5 billion
address: ["Ha Noi"]  
price: [<5000000000] 
property_type: ["house"] 
area: null 
bedrooms: [4] 
bathrooms: null 
house_direction: null 
description: null 
floors: null 
installment_payment: null 
furniture: null 
balcony_direction: null
output: {
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "address": {
              "query": "Ha Noi",
              "operator": "and"
            }
          }
        },
        {
          "match": {
            "property_type": "house"
          }
        },
        {
          "range": {
            "price": {
              "lte": 5000000000
            }
          }
        },
        {
          "match": {
            "bedrooms": 4
            }
          }
        }
      ]
    }
  }
}
input: I am looking for 1 bedroom apartment for rent in District 1 with a maximum budget of 15 million VND
address: ["District 1"]  
price: [<=15000000] 
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
output: {
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "address": {
              "query": "District 1",
              "operator": "and"
            }
          }
        },
        {
          "match": {
            "bedrooms": {
              "query": 1,
              "operator": "and"
            }
          }
        },
        {
          "range": {
            "price": {
              "lte": 15000000
            }
          }
        },
        {
          "match": {
            "property_type": "apartment"
          }
        }
      ]
    }
  }
}
input: 3 bedroom house for rent in Hanoi with max price 3 billion VND and minimum price 2 billion VND
address: ["Hanoi"]  
price: [2000000000, 3000000000] 
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
output: {
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "property_type": "house"
          }
        },
        {
          "range": {
            "price": {
              "gte": 2000000000,
              "lte": 3000000000
            }
          }
        },
        {
          "match": {
            "bedrooms": {
              "query": 3
            }
          }
        }
      ]
    }
  }
}
input: Looking for a 1 bedroom, 1 bathroom apartment in Hanoi under 25 million VND/month
address: ["Hanoi"]  
price: [<25000000] 
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
output: {
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "bedrooms": {
              "query": 1,
              "operator": "and"
            }
          }
        },
        {
          "match": {
            "bathrooms": {
              "query": 1,
              "operator": "and"
            }
          }
        },
        {
          "range": {
            "price": {
              "lte": 25000000
            }
          }
        },
        {
          "match": {
            "property_type": {
              "query": "apartment",
              "operator": "and"
            }
          }
        },
        {
          "match": {
            "address": {
              "query": "Hanoi",
              "operator": "and"
            }
          }
        }
      ]
    }
  }
}
input: I want to buy a house in Thinh Liet ward, Hoang Mai district Hanoi with 4 bedrooms. I can pay for the maximum price of 5 billion VND. I want my house to have a small garden, with basic furniture
address: ["Thinh Liet", "Hoang Mai", "Hanoi"] 
price: [<5000000000]
property_type: ["house"]
area: null
bedrooms: [4]
bathrooms: null
house_direction: null
description: ["garden"]
floors: null
installment_payment: null
furniture: ["furnished"]
balcony_direction: null
output: {
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "location": {
              "query": "Thinh Liet",
              "operator": "and"
            }
          }
        },
        {
          "match": {
            "location": {
              "query": "Hoang Mai",
              "operator": "and"
            }
          }
        },
        {
          "match": {
            "location": {
              "query": "Hanoi",
              "operator": "and"
            }
          }
        },
        {
          "match": {
            "property_type": "house"
          }
        },
        {
          "match": {
            "bedrooms": {
              "query": 4
            }
          }
        },
        {
          "match": {
            "description": "garden"
          }
        },
        {
          "match": {
            "furniture": "furnished"
          }
        },
        {
          "range": {
            "price": {
              "lte": 5000000000
            }
          }
        }
      ]
    }
  }
}
input: I'm interested in purchasing a house that meets certain criteria. I'm specifically looking for a single-family home with 3 bedrooms and 2 bathrooms. A west-facing orientation would be ideal for afternoon sun. I'm targeting properties around 180 square feet in the Willowbrook neighborhood. My budget is approximately 3.5 billion, and I'm open to properties with flexible installment payment options. If any of the houses offer a garage and a pool, that would be fantastic. Could you help me explore options that align with these requirements? Thank you
address: ["Willowbrook"] 
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
output: {
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "property_type": "house"
          }
        },
        {
          "match": {
            "bedrooms": {
              "query": 3
            }
          }
        },
        {
          "match": {
            "bathrooms": {
              "query": 2
            }
          }
        },
        {
          "range": {
            "area": {
              "lte": 170,
              "gte": 190
            }
          }
        },
        {
          "match": {
            "house_direction": {
              "query": "west"
            }
          }
        },
        {
          "match": {
            "description": {
              "query": "garage"
            }
          }
        },
        {
          "match": {
            "description": {
              "query": "pool"
            }
          }
        },
        {
          "match": {
            "address": {
              "query": "Willowbrook"
              "operator": "and"
            }
          }
        },
        {
          "range": {
            "price": {
              "lte": 3500000000
            }
          }
        }
      ]
    }
  }
}
input: I'm in the market for a new house and have some specific preferences. I'm interested in a condo property with 2 bedrooms and 1 bathroom. A northwest-facing house would be preferable for consistent lighting. I'm looking for properties around 1,000 square feet in Hanoi. My budget is around 10 billion, and I'm considering properties with installment payment plans. If any of the houses are available furnished and come with an east-facing balcony, that would be a great fit. Can you provide me with choices that meet these criteria? Thank you.
address: ["downtown"]
price: [~10000000000]
property_type: ["condo"]
area: [1000] 
bedrooms: [2]
bathrooms: [1]
house_direction: ["northwest"]
description: null
floors: null
installment_payment: null
furniture: ["furnished"]
balcony_direction: ["east"]
output: {
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "property_type": "condo"
          }
        },
        {
          "match": {
            "bedrooms": {
              "query": 2
            }
          }
        },
        {
          "match": {
            "bathrooms": {
              "query": 1
            }
          }
        },
        {
          "match": {
            "area": {
              "query": 1000
            }
          }
        },
        {
          "match": {
            "house_direction": {
              "query": "northwest"
            }
          }
        },
        {
          "match": {
            "address": {
              "query": "Hanoi"
            }
          }
        },
        {
          "range": {
            "price": {
              "lte": 10000000000
            }
          }
        },
        {
          "match": {
            "furniture": "furnished"
          }
        },
        {
          "match": {
            "balcony_direction": {
              "query": "east"
            }
          }
        }
      ]
    }
  }
}
input: Hello, I'm looking to buy a house on installment payments in Nha Trang, I can pay about 20 million/month
address: ["Nha Trang"] 
price: null
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
output: {
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "property_type": "house"
          }
        },
        {
          "match": {
            "address": {
              "query": "Nha Trang",
              "operator": "and"
            }
          }
        },
        {
          "range": {
            "installment_payment": {
              "lte": 20000000
            }
          }
        }
      ]
    }
  }
}
input: my request remains the same but now I want to move to Ho Chi Minh City
address: ["Nha Trang"] 
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
output: {
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "property_type": "house"
          }
        },
        {
          "match": {
            "address": {
              "query": "Ho Chi Minh City",
              "operator": "and"
            }
          }
        },
        {
          "match": {
            "bedrooms": 3
          }
        }
      ]
    }
  }
}
input: how about the one with price around 4 billion VND?
address: ["Hanoi"]  
price: [<5000000000] 
property_type: ["house"] 
area: null 
bedrooms: [>2] 
bathrooms: null 
house_direction: null 
description: null 
floors: null 
installment_payment: null 
furniture: null 
balcony_direction: null 
output: {
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "property_type": "house"
          }
        },
        {
          "range": {
            "price": {
              "lte": 4000000000
            }
          }
        },
        {
          "match": {
            "address": {
              "query": "Hanoi",
              "operator": "and"
            }
          }
        },
        {
          "range": {
            "bedrooms": {
              "gte": 2
            }
          }
        }
      ]
    }
  }
}
input: hey I want a house in Long Bien with a swimming pool, house face northwest and balcony face south. I also want 3 bedrooms and 2 bathrooms. my budget is 6 billion
address: ["Long Bien"] 
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
output: {
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "property_type": "house"
          }
        },
        {
          "range": {
            "price": {
              "lte": 6000000000
            }
          }
        },
        {
          "match": {
            "bedrooms": {
              "query": 3
            }
          }
        },
        {
          "match": {
            "bathrooms": {
              "query": 2
            }
          }
        },
        {
          "match": {
            "house_direction": {
              "query": "northwest"
            }
          }
        },
        {
          "match": {
            "description": {
              "query": "swimming pool"
            }
          }
        },
        {
          "match": {
            "balcony_direction": {
              "query": "south"
            }
          }
        },
        {
          "match": {
            "address": {
              "query": "Long Bien",
              "operator": "and"
            }
          }
        }
      ]
    }
  }
}
input: but I want my house direction is north
address: ["Hanoi"]  
price: null 
property_type: ["house"] 
area: null 
bedrooms: null 
bathrooms: null 
house_direction: null
description: null 
floors: [4]
installment_payment: null 
furniture: null 
balcony_direction: null
output: {
    "query": {
      "bool": {
        "must": [
          {
            "match": {
              "property_type": "house"
            }
          },
          {
            "match": {
              "floors": 4
          },
          {
            "match": {
              "address": {
                "query": "Hanoi",
                "operator": "and"
              }
            }
          },
          {
            "match": {
              "house_direction": {
                "query": "north"
              }
            }
          }
        ]
      }
    }
  }
input: Hi, how are you?
address: null
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
output: null
input: nice to meet you
address: null
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
output: null
input: how many apartment are there in Hanoi?
address: ["Hanoi"]  
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
output: {
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "property_type": "apartment"
          }
        },
        {
          "match": {
            "address": {
              "query": "Hanoi",
              "operator": "and"
            }
          }
        }
      ]
    }
  },
}
input: I'm interested in purchasing a 3-storey house with full furniture in a particular district of Ho Chi Minh City, preferably District 1. My budget is open to negotiation but ideally between 4 billion and 6 billion VND. I'm looking for a house with an area of around 50 square meters, with a tolerance of about 5 square meters. I have a preference for houses that face the south or west direction. Could you provide me with some options that meet these criteria?
address: ["District 1", "Ho Chi Minh"] 
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
output: {
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "property_type": "house"
          }
        },
        {
          "range": {
            "area": {
              "lte": 55,
              "gte": 45
            }
          }
        },
        {
          "match": {
            "floors": 3
          }
        },
        {
          "match": {
            "address": {
              "query": "District 1",
              "operator": "and"
            }
          }
        },
        {
          "range": {
            "price": {
              "lte": 6000000000,
              "gte": 4000000000
            }
          }
        },
        {
          "match": {
            "house_direction": {
              "query": "south",
              "operator": "or"
            }
          }
        },
        {
          "match": {
            "house_direction": {
              "query": "west",
              "operator": "or"
            }
          }
        },
        {
          "match": {
            "furniture": "furnished"
          }
        }
      ]
    }
  }
  input: any house or apartment in Hanoi?
  address: ["Hanoi"]
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
  output: {
    "query": {
      "bool": {
        "must": [
          {
            "match": {
              "address": {
                "query": "Hanoi",
                "operator": "and"
              }
            }
          },
          {
            "match": {
              "property_type": {
                "query": "house apartment",
                "operator": "or"
              }
            }
          }
        ]
      }
    }
  }
  input: I want a house that have the cheapest price 
  address: ["Ho Chi Minh"]
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
  output: {
    "query": {
      "bool": {
        "must": {
          "match": {
            "address": "Hanoi"
          },
          "match": {
            "property_type": "house"
          }
        }
      }
    },
    "sort": [
      {
        "price": {
          "order": "asc"
        }
      }
    ]
  }
  input: show me the one that has the most expensive price
  address: ["Hanoi"]
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
  output: {
    "query": {
      "bool": {
        "must": {
          "match": {
            "address": "Hanoi"
          }
        }
      }
    },
    "sort": [
      {
        "price": {
          "order": "desc"
        }
      }
    ]
  }
  input: what is the most expensive apartment in Binh Duong?
  address: ["Binh Duong"]
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
  output: {
    "query": {
      "bool": {
        "must": {
          "match": {
            "address": "Hanoi"
          },
          "match": {
            "property_type": "apartment"
          }
        }
      }
    },
    "sort": [
      {
        "price": {
          "order": "desc"
        }
      }
    ]
  }
  input: show me the cheapest house you have
  address: null
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
  output: {
    "sort": [
      {
        "price": {
          "order": "asc"
        }
      }
    ]
  }
  input: show me houses which price is larger than 1 trillion VND 
  address: ["Hanoi"]
  price: [>1000000000000]
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
  output: {
    "query": {
      "bool": {
        "must": [
          {
            "match": {
              "property_type": "house"
            }
          },
          {
            "range": {
              "price": {
                "gte": 1000000000000
              }
            }
          }
        ]
      }
    }
  }
  input: I want to find a house in Danang
  address: ["Danang"] 
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
  output: {
    "query": {
      "bool": {
        "must": [
          {
            "match": {
              "property_type": "house"
            }
          },
          {
            "match": {
              "address": {
                "query": "Danang"
              }
            }
          }
        ]
      }
    }
  }
  input: I want to find an apartment in Ha Noi that has 2 bedrooms and the house direction will be north or south
  address: ["Hanoi"] 
  price: null
  property_type: ["apartment"]
  area: null
  bedrooms: [2]
  bathrooms: null
  house_direction: ["north", "south"]
  description: null
  floors: null
  installment_payment: null
  furniture: null
  balcony_direction: null
  output: {
    "query": {
      "bool": {
        "must": [
          {
            "match": {
              "property_type": "apartment"
            }
          },
          {
            "match": {
              "address": {
                "query": "Hanoi"
              }
            }
          },
          {
            "match": {
              "bedrooms": 2
            }
          },
          {
            "match": {
              "house_direction": {
                "query": "north south",
                "operator": "or"
              }
            }
          }
        ]
      }
    }
  }
  input: I want to find a house with 2 floors in Kozai with price under 5 billion VND. Must have furniture
address: ["Cau Giay"]  
price: [<5000000000] 
property_type: ["house"] 
area: null 
bedrooms: null 
bathrooms: null 
house_direction: null 
description: null 
floors: [2]
installment_payment: null 
furniture: ["furnished"] 
balcony_direction: null 
output: {
    "query": {
      "bool": {
        "must": [
          {
            "match": {
              "property_type": "house"
            }
          },
          {
            "range": {
              "price": {
                "lte": 5000000000
              }
            }
          },
          {
            "match": {
              "floors": {
                "query": 2
              }
            }
          },
          {
            "match": {
              "address": {
                "query": "Cau Giay"
              }
            }
          },
          {
            "match": {
              "furniture": "furnished"
            }
          }
        ]
      }
    }
  }
  """
  prompt2 = f"""{input}\noutput:"""

  response = palm.generate_text(
    **defaults,
    prompt=prompt+prompt2
  )
  return response.result
# print(generate_text(input))