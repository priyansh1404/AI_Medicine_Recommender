import difflib

# Medical data-->

medical_kb = {
    
    # --- Respiratory & Cold ---
    "Fever": {"med": "Paracetamol (Tylenol)", "info": "Reduces temperature and body aches."},
    "Dry Cough": {"med": "Dextromethorphan (Delsym)", "info": "Suppressant for non-productive coughs."},
    "Wet Cough": {"med": "Guaifenesin (Mucinex)", "info": "Expectorant to help thin and clear mucus."},
    "Sore Throat": {"med": "Benzocaine Lozenges (Cepacol)", "info": "Numbs the throat for temporary relief."},
    "Nasal Congestion": {"med": "Pseudoephedrine (Sudafed)", "info": "Decongestant to shrink swollen nasal passages."},

    # --- Digestive System ---
    "Heartburn": {"med": "Antacids (Tums) or Omeprazole", "info": "Neutralizes or reduces stomach acid."},
    "Diarrhea": {"med": "Loperamide (Imodium)", "info": "Slows down the digestive system."},
    "Constipation": {"med": "Bisacodyl (Dulcolax) or Miralax", "info": "Laxatives to stimulate bowel movement."},
    "Nausea": {"med": "Bismuth Subsalicylate (Pepto-Bismol)", "info": "Soothes stomach lining and reduces upset."},
    "Gas/Bloating": {"med": "Simethicone (Gas-X)", "info": "Relieves pressure caused by excess gas."},
    "Motion Sickness": {"med": "Dimenhydrinate (Dramamine)", "info": "Prevents dizziness and vomiting during travel."},
    "Loose Motion": {"med": "Loperamide (Imodium)", "info": "Slows down bowel movement. Drink plenty of ORS (Oral Rehydration Salts)."},
    "Food Poisoning": {"med": "Bismuth Subsalicylate (Pepto-Bismol)", "info": "Helps with nausea and diarrhea caused by bacteria."},
    "Stomach Cramps": {"med": "Dicyclomine (Bentyl) or Mebeverine", "info": "Antispasmodic to relax stomach muscles."},
    "Dehydration": {"med": "Electrolyte Solutions (Electral/Pedialyte)", "info": "Essential to replace lost fluids and salts during loose motion."},

    # --- Skin & First Aid ---
    "Athlete's Foot": {"med": "Terbinafine (Lamisil) or Clotrimazole", "info": "Antifungal cream for itchy, peeling feet."},
    "Cold Sores": {"med": "Docosanol (Abreva)", "info": "Antiviral cream for tingling or blistered lips."},
    "Minor Burns": {"med": "Aloe Vera or Bacitracin", "info": "Soothes skin and prevents infection."},
    "Insect Bites": {"med": "Hydrocortisone Cream", "info": "Reduces itching and inflammation from bites/rashes."},
    "Acne": {"med": "Benzoyl Peroxide or Salicylic Acid", "info": "Kills bacteria and clears clogged pores."},
    "Sunburn": {"med": "Lidocaine Spray", "info": "Provides topical numbing for painful burns."},

    # --- Eye & Ear Care ---
    "Pink Eye (Allergic)": {"med": "Ketotifen Eye Drops", "info": "Antihistamine drops for itchy, red eyes."},
    "Dry Eyes": {"med": "Artificial Tears (Refresh)", "info": "Lubricates the eye surface."},
    "Ear Wax Buildup": {"med": "Carbamide Peroxide", "info": "Softens and loosens ear wax for removal."},

    # --- Pain & General ---
    "Headache": {"med": "Ibuprofen (Advil) or Aspirin", "info": "Relieves tension and inflammatory pain."},
    "Muscle Strain": {"med": "Naproxen (Aleve)", "info": "Long-lasting anti-inflammatory for body aches."},
    "Insomnia": {"med": "Melatonin or Diphenhydramine", "info": "Sleep aids to help regulate rest cycles."},
    "Allergies": {"med": "Cetirizine (Zyrtec) or Loratadine", "info": "Non-drowsy relief for sneezing and runny nose."}
}

class AIHealthAssistant:
    def __init__(self, data):
        self.data = data
        self.symptoms = list(data.keys())

    def find_match(self, user_query):
        # Uses a similarity ratio (AI logic) to find the best match
        best_matches = difflib.get_close_matches(user_query.title(), self.symptoms, n=1, cutoff=0.4)
        return best_matches[0] if best_matches else None

    def get_advice(self, user_query):
        match = self.find_match(user_query)
        if match:
            info = self.data[match]
            return f"\n🔍 AI matched your symptom to: **{match}**\n💊 Recommended OTC: {info['med']}\nℹ️ Details: {info['info']}"
        else:
            return "\n⚠️ I couldn't find a specific match. Please describe the symptom differently or see a doctor."

# --- Interaction Loop ---
assistant = AIHealthAssistant(medical_kb)
print("="*40)
print("      AI MEDICINE RECOMMENDER")
print("="*40)

while True:
    print("\n")
    print("\n[Categories: Respiratory, Digestive, Skin, Eye/Ear, Pain]")
    query = input("Describe your symptom (or 'quit'): ").strip()

    if query.lower() in ['quit', 'exit']:
        print("\n""Stay healthy! Goodbye.")
        break

    print(assistant.get_advice(query))
    print("-" * 40)
    print("DISCLAIMER: This is not a substitute for professional medical advice.If the problem is serious consult a doctor as soon as possible.")
    print("THANK YOU!")