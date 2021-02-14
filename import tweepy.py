import tweepy """ libreria """


class TweetsListener(tweepy.StreamListener):
    def on_connect(self):
        print("Estoy conectado!")

    def on_status(self, status):
        print(status.text)

    def on_error(self, status_code):
        print("Error", status_code)

""" credenciales """
consumer_key = "tPhuYUlVME2IjA1rYsh26yXpa"
consumer_secret = "dS7zZIp1Jgq9dB3inxerM5GcDB85tC0CoyyOBch0aDCJPGm4PT"
access_token = "1146457499954044928-uVK4oBmxpb4SqAXRvtd8TwmJoE8SiR"
access_token_secret = "rn6LaX48qT3Gk1q47hSSTgGOqw9EahZitxX9DOgNkc2VH"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


stream = TweetsListener()
streamingApi = tweepy.Stream(auth=api.auth, listener=stream)
""" filtro los hastag """
streamingApi.filter(
    # follow=["151179935"],
    track=[
        "Coronavirus",
        "VacunaCOVID19",
        "sismo",
        "WandaVision",
        "UKlockdown3",
        "Indonesia",
        "iPhone",
        "CES2021",
        "Adictosdigitales",
        "Tech",
        "innovation",
        "iphone",
        "EE.UU",
    ],
    locations=[
        -3.17023456,
        39.22666107,
        -1.14239527,
        40.65869238,
    ],  # localizacion de cuenca
)
