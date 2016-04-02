from django.core.cache import cache
import requests
from django.conf import settings

class ClientDisney:
        
     @staticmethod
     def get_attractions():
                
        token = ClientDisney.get_auth_token();
        header_token = {'Authorization':'Bearer {0}'.format(token)}
        header_token['X-Conversation-Id'] = '~WDPRO-MOBILE.CLIENT-PROD'
        request_entities = requests.get(settings.CLIENT_DISNEY['url_attractions'],headers=header_token);
        value =  request_entities.json()
        cache.set('attractions', value)

        return value

     @staticmethod
     def get_auth_token():
        
        params_auth = {u'assertion_type':u'public', u'client_id':u'WDPRO-MOBILE.CLIENT-PROD',u'grant_type':u'assertion'}
        headers_auth = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
        request_token  = requests.post(settings.CLIENT_DISNEY['url_auth'],data = params_auth, headers=headers_auth)
        token = request_token.json()['access_token']
        return token




