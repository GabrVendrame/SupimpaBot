import os
import random
import tweepy

consumer_key = os.environ["APIKEY"]
consumer_secret = os.environ["APISECRET"]
access_token = os.environ["ACCESSTOKEN"]
access_token_secret = os.environ["ACCESSTOKENSECRET"]

auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

def perolas():
    perolasdovoice = ["\"Se o Fulano quiser crua eu tiro pra ele\"",
        "\"Ciclano, ta certo seus exercicios?\"\n\n\"Sla n sei, acho que não\"",
        "\"eu dei vc gostou?\"\n\n\"gostei\"",
        "\"isso q ele falou foi lúcido\"\n\n\"foi, mas isso não se tweeta\"",
        "\"vc sabe como faz pra encontrar um tetraplégico?\"\n\n*silêncio mortal de 1 minuto*\n\n\"é só ir no lugar q vc deixou ele\"",
        "\"mano faz dias q to vendo video de um ex salva-vidas nadando\"",
        "\"Como que chama quando vc passa a mão\"",
        "\"vou fazer uma função em homenagem ao Beltrano chamada o_grande_reset()\"",
        "\"eu exclui o tiktok\"",
        "\"é lá na coreia do sul q é o kin jon un? a nao é na china né\"",
        "\"Não ele pegou o pau ele pegou o pau\"",
        "\"Eu sou a cura gay\"",
        "\"ah mas esses 2 últimos anos nem contou\"",
        "\"Mó estranho vei, a Anitta de roupa\"",
        "\"O objetivo é sair de lá com a ruela do eno\"",
        "\"cabelo branco é dentro\"",
        "\"e cade voce na aula?\"\n\n\"aula é só 9:40 mlk\"\n\n\"e aula de matematica?\"\n\n\"meeeeeeeee tem matemática\"",
        "\"Minha vida é um algoritmo guloso, eu vou sempre no mais facil\"",
        "\"ai eu amo frontend\"",
        "\"ai meu pinto\"\n\n\"seu pinto não, nosso\"",
        "\"não fazia muito sentido um era ruivo e o outro é preto\"",
        "\"se isso aqui nao for ponto G eu to maluco\"",
        "\"aquele dedo me fudeu\"",
        "\"vc que ta acostumado a dar a rodinha né\"\n\n\"só pra vc\"",
        "\"as bolas do Radahn machucam ein\"",
        "\"eu pegaria fácil\"",
        "\"ou vc é calvo, ou vc é broxa, ou vc é gay. Eu n sou calvo, n sou broxa...\"",
        "\"ah não vei, pelo amor de Deus vamo mais um lol ae\"",
        "\"o background da asuka é bonito porra\"",
        "\"rust é estranho né?\"\n\n\"sim, muito bom\"",
        "\"fazer CC é igual lavar a louça, sentimento 0\"",
        "\"brasil da dinheiro pra quem? pra mim n da nao\"",
        "\"eu gosto de segregação...\tde newbas\"",
        "\"é muito grande, mas é muito bom...\tmas é grande\"",
        "\"cê quer q eu boto mais?\"\n\n\"SIM?!\"",
        "\"Neymar tem habilidade com bolas\"",
        "\"amamdomoame ne\"",
        "\"vamo fazer a optativa de fazer jutsu lá\"\n\n\"fazer jutsu?\"\n\n\"é, libras\"",
        "\"ah mlk enfia o stranger things na bunda\"",
        "\"perae que vou dar rage aqui\"",
        "\"ajudo, ajudo, quer que eu escreva o número em que linguagem?\"",
        "\"ai mano esse compilador do rust é muito gay\"",
        "\"olha essa mikasa brasileira 100% jesus completamente gostosa\""]
    tweet_do_dia = random.choice(perolasdovoice)
    return tweet_do_dia

def main():
    tweet = perolas()
    if tweet == "\"olha essa mikasa brasileira 100% jesus completamente gostosa\"":
        api.update_status_with_media(tweet, "minhacasa.png")
    else:
        api.update_status(tweet)

if __name__ == "__main__":
    main()