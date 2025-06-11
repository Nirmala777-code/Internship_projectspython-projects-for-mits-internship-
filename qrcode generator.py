import qrcode

# Step 1: Take input
data = input("Enter text or URL to generate QR Code: ")

# Step 2: Create QR
qr = qrcode.make(data)

# Step 3: Save file
filename = "nirmala_qr_code.png"
qr.save(filename)

print(f"\n✅ QR Code generated and saved as {filename}")