import qrcode

# Taking input from User

UPI_id = input("Enter the UPI_id :")

# upi://pay?pa=UPI_ID&pn=Name&am=Amount&cu=CURRENCY&tn=MESSAGE


#Defining the payment URL based on the UPI ID and the payment app
#You can modefiy these URLs based on the payment apps you want to support
# Here we are going to the Defining the payment url.

phonepe_url =  f'upi://pay?pa={UPI_id}&pn=Recipient%20Name&mc=1234'
# '''The string upi://pay?pa={UPI_id}&pn=Recipient%20Name&mc=1234 is a Unified Payments Interface (UPI) payment URL. It is used to create a link that can initiate a UPI payment request on supported payment apps like PhonePe, Google Pay, Paytm, etc.

# Here’s a detailed breakdown of the components:'''
paytm_url =  f'upi://pay?pa={UPI_id}&pn=Recipient%20Name&mc=1234'
google_pay_url =  f'upi://pay?pa={UPI_id}&pn=Recipient%20Name&mc=1234'



'''The phonepe_url string represents a Unified Payments Interface (UPI) payment link formatted for PhonePe. Here's what each part of the string indicates:

upi://pay: Specifies that this is a UPI payment request.
pa={UPI_id}: The pa parameter represents the "Payee Address," which is the UPI ID of the recipient.
pn=Recipient%20Name: 
The pn parameter specifies the "Payee Name." The %20 represents a space in URL encoding.
mc=1234: 
The mc parameter represents the "Merchant Code," which categorizes the payment (e.g., retail, utilities, etc.).'''


#Creating QR Codes For each payment app

phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_url = qrcode.make(google_pay_url)


# Display the QR code 
phonepe_qr.show()
paytm_qr.show()
google_pay_url.show()


