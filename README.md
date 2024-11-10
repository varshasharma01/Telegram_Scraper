This Selenium script automates logging into Telegram Web, entering the user’s mobile number, and verifying with an OTP for access. 
It opens Telegram Web using Chrome WebDriver and clicks on the "Login by Phone" button. 
After prompting the user to input an OTP in the console, it navigates to the "Saved Messages" chat as a point of reference. 
The script then enters a loop where it checks for new messages by monitoring elements with a specific class name. 
If a new message is detected, it prints the message text in the console. 
The script pauses briefly between checks to avoid rapid polling, creating a basic setup for real-time message monitoring in Telegram Web.
