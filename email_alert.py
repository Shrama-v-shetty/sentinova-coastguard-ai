import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email_alert(dam_name, severity, user_email, address, maps_link, image_path, lat=None, lon=None, selected_location=None):

    sender_email = "your-email@gmail.com"
    receiver_email = "authority-email@example.com"
    password = "your-app-password"

    subject = f"🚨 ALERT: Severe Crack in {dam_name}"

    # ----------- BUILD LOCATION DETAILS -----------
    location_details = ""

    if address:
        location_details += f"<p><b>Typed Address:</b> {address}</p>"

    if lat and lon:
        location_details += f"<p><b>Coordinates:</b> {lat}, {lon}</p>"

    if selected_location:
        location_details += f"""
        <p><b>Map Selected Location:</b><br>
        <a href="{selected_location}">Open Selected Location</a></p>
        """

    if maps_link:
        location_details += f"""
        <p><b>Final Location Link:</b><br>
        <a href="{maps_link}">Open in Google Maps</a></p>
        """

    # ----------- HTML EMAIL BODY -----------
    html_body = f"""
    <html>
    <body style="font-family: Arial;">

    <h2 style="color:red;">🚨 DAM CRACK ALERT 🚨</h2>

    <p><b>Dam Name:</b> {dam_name}</p>

    {location_details}

    <p><b>Severity Level:</b> {severity}</p>

    <p><b>Reported By:</b> {user_email}</p>

    <p style="color:red;"><b>Immediate inspection required.</b></p>

    </body>
    </html>
    """

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(html_body, 'html'))

    # ----------- ATTACH IMAGE -----------
    try:
        with open(image_path, "rb") as f:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(f.read())

        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="crack.jpg"')
        msg.attach(part)
    except:
        pass

    # ----------- SEND EMAIL -----------
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    server.send_message(msg)
    server.quit()