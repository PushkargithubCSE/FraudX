from fraud_model import detect_fraud, detect_urgency  

# Sample text message for fraud detection  
text = "Your credit card data has been found under phishing scam and we would like to block your credit card. Team HDFC"

# Call the fraud detection function  
fraud_label, fraud_score = detect_fraud(text)  

# Call the urgency detection function  
urgency = detect_urgency(text)  

# Print the results  
print("🚨 Fraud Detection Results 🚨")
print(f"🔹 Fraud Label: {fraud_label}")
print(f"🔹 Fraud Score: {fraud_score:.2f}")
print(f"🔹 Urgency Level: {urgency}")
