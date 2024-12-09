import qrcode

# Taking input from User
UPI_id = input("Enter the UPI_id: ")

# Defining the universal payment URL
upi_url =  f'upi://pay?pa={UPI_id}&pn=Recipient%20Name&mc=1234'

# Creating the QR Code
upi_qr = qrcode.make(upi_url)

# Display the QR code
upi_qr.show()
