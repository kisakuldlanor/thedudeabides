# -*- coding: utf-8 -*-

'''
    Exodus Add-on
    

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''


import re,urllib,urlparse,hashlib,random,string,json,base64,sys

from resources.lib.zmodules import cleantitle
from resources.lib.zmodules import client
from resources.lib.zmodules import cache
from resources.lib.zmodules import directstream
from resources.lib.zmodules import jsunfuck

CODE = '''def retA():
    class Infix:
        def __init__(self, function):
            self.function = function
        def __ror__(self, other):
            return Infix(lambda x, self=self, other=other: self.function(other, x))
        def __or__(self, other):
            return self.function(other)
        def __rlshift__(self, other):
            return Infix(lambda x, self=self, other=other: self.function(other, x))
        def __rshift__(self, other):
            return self.function(other)
        def __call__(self, value1, value2):
            return self.function(value1, value2)
    def my_add(x, y):
        try: return x + y
        except Exception: return str(x) + str(y)
    x = Infix(my_add)
    return %s
param = retA()'''

class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['yesmovies.to']
        self.base_link = 'https://yesmovies.to'
        self.search_link_2 = '/movie/search/%s.html'
        self.info_link = '/ajax/movie_info/%s.html?is_login=false'
        self.server_link = '/ajax/v4_movie_episodes/%s'
        self.embed_link = '/ajax/movie_embed/%s'
        self.token_link = '/ajax/movie_token?eid=%s&mid=%s'
        self.sourcelink = '/ajax/movie_sources/%s?x=%s&y=%s'

    def getImdbTitle(self, imdb):
        try:
            t = 'http://www.omdbapi.com/?i=%s' % imdb
            t = client.request(t)
            t = json.loads(t)
            t = cleantitle.normalize(t['Title'])
            return t
        except:
            return

    def movie(self, imdb, title, localtitle, year):
        try:
            r = self.searchMovie(title)

            if r == None:
                t = cache.get(self.getImdbTitle, 900, imdb)
                if t != title:
                    r = self.searchMovie(t)

            return urllib.urlencode({'url': r, 'episode': 0})
        except:
            return

    def searchMovie(self, title):
        try:
            title = cleantitle.normalize(title)
            url = urlparse.urljoin(self.base_link, self.search_link_2 % urllib.quote_plus(cleantitle.getsearch(title)))
            r = client.request(url, timeout='10')
            r = client.parseDOM(r, 'div', attrs={'class': 'ml-item'})
            r = zip(client.parseDOM(r, 'a', ret='href'), client.parseDOM(r, 'a', ret='title'))
            url = [i[0] for i in r if cleantitle.get(title) == cleantitle.get(i[1])][0]
            return url
        except:
            return

    def tvshow(self, imdb, tvdb, tvshowtitle, localtvshowtitle, year):
        try:
            url = {'imdb': imdb, 'tvdb': tvdb, 'tvshowtitle': tvshowtitle, 'year': year, 'localtvshowtitle': localtvshowtitle}
            url = urllib.urlencode(url)
            return url
        except:
            return

    def searchShow(self, title, season):
        try:
            title = cleantitle.normalize(title)
            search = '%s Season %s' % (title, int(season))
            url = urlparse.urljoin(self.base_link, self.search_link_2 % urllib.quote_plus(cleantitle.getsearch(search)))
            r = client.request(url, timeout='10')
            r = client.parseDOM(r, 'div', attrs={'class': 'ml-item'})
            r = zip(client.parseDOM(r, 'a', ret='href'), client.parseDOM(r, 'a', ret='title'))
            url = [i[0] for i in r if cleantitle.get(search) == cleantitle.get(i[1])][0]
            return url
        except:
            return

    def episode(self, url, imdb, tvdb, title, premiered, season, episode):
        try:
            data = urlparse.parse_qs(url)
            data = dict([(i, data[i][0]) if data[i] else (i, '') for i in data])

            if 'tvshowtitle' in data:
                r = self.searchShow(data['tvshowtitle'], season)

            if r == None:
                t = cache.get(self.getImdbTitle, 900, imdb)
                if t != data['tvshowtitle']:
                    r = self.searchShow(t, season)

            return urllib.urlencode({'url': r, 'episode': episode})
        except:
            return

    def movie_info(self, url):
        try:
            u = urlparse.urljoin(self.base_link, self.info_link)
            u = client.request(u % url)

            q = client.parseDOM(u, 'div', attrs = {'class': 'jtip-quality'})[0]

            y = client.parseDOM(u, 'div', attrs = {'class': 'jt-info'})
            y = [i.strip() for i in y if i.strip().isdigit() and len(i.strip()) == 4][0]

            return y, q
        except:
            return

    def sources(self, url, hostDict, hostprDict):
        try:
            sources = []

            if url is None: return sources

            data = urlparse.parse_qs(url)
            data = dict([(i, data[i][0]) if data[i] else (i, '') for i in data])

            url = data['url']

            try:
                if data['episode'] > 0:
                    episode = data['episode']
                else:
                    episode = None
            except:
                episode = None

            mid = re.findall('-(\d+)', url)[-1]

            try:
                headers = {'Referer': url}
                u = urlparse.urljoin(self.base_link, self.server_link % mid)
                r = client.request(u, headers=headers, XHR=True)
                r = json.loads(r)['html']
                r = client.parseDOM(r, 'div', attrs = {'class': 'pas-list'})
                ids = client.parseDOM(r, 'li', ret='data-id')
                servers = client.parseDOM(r, 'li', ret='data-server')
                labels = client.parseDOM(r, 'a', ret='title')
                r = zip(ids, servers, labels)
                for eid in r:
                    try:
                        try:
                            ep = re.findall('episode.*?(\d+).*?',eid[2].lower())[0]
                        except:
                            ep = 0
                        if (episode is None) or (int(ep) == int(episode)):
                            url = urlparse.urljoin(self.base_link, self.token_link % (eid[0], mid))
                            script = client.request(url)
                            if '$_$' in script:
                                params = self.uncensored1(script)
                            elif script.startswith('[]') and script.endswith('()'):
                                params = self.uncensored2(script)
                            else:
                                raise Exception()
                            u = urlparse.urljoin(self.base_link, self.sourcelink % (eid[0], params['x'], params['y']))
                            r = client.request(u, XHR=True)
                            url = json.loads(r)['playlist'][0]['sources']
                            url = [i['file'] for i in url if 'file' in i]
                            url = [directstream.googletag(i) for i in url]
                            url = [i[0] for i in url if i]
                            for s in url:
                                sources.append({'source': 'gvideo', 'quality': s['quality'], 'language': 'en',
                                                'url': s['url'], 'direct': True, 'debridonly': False})
                    except:
                        pass
            except:
                pass

            return sources
        except:
            return sources

    def resolve(self, url):
        try:
            if self.embed_link in url:
                result = client.request(url, XHR=True)
                url = json.loads(result)['embed_url']
                return url

            try:
                if not url.startswith('http'):
                    url = 'http:' + url

                for i in range(3):
                    u = directstream.googlepass(url)
                    if not u == None: break

                return u
            except:
                return
        except:
            return

    def uncensored(a, b):
        x = '' ; i = 0
        for i, y in enumerate(a):
            z = b[i % len(b) - 1]
            y = int(ord(str(y)[0])) + int(ord(str(z)[0]))
            x += chr(y)
        x = base64.b64encode(x)
        return x

    def uncensored1(self, script):
        try:
            script = '(' + script.split("(_$$)) ('_');")[0].split("/* `$$` */")[-1].strip()
            script = script.replace('(__$)[$$$]', '\'"\'')
            script = script.replace('(__$)[_$]', '"\\\\"')
            script = script.replace('(o^_^o)', '3')
            script = script.replace('(c^_^o)', '0')
            script = script.replace('(_$$)', '1')
            script = script.replace('($$_)', '4')

            vGlobals = {"__builtins__": None, '__name__': __name__, 'str': str, 'Exception': Exception}
            vLocals = {'param': None}
            exec (CODE % script.replace('+', '|x|'), vGlobals, vLocals)
            data = vLocals['param'].decode('string_escape')
            x = re.search('''_x=['"]([^"']+)''', data).group(1)
            y = re.search('''_y=['"]([^"']+)''', data).group(1)
            return {'x': x, 'y': y}
        except:
            pass

    def uncensored2(self, script):
        try:
            js = jsunfuck.JSUnfuck(script).decode()
            x = re.search('''_x=['"]([^"']+)''', js).group(1)
            y = re.search('''_y=['"]([^"']+)''', js).group(1)
            return {'x': x, 'y': y}
        except:
            pass