class SustainabilityImpact:

    def get_impact(self, category):

        impacts = {

            "Plastic": {
                "impact": "Proper recycling helps reduce plastic waste sent to landfills and the environment.",
                "sdg": "SDG 12 - Responsible Consumption and Production"
            },

            "Organic Waste": {
                "impact": "Composting organic waste can reduce landfill waste and create useful natural compost.",
                "sdg": "SDG 12 - Responsible Consumption and Production"
            },

            "Paper": {
                "impact": "Recycling paper helps reduce waste and supports efficient use of resources.",
                "sdg": "SDG 12 - Responsible Consumption and Production"
            },

            "Metal": {
                "impact": "Recycling metal helps recover valuable materials and reduces the need for new resource extraction.",
                "sdg": "SDG 12 - Responsible Consumption and Production"
            },

            "E-Waste": {
                "impact": "Proper e-waste disposal helps prevent harmful materials from entering the environment.",
                "sdg": "SDG 12 - Responsible Consumption and Production"
            },

            "Unknown": {
                "impact": "Manual verification is recommended before disposal to avoid incorrect waste segregation.",
                "sdg": "Responsible AI and Sustainable Decision-Making"
            }
        }

        return impacts.get(
            category,
            {
                "impact": "Please verify the waste type before disposal.",
                "sdg": "SDG 12 - Responsible Consumption and Production"
            }
        )