from ping3 import ping
from twilio.rest import Client
import speedtest

# Twilio account details
account_sid = 'your twilio_account_sid'
auth_token = 'your twilio_auth_token'
twilio_phone_number = 'your twili0_phone_number'
client_phone_numbers =["+910000000000","+910000000000"]

# Router details: Use static IP addresses for each router
routers = [
    {"ip": "Router's Static_IP", "name": "Router_1"},
    {"ip": "Router's Static_IP", "name": "Router_2"},
    {"ip": "Router's Static_IP", "name": "Router_3"},
    {"ip": "Router's Static_IP", "name": "Router_4"}
]

# Thresholds for connection status
LATENCY_THRESHOLD = 100  # ms
DOWNLOAD_THRESHOLD = 10  # Mbps
UPLOAD_THRESHOLD = 5     # Mbps

# Track previous connection statuses to detect changes
previous_statuses = {router["ip"]: "Unknown" for router in routers}

# Twilio client
twilio_client = Client(account_sid, auth_token)

# Function to send SMS
def send_sms(body):
    for phone_number in client_phone_numbers:
        try:
            message = twilio_client.messages.create(
                body=body,
                from_=twilio_phone_number,
                to=phone_number
            )
            print(f"SMS sent successfully to {phone_number}. Message SID: {message.sid}")
        except Exception as e:
            print(f"Error sending SMS to {phone_number}: {e}")

# Ping the router to check latency
def test_latency(router_ip):
    try:
        response = ping(router_ip)
        if response is not None:
            return response  # Latency in ms
        else:
            print(f"Router {router_ip} is unreachable.")
            return None  # Indicates the router is unreachable
    except OSError as e:
        print(f"Error reaching {router_ip}: {e}")
        return None  # Return None if there's an error reaching the router

# Check download and upload speed
import speedtest

# Check download and upload speed with error handling
def test_speed():
    try:
        st = speedtest.Speedtest()
        st.download()
        st.upload()
        download_speed = st.results.download / 10**6  # Convert from bps to Mbps
        upload_speed = st.results.upload / 10**6      # Convert from bps to Mbps
        return download_speed, upload_speed
    except Exception as e:
        print(f"Error testing speed: {e}")
        return None, None  # Return None if there's an error testing speed

# Determine connection status
def determine_status(latency, download_speed, upload_speed):
    if latency is None:
        return "Connection Off"
    elif (latency > LATENCY_THRESHOLD or
          (download_speed is not None and download_speed < DOWNLOAD_THRESHOLD) or
          (upload_speed is not None and upload_speed < UPLOAD_THRESHOLD)):
        return "Bad"
    else:
        return "Good"

# Main function to gather information for all routers
def get_network_info():
    for router in routers:
        router_ip = router["ip"]
        router_name = router["name"]

        # Test latency for each router
        latency = test_latency(router_ip)

        # Test download and upload speeds only if latency is available (connection is on)
        download_speed, upload_speed = (None, None)
        if latency is not None:
            download_speed, upload_speed = test_speed()

        # Determine connection status
        status = determine_status(latency, download_speed, upload_speed)

        # Check if the connection status is "Connection Off"
        if status == "Connection Off" and previous_statuses[router_ip] != "Connection Off":
            # Send an SMS notification for "Connection Off"
            send_sms(f"Alert: Connection is down for {router_name} ({router_ip}). Please check the router.")

        # Update the previous status to avoid duplicate notifications
        previous_statuses[router_ip] = status

# Schedule the task to run every 1 minute
# schedule.every(1).minutes.do(get_network_info)

# Run the scheduler to continuously check every minute
if __name__ == "__main__":
    while True:
        # schedule.run_pending()  # Run any scheduled task
        # time.sleep(1)  # Sleep for 1 second before checking the schedule again
        get_network_info()
