# secondHandMETU
Welcome to the secondHandMETU repository! This project is designed to provide a sustainable way to buy and sell second-hand items within the METU community. The repository consists of two leading apps - "userAuthentication" and "marketplace," each serving distinct functionalities to improve the user experience.

The secondHandMETUproject directory includes the Django apps that consist of both front-end and back-end codes for this project. The progress directory includes the submitted progress report, Environments-Scripts-Project related files directory is more about the environment, packages etc. 

The project is structured into two main apps, each with its designated purpose:

userAuthentication
--------------------------------------------------
The "userAuthentication" app focuses on user-related functionalities, including authentication, registration, and profile management.

Models:
UserProfile: This model stores essential user information such as email and phone number. Additional fields, like profile_picture, are implemented to support future project stages.

Views:
register: Handles user registration, ensuring a seamless process for new users to join the system.
user_login: Manages user login using the AuthenticationForm, redirecting authenticated users to the dashboard.
dashboard: Retrieves and displays the user profile upon successful login.
user_logout: Implements the logout functionality, redirecting users to the home page.

Forms:
UserProfileForm: This enables users to add phone numbers and emails to their profiles when visiting the Profile page.

URLs:
urls.py: Manages URL patterns (routing) for authentication-related views.

Templates: 
register.html: Page with form for user registration.
login.html: Page with form for user login.
dashboard.html: Dashboard view displaying the nav-bar.
profile/user_profile.html: User profile editing page.

marketplace
----------------------------------------------------

The "marketplace" app is created for buying and selling items within the project.

Models:
Item: Represents the items the users want to sell in the marketplace, including properties such as item name, price, category, condition, description, and image. Items are associated with users through a foreign key.

Views:
sell_item: Enables the addition of new items for sale, redirecting users to the dashboard upon successful item registration.
my_posts: Displays posts made by the currently authenticated user.

Forms:
SellItemForm:  Takes information about item properties when users visit the Sell Item page.

URLs:
urls.py: Manages URL patterns (routing) for marketplace-related views.

Templates
sell_item.html: Form page for selling items.
my_posts.html: View displaying posts made by the currently authenticated user.
