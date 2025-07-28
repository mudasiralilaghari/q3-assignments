from agents import function_tool

@function_tool()
def set_destination(destination: str) -> str:
    return destination

@function_tool()
def get_flights(destination: str) -> list[dict]:
    return [
        {"airline": "Air PKR", "flight_no": "PK001", "depart": "09:00", "arrive": "12:00", "price_usd": 500},
        {"airline": "Sky Express", "flight_no": "SE123", "depart": "14:00", "arrive": "17:00", "price_usd": 450},
        {"airline": "Global Air", "flight_no": "GA456", "depart": "20:00", "arrive": "23:00", "price_usd": 480}
    ]

@function_tool()
def suggest_hotels(destination: str) -> list[dict]:
    return [
        {"name": "Comfort Inn", "city": destination, "stars": 3, "price_per_night_usd": 80},
        {"name": "SkyView Hotel", "city": destination, "stars": 4, "price_per_night_usd": 120},
        {"name": "BudgetStay", "city": destination, "stars": 2, "price_per_night_usd": 50},
        {"name": "Grand Palace", "city": destination, "stars": 5, "price_per_night_usd": 200}
    ]

@function_tool()
def recommend_exploration(destination: str) -> dict:
    return {
        "attractions": [
            {"name": "Old Town Square", "type": "Historical", "entry_fee_usd": 10},
            {"name": "Riverfront Park", "type": "Nature", "entry_fee_usd": 0},
            {"name": "City Museum", "type": "Cultural", "entry_fee_usd": 15}
        ],
        "activities": [
            {"name": "Guided City Tour", "duration_h": 3, "price_usd": 40},
            {"name": "Sunset Boat Cruise", "duration_h": 2, "price_usd": 60},
            {"name": "Mountain Hike", "duration_h": 5, "price_usd": 30}
        ],
        "food": [
            {"dish": "Local BBQ Ribs", "type": "Street Food", "avg_price_usd": 8},
            {"dish": "Seafood Platter", "type": "Fine Dining", "avg_price_usd": 25},
            {"dish": "Traditional Stew", "type": "Local Cuisine", "avg_price_usd": 12}
        ]
    }
