import HealthcareAgent as ha

def get_nutrition_recommendation(query_food=None):
    if not query_food:
        return "🥗 Please specify a food item to get nutrition info."
    try:
        # جستجوی اطلاعات تغذیه‌ای برای کالای درخواست شده
        result = ha.api(api_name="food_calories_usda", query=query_food, topk=5)
        item_list_pretty = result.get("item_list_pretty", [])
        # نمایش اولین مورد
        if item_list_pretty:
            return "🥗 Nutrition info:\n" + item_list_pretty[0]
        else:
            return "🥗 No nutrition data found for " + query_food
    except Exception as e:
        return "❌ Nutrition lookup failed: " + str(e)
