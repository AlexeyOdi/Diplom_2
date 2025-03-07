from user_generator import generate_email

create_user_error = '{"success":false,"message":"You should be authorised"}'
success = '"success":true'
create_exist_error = "User already exists"
create_field_error = "Email, password and name are required fields"
login_field_error =  "email or password are incorrect"
email_to_change = {'email': f'{generate_email()}'}
password_to_change = {'password': 'asdzxcasd'}
name_to_change = {'name': 'Alex'}
email_change_error = "User with such email already exists"
order_data = {"ingredients": ['61c0c5a71d1f82001bdaaa6d', '61c0c5a71d1f82001bdaaa6f', '61c0c5a71d1f82001bdaaa72']}
ingr_error = "Ingredient ids must be provided"
using_email = {'email': 'alex@yandex.ru'}

