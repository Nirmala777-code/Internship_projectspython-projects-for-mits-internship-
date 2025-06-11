print("🤖 Internship Domain Recommendation")
print("Answer the following questions (yes/no):")

coding = input("Do you like coding? ")
net = input("Do you enjoy networking or security? ")
design = input("Are you interested in design or websites? ")
data = input("Do you enjoy analyzing or organizing data? ")
marketing = input("Do you like talking or promoting products? ")

if coding == "yes" and net == "yes":
    print("✅ Recommended: Cybersecurity or Ethical Hacking")
elif coding == "yes" and design == "yes":
    print("✅ Recommended: Web Development or Front-End Design")
elif data == "yes":
    print("✅ Recommended: Data Analytics or Machine Learning")
elif marketing == "yes":
    print("✅ Recommended: Digital Marketing or Sales Internships")
else:
    print("✅ Recommended: General Internship – Explore multiple domains")