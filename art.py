logo = r'''
 _   _ ____ ___ _   _ ____ ____    _____ ____    __   _____ _    _ ____ ____ 
( )_( |_  _) __| )_( | ___|  _ \  (  _  |  _ \  (  ) (  _  | \/\/ | ___|  _ \
 ) _ ( _)(( (_-.) _ ( )__) )   /   )(_)( )   /   )(__ )(_)( )    ( )__) )   /
(_) (_|____)___(_) (_|____|_)\_)  (_____|_)\_)  (____|_____|__/\__|____|_)\_)
'''

logo_vs = r'''
 _  _ ___ 
( \/ ) __)
 \  /\__ \
  \/ (___/
'''


# def game():
#     print(logo)
#     score = 0
#     game_should_continue = True
#     account_a = get_random_account()
#     account_b = get_random_account()
#
#     while game_should_continue:
#         account_a = account_b
#         account_b = get_random_account()
#
#         while account_a == account_b:
#             account_b = get_random_account()
#
#         print(f"Compare A: {format_data(account_a)}.")
#         print(logo_vs)
#         print(f"Against B: {format_data(account_b)}.")
#
#         guess = input("Who has more followers? Type 'A' or 'B': ").lower()
#         a_follower_count = account_a["follower_count"]
#         b_follower_count = account_b["follower_count"]
#         is_correct = check_answer(guess, a_follower_count, b_follower_count)
#
#         clear()
#         print(logo)
#         if is_correct:
#             score += 1
#             print(f"You're right! Current score: {score}.")
#         else:
#             game_should_continue = False
#             print(f"Sorry, that's wrong. Final score: {score}")
