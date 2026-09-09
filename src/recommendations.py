class WasteRecommendation:

    def get_recommendation(self, object_name):

        object_name = object_name.lower().strip()

        recommendations = {

            # ♻️ PLASTIC / RECYCLABLE ITEMS
            "bottle": {
                "category": "Plastic",
                "bin": "Recyclable Bin",
                "recommendation": "Empty, rinse, and clean the bottle before placing it in the recyclable waste bin."
            },

            "cup": {
                "category": "Reusable / Check Material",
                "bin": "Manual Verification Required",
                "recommendation": "Check whether the cup is plastic, paper, ceramic, or another material before disposal. Reusable cups should not be discarded."
            },

            # 🍌 ORGANIC WASTE
            "banana": {
                "category": "Organic Waste",
                "bin": "Green / Compost Bin",
                "recommendation": "Place organic waste in a compost bin or designated green waste bin."
            },

            "apple": {
                "category": "Organic Waste",
                "bin": "Green / Compost Bin",
                "recommendation": "Place food scraps in organic waste or compost where available."
            },

            "orange": {
                "category": "Organic Waste",
                "bin": "Green / Compost Bin",
                "recommendation": "Place fruit waste in organic waste or compost where available."
            },

            # 📄 PAPER
            "book": {
                "category": "Paper",
                "bin": "Recyclable Bin",
                "recommendation": "Recycle clean and dry paper. Remove non-paper materials if possible."
            },

            # 🥫 METAL
            "can": {
                "category": "Metal",
                "bin": "Recyclable Bin",
                "recommendation": "Empty and clean the metal item before recycling."
            },

            # 💻 E-WASTE
            "cell phone": {
                "category": "E-Waste",
                "bin": "Authorized E-Waste Collection Point",
                "recommendation": "Do not place electronic waste in regular bins. Take it to an authorized e-waste collection point."
            },

            "laptop": {
                "category": "E-Waste",
                "bin": "Authorized E-Waste Collection Point",
                "recommendation": "Do not dispose of electronic devices with household waste. Use an authorized e-waste collection facility."
            },

            "keyboard": {
                "category": "E-Waste",
                "bin": "Authorized E-Waste Collection Point",
                "recommendation": "Take electronic accessories to an authorized e-waste collection point."
            },

            "mouse": {
                "category": "E-Waste",
                "bin": "Authorized E-Waste Collection Point",
                "recommendation": "Take electronic accessories to an authorized e-waste collection point."
            }
        }

        # Return known recommendation
        if object_name in recommendations:
            return recommendations[object_name]

        # Responsible AI fallback
        return {
            "category": "Unknown",
            "bin": "Manual Verification Required",
            "recommendation": "The AI could not confidently identify this item. Please verify the waste type manually."
        }