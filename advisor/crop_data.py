"""Facts shown for each crop the model can recommend.
(English name, emoji, Hindi name, season, duration, water need, tip)"""
CROPS = {
 "rice": ("Rice", "🌾", "चावल", "Kharif", "100–150 days", "High", "Keep 2–5 cm of standing water in the field and transplant seedlings at 20–25 days."),
 "maize": ("Maize", "🌽", "मक्का", "Kharif / Rabi", "80–110 days", "Medium", "Needs well-drained soil. Waterlogging kills young plants within days."),
 "chickpea": ("Chickpea", "🌱", "चना", "Rabi", "100–120 days", "Low", "Sow on residual monsoon moisture. Avoid heavy irrigation at flowering."),
 "kidneybeans": ("Kidney beans", "🫘", "राजमा", "Kharif / Rabi", "90–120 days", "Medium", "Stake climbing types. Plants are sensitive to frost and waterlogging."),
 "pigeonpeas": ("Pigeon peas", "🌱", "अरहर (तूर)", "Kharif", "150–180 days", "Low–Medium", "Intercrop with soybean or sorghum to use the space while it establishes."),
 "mothbeans": ("Moth beans", "🌱", "मोठ", "Kharif", "60–90 days", "Low", "Very drought hardy and suited to sandy soils. It rarely needs irrigation."),
 "mungbean": ("Mung bean", "🌱", "मूंग", "Kharif / Zaid", "60–70 days", "Low", "Short duration, so it fits between two main crops. Pick pods as they mature."),
 "blackgram": ("Black gram", "🌱", "उड़द", "Kharif", "70–90 days", "Low–Medium", "Treat seed with Rhizobium culture so the crop fixes more nitrogen."),
 "lentil": ("Lentil", "🌱", "मसूर", "Rabi", "100–110 days", "Low", "Sow in October–November. Cool weather helps the pods fill."),
 "pomegranate": ("Pomegranate", "🔴", "अनार", "Perennial", "2–3 years to fruit", "Low–Medium", "Tolerates dry spells. Drip irrigation gives bigger fruit and less cracking."),
 "mango": ("Mango", "🥭", "आम", "Perennial", "4–5 years to fruit", "Low–Medium", "Stop irrigation just before flowering, since extra water can reduce fruit set."),
 "banana": ("Banana", "🍌", "केला", "Perennial", "10–14 months", "High", "Needs steady water and potassium. Prop heavy bunches against wind."),
 "grapes": ("Grapes", "🍇", "अंगूर", "Perennial", "2–3 years to fruit", "Medium", "Train on a trellis and prune every year. Keep leaves dry to limit mildew."),
 "watermelon": ("Watermelon", "🍉", "तरबूज", "Zaid (summer)", "80–100 days", "Medium", "Prefers sandy loam. Stop irrigating a few days before harvest for sweeter fruit."),
 "muskmelon": ("Muskmelon", "🍈", "खरबूजा", "Zaid (summer)", "80–90 days", "Medium", "Mulch to keep fruit off wet soil. Ripe fruit slips easily from the vine."),
 "apple": ("Apple", "🍎", "सेब", "Perennial", "3–5 years to fruit", "Medium", "Needs winter chill and well-drained hill slopes."),
 "orange": ("Orange", "🍊", "संतरा", "Perennial", "3–4 years to fruit", "Medium", "Water at the root zone, not the trunk. Watch for citrus canker and leaf miner."),
 "papaya": ("Papaya", "🟠", "पपीता", "Perennial", "9–12 months", "Medium", "Cannot stand waterlogging. Use raised beds on heavy soil."),
 "coconut": ("Coconut", "🥥", "नारियल", "Perennial", "5–7 years to nuts", "Medium–High", "Likes a humid coastal climate. Add organic matter and potash every year."),
 "cotton": ("Cotton", "☁️", "कपास", "Kharif", "150–180 days", "Medium", "Scout for bollworm every week. Too much nitrogen delays boll set."),
 "jute": ("Jute", "🌿", "जूट", "Kharif", "100–120 days", "High", "Needs warm, humid weather. Ret stems in clean, slow water for better fibre."),
 "coffee": ("Coffee", "☕", "कॉफ़ी", "Perennial", "3–4 years to crop", "Medium", "Grow under shade trees on hill slopes and pick only ripe red cherries."),
}

def crop_ctx(key):
    n, emoji, hi, season, dur, water, tip = CROPS.get(key, (key.title(), "🌱", "", "", "", "", ""))
    return dict(key=key, name=n, emoji=emoji, hindi=hi, season=season, duration=dur, water=water, tip=tip)
