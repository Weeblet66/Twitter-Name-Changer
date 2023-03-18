import tweepy
import logging
import time


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
auth = tweepy.OAuthHandler('consumer_key',
                           'consumer_secret')
auth.set_access_token('access_token',
                      'access_token_secret')

api = tweepy.API(auth, wait_on_rate_limit=True)

def validate_follower_count(user):
    # update string split if you don't use this naming format for twitter profile:
    # 'insert_your_name|{emoji_follower_count(user)} Followers'
    current_follower_count = user.name.replace('Avinash', ' ').split()
    return current_follower_count


def emoji_follower_count(user):
    emoji_numbers = {0: "0️⃣", 1: "1️⃣", 2: "2️⃣", 3: "3️⃣",
                     4: "4️⃣", 5: "5️⃣", 6: "6️⃣", 7: "7️⃣", 8: "8️⃣", 9: "9️⃣"}

    follower_count_list = [int(i) for i in str(user.followers_count)]

    emoji_followers = ''.join([emoji_numbers[k]
                               for k in follower_count_list if k in emoji_numbers.keys()])

    return emoji_followers


def main():
    api = tweepy.API(auth)

    while True:
        # change to your own twitter_handle
        user = api.get_user(screen_name='Avinash_weeb')

        if validate_follower_count(user) == emoji_follower_count(user):
            logger.info(
                f'You still have the same amount of followers, no update neccesary: {validate_follower_count(user)} -> {emoji_follower_count(user)}')
        else:
            logger.info(
                f'Your amount of followers has changed, updating twitter profile: {validate_follower_count(user)} -> {emoji_follower_count(user)}')
            # Updating your twitterprofile with your name including the amount of followers in emoji style
            api.update_profile(
                name=f'Avinash |{emoji_follower_count(user)} Followers')

        logger.info("Waiting to refresh..")
        time.sleep(60)


if __name__ == "__main__":
    main()

# python bot.py