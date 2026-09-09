from src.classifier import WasteClassifier
from src.recommendations import WasteRecommendation
from src.sustainability import SustainabilityImpact

print("Loading EcoSort AI...")

# Initialize components
classifier = WasteClassifier()
recommender = WasteRecommendation()
impact_analyzer = SustainabilityImpact()

print("AI model loaded successfully!")

# Test image path
image_path = "assets/test_images/test.jpg.png"

# Detect object
results = classifier.classify(image_path)

print("\n========== ECOSORT AI RESULTS ==========")

for item in results:

    object_name = item["object"]
    confidence = item["confidence"]

    # Get recommendation
    recommendation = recommender.get_recommendation(object_name)

    # Get sustainability impact
    impact = impact_analyzer.get_impact(
        recommendation["category"]
    )

    print(f"\nDetected Object: {object_name}")
    print(f"Confidence: {confidence}%")

    print("\nWaste Information:")
    print(f"Category: {recommendation['category']}")
    print(f"Bin: {recommendation['bin']}")
    print(f"Recommendation: {recommendation['recommendation']}")

    print("\nSustainability Impact:")
    print(f"Impact: {impact['impact']}")
    print(f"SDG Alignment: {impact['sdg']}")

print("\n========================================")