Downcharmed.online home page user-hub
-------------------------------------

#    _____                                        
#   |  __ \                                       
#   | |  | | _____      ___ __                    
#   | |  | |/ _ \ \ /\ / / '_ \                   
#   | |__| | (_) \ V  V /| | | |                  
#   |_____/ \___/ \_/\_/ |_| |_|                _ 
#    / ____| |                                 | |
#   | |    | |__   __ _ _ __ _ __ ___   ___  __| |
#   | |    | '_ \ / _` | '__| '_ ` _ \ / _ \/ _` |
#   | |____| | | | (_| | |  | | | | | |  __/ (_| |
#    \_____|_| |_|\__,_|_|_ |_|_|_| |_|\___|\__,_|
#    _    _               _    _       _
#   | |  | |             | |  | |     | |         
#   | |  | |___  ___ _ __| |__| |_   _| |__       
#   | |  | / __|/ _ \ '__|  __  | | | | '_ \      
#   | |__| \__ \  __/ |  | |  | | |_| | |_) |     
#    \____/|___/\___|_|  |_|  |_|\__,_|_.__/      
#                                                 

Python/Flask Application running for downncharmed.online
under index.html and interact with users to present 
the user with options to 
 - register for newsletters (or de-register button if already registered)
 - register for gig updates (or de-register button if already registered)
 - select from a list of social redirects if no default chosen
 - display default socual if previosuly selected
     - display "remove default social button"
     - display 5 second countdown  "redirecting to SOCIAL in X seconds"
     - display "go to SOCIAL now" button for immediate redirect
 - select whether to set as default the social link chosen
 - provide links for contact page

 - legally required cookie notification
   - cookies stored for 28 days
   - cookie value details for registration
     - username
     - location (country)
     - contact details
   - cookie value details for preferred social redirect
     - preferred social link




1. user arrives on page
2. check for site cookie
3. if site cookie detected, read and redirect to preferred social platfrom
4. if site cookie absent, present main socials menu
	"Register"
		- Register for Newsletter tickbox	
		- Register for Gig Updates tickbox
	"Instagram"
	"Facebook"
	
		- Set default social tickbox
	- privacy policy link
	- contact link
	- cookie policy link
		- user country
		- user date of visit
		- username
		- email
		- whatsapp
		- social links

