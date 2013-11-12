#!/usr/bin/env python2

import os
import imp
from nose.tools import assert_raises

try:
    from urllib.request import urlopen
except ImportError:  # Python 2 fallback
    from urllib import urlopen

yturl = imp.load_source("yturl", os.path.join(os.path.dirname(__file__), "../yturl"))
known_itags = yturl.default_itag_order()

def test_itag_order():
    assert known_itags == ['38', '37', '46', '22', '45', '44', '35', '43', '34', '18', '6', '5', '36', '17', '13']

def test_desired_itag_order():
    itag_order = yturl.itag_order("18", known_itags)
    assert itag_order == ('18', '34', '6', '43', '5', '35', '36', '44', '17', '45', '13', '22', '46', '37', '38')

def test_url_stripping():
    assert yturl.strip_to_video_id("http://www.youtube.com/watch?feature=player_embedded&v=gEl6TXrkZnk") == "gEl6TXrkZnk"
    assert yturl.strip_to_video_id("youtu.be/gEl6TXrkZnk#foo") == "gEl6TXrkZnk"

def test_available_itags_parsing():
    with open(os.path.join(os.path.dirname(__file__), "api_output/good"), "rb") as f:
        avail = yturl.available_itags(None, f)
        assert list(avail) == \
            [('43',
              'http://r1---sn-uh-2xol.c.youtube.com/videoplayback?mv=m&ratebypass=yes&source=youtube&ms=au&itag=43&sparams=cp%2Cid%2Cip%2Cipbits%2Citag%2Cratebypass%2Csource%2Cupn%2Cexpire&cp=U0hVSlZLU19HUENONV9ORVdBOlZjeTVCdFBGbVRx&upn=c0mR0CEwjLA&key=yt1&id=2b16823874f4a662&mt=1365582793&newshard=yes&ipbits=8&expire=1365605026&fexp=906373%2C912519%2C904828%2C911305%2C914072%2C916625%2C913813%2C932000%2C932004%2C906383%2C916910%2C902000%2C901208%2C919512%2C929903%2C925714%2C931202%2C900821%2C900823%2C931203%2C931401%2C906090%2C909419%2C908529%2C904830%2C930807%2C919373%2C930803%2C906836%2C920201%2C929602%2C930101%2C900824%2C910223&ip=175.136.239.229&sver=3&signature=CF8569C59EA5BA26893E056A143CE7198B63127F.CB324AEDF80381BA93DDC7E9FC7A1FB4BAF06F10'),
             ('34',
              'http://r1---sn-uh-2xol.c.youtube.com/videoplayback?ip=175.136.239.229&source=youtube&ms=au&itag=34&mv=m&sparams=algorithm%2Cburst%2Ccp%2Cfactor%2Cid%2Cip%2Cipbits%2Citag%2Csource%2Cupn%2Cexpire&cp=U0hVSlZLU19HUENONV9ORVdBOlZjeTVCdFBGbVRx&upn=c0mR0CEwjLA&algorithm=throttle-factor&burst=40&id=2b16823874f4a662&key=yt1&mt=1365582793&newshard=yes&fexp=906373%2C912519%2C904828%2C911305%2C914072%2C916625%2C913813%2C932000%2C932004%2C906383%2C916910%2C902000%2C901208%2C919512%2C929903%2C925714%2C931202%2C900821%2C900823%2C931203%2C931401%2C906090%2C909419%2C908529%2C904830%2C930807%2C919373%2C930803%2C906836%2C920201%2C929602%2C930101%2C900824%2C910223&expire=1365605026&ipbits=8&sver=3&factor=1.25&signature=CB0AABC138D50FD014CC9CE184207B07C584859A.9E2CDB03A977884E98A8D680338B3C6E3D750DA9'),
             ('18',
              'http://r1---sn-uh-2xol.c.youtube.com/videoplayback?mv=m&ratebypass=yes&source=youtube&ms=au&itag=18&sparams=cp%2Cid%2Cip%2Cipbits%2Citag%2Cratebypass%2Csource%2Cupn%2Cexpire&cp=U0hVSlZLU19HUENONV9ORVdBOlZjeTVCdFBGbVRx&upn=c0mR0CEwjLA&key=yt1&id=2b16823874f4a662&mt=1365582793&newshard=yes&ipbits=8&expire=1365605026&fexp=906373%2C912519%2C904828%2C911305%2C914072%2C916625%2C913813%2C932000%2C932004%2C906383%2C916910%2C902000%2C901208%2C919512%2C929903%2C925714%2C931202%2C900821%2C900823%2C931203%2C931401%2C906090%2C909419%2C908529%2C904830%2C930807%2C919373%2C930803%2C906836%2C920201%2C929602%2C930101%2C900824%2C910223&ip=175.136.239.229&sver=3&signature=307E2380C1BF7D8CE460662EE86F78C904BD89CD.9DAED1D7D04B700C0695E80A2CE629DD853DE453'),
             ('5',
              'http://r1---sn-uh-2xol.c.youtube.com/videoplayback?ip=175.136.239.229&source=youtube&ms=au&itag=5&mv=m&sparams=algorithm%2Cburst%2Ccp%2Cfactor%2Cid%2Cip%2Cipbits%2Citag%2Csource%2Cupn%2Cexpire&cp=U0hVSlZLU19HUENONV9ORVdBOlZjeTVCdFBGbVRx&upn=c0mR0CEwjLA&algorithm=throttle-factor&burst=40&id=2b16823874f4a662&key=yt1&mt=1365582793&newshard=yes&fexp=906373%2C912519%2C904828%2C911305%2C914072%2C916625%2C913813%2C932000%2C932004%2C906383%2C916910%2C902000%2C901208%2C919512%2C929903%2C925714%2C931202%2C900821%2C900823%2C931203%2C931401%2C906090%2C909419%2C908529%2C904830%2C930807%2C919373%2C930803%2C906836%2C920201%2C929602%2C930101%2C900824%2C910223&expire=1365605026&ipbits=8&sver=3&factor=1.25&signature=30725A5BE0FE42CE6F9503D3F6C9AAAB23800F58.48C91855BAE589DA4749E48AAC067B89C7A7823D'),
             ('17',
              'http://r1---sn-uh-2xol.c.youtube.com/videoplayback?ip=175.136.239.229&source=youtube&ms=au&itag=17&mv=m&sparams=algorithm%2Cburst%2Ccp%2Cfactor%2Cid%2Cip%2Cipbits%2Citag%2Csource%2Cupn%2Cexpire&cp=U0hVSlZLU19HUENONV9ORVdBOlZjeTVCdFBGbVRx&upn=c0mR0CEwjLA&algorithm=throttle-factor&burst=40&id=2b16823874f4a662&key=yt1&mt=1365582793&newshard=yes&fexp=906373%2C912519%2C904828%2C911305%2C914072%2C916625%2C913813%2C932000%2C932004%2C906383%2C916910%2C902000%2C901208%2C919512%2C929903%2C925714%2C931202%2C900821%2C900823%2C931203%2C931401%2C906090%2C909419%2C908529%2C904830%2C930807%2C919373%2C930803%2C906836%2C920201%2C929602%2C930101%2C900824%2C910223&expire=1365605026&ipbits=8&sver=3&factor=1.25&signature=B4BEF7E233DA97A8BCB5EDBDA337BE3AAD3C9AAA.51924747D449A7CB28D6321AD6BBBCE12962042B')]

def test_quality_group_parsing():
    parse = yturl.quality_group

    assert parse("18", known_itags) == "18"
    assert known_itags.index(parse("high", known_itags)) == 0
    assert known_itags.index(parse("medium", known_itags)) == len(known_itags) // 2
    assert known_itags.index(parse("low", known_itags)) == len(known_itags) - 1

def test_embed_restriction_raises():
    with open(os.path.join(os.path.dirname(__file__), "api_output/embed_restricted"), "rb") as f:
        avail = yturl.available_itags(None, f)
        assert_raises(LookupError, list, avail)
