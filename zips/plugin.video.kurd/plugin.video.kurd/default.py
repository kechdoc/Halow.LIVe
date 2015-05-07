# -*- coding: utf-8 -*-
# please visit 
import xbmc,xbmcgui,xbmcplugin,sys
icons = "http://karwan.tv/images/tvlogo/"
icon = xbmc.translatePath("special://home/addons/plugin.video.karwan-kurdtv/icon.png")
plugin_handle = int(sys.argv[1])
mode = sys.argv[2]
	
def add_video_item(url, infolabels, img=''):
    if 'rtmp://' in url:
        url = url.replace('<playpath>',' playpath=')
        #url = url + ' swfUrl=http://onyxvids.stream.onyxservers.com/[[IMPORT]]/karwan.tv/player_file/flowplayer/player.cluster-3.2.9.swf pageUrl=http://karwan.tv/kurdistan-tv.html live=1'
        url = url + ' swfUrl=http://p.jwpcdn.com/6/11/jwplayer.flash.swf pageUrl=http://karwan.tv/sterk-tv.html live=1'
    url = 'plugin://plugin.video.kurd/?playkurd=' + url + '***' + infolabels['title'] + '***' + img
    listitem = xbmcgui.ListItem(infolabels['title'], iconImage=img, thumbnailImage=img)
    listitem.setInfo('video', infolabels)
    listitem.setProperty('IsPlayable', 'false')
    xbmcplugin.addDirectoryItem(plugin_handle, url, listitem)
    return
	
def iptvxtra_play():
    xbmcPlayer = xbmc.Player()
    idx = mode.replace("?playkurd=", "").replace("###", "|").replace("#x#", "?").replace("#h#", "http://").split('***')
    xbmc.executebuiltin('XBMC.Notification('+idx[1]+' , KARWAN.TV ,5000,'+idx[2]+')')
    listitem = xbmcgui.ListItem( idx[1], iconImage=idx[2], thumbnailImage=idx[2])
    playlist = xbmc.PlayList( xbmc.PLAYLIST_VIDEO )
    playlist.clear()
    playlist.add(idx[0], listitem )
    xbmcPlayer.play(playlist,None,False)
    sys.exit(0)

def main():

    add_video_item('rtmp://live.karwan.tv:1935/kurdsat-tv/<playpath>kurdsat-tv.stream'				,{ 'title': 'KurdSat TV'}, icons + 'kurdsat-tv.png')
    add_video_item('rtmp://live.karwan.tv:1935/kurdsat-news-tv/<playpath>kurdsat-news-tv.stream'	,{ 'title': 'KurdSat News'}, icons + 'kurdsat-news-tv.png')
    add_video_item('rtmp://live.karwan.tv:1935/kurdistan-tv/<playpath>kurdistan-tv.stream'			,{ 'title': 'Kurdistan TV'}, icons + 'kurdistan-tv.png')
    add_video_item('rtmp://live.karwan.tv:1935/zagros-tv/<playpath>zagros-tv.stream'				,{ 'title': 'Zagros TV'}, icons + 'zagros-tv.png')
    add_video_item('rtmp://live.karwan.tv:1935/nalia-tv/<playpath>nalia-tv.stream'					,{ 'title': 'Nalia TV HD'}, icons + 'nalia-tv.png')
    add_video_item('rtmp://live.karwan.tv:1935/nalia-2-tv/<playpath>nalia-2-tv.stream'				,{ 'title': 'Nalia 2 TV HD'}, icons + 'nalia-2-tv.png')
    add_video_item('rtmp://live.karwan.tv:1935/rudaw-tv/<playpath>rudaw-tv.stream'					,{ 'title': 'Rudaw TV'}, icons + 'rudaw.png')
    add_video_item('rtmp://live.karwan.tv:1935/knn-tv/<playpath>knn-tv.stream'						,{ 'title': 'KNN TV'}, icons + 'knn-tv.png')
    #     add_video_item('rtmp://live.karwan.tv:1935/geli-kurdistan-tv/<playpath>geli-kurdistan-tv.stream',{ 'title': 'Geli Kurdistan'}, icons + 'geli-kurdistan-tv.png')
    add_video_item('rtmp://live.karwan.tv:1935/gk-silemani-tv/<playpath>gk-silemani-tv.stream'		,{ 'title': 'GK Silemani TV'}, icons + 'gk-silemani-tv.png')
    add_video_item('rtmp://live.karwan.tv:1935/korek-tv/<playpath>korek-tv.stream'					,{ 'title': 'Korek TV'}, icons + 'korek-tv.png')
    add_video_item('rtmp://live2.karwan.tv/kurdmax-tv/<playpath>kurdmax-tv.stream'				,{ 'title': 'KurdMAX TV'}, icons + 'kurdmax-tv.png')
    add_video_item('rtmp://live.karwan.tv:1935/kanal4/<playpath>kanal4.stream'						,{ 'title': 'Kanal 4'}, icons + 'kanal4.png')
    add_video_item('rtmp://live.karwan.tv:1935/amozhgary-tv/<playpath>amozhgary-tv.stream'			,{ 'title': 'Amozhgary TV'}, icons + 'amozhgary-tv.png')
    add_video_item('rtmp://live.karwan.tv:1935/gem-kurd-tv/<playpath>gem-kurd-tv.stream'			,{ 'title': 'GEM Kurd TV'}, icons + 'gem-kurd-tv.png')
    add_video_item('rtmp://live.karwan.tv:1935/korek-tv/<playpath>korek-tv.stream'					,{ 'title': 'Korek TV'}, icons + 'korek-tv.png')
    add_video_item('rtmp://live.karwan.tv:1935/4sem-tv/<playpath>4sem-tv.stream'					,{ 'title': '4 Sem TV'}, icons + '4sem-tv.png')
    add_video_item('rtmp://live.karwan.tv:1935/gk-silemani-tv/<playpath>gk-silemani-tv.stream'		,{ 'title': 'GK Silemani TV'}, icons + 'gk-silemani-tv.png')
    add_video_item('rtmp://live.karwan.tv:1935/rega-tv/<playpath>rega-tv.stream'					,{ 'title': 'REGA TV'}, icons + 'rega-tv.png')
    add_video_item('rtmp://live.karwan.tv:1935/vin-tv/<playpath>vin-tv.stream'						,{ 'title': 'Vin TV'}, icons + 'vin-tv.png')
    add_video_item('rtmp://live.karwan.tv:1935/jamawar-tv/<playpath>jamawar-tv.stream'				,{ 'title': 'Jamawar TV'}, icons + 'jamawar-tv.png')
    add_video_item('rtmp://live.karwan.tv:1935/newroz-tv/<playpath>newroz-tv.stream'				,{ 'title': 'Newroz TV'}, icons + 'newroz-tv.png')
    add_video_item('rtmp://live2.karwan.tv/waar-tv/<playpath>waar-tv.stream'					,{ 'title': 'WAAR TV'}, icons + 'waar-tv.png')
    add_video_item('rtmp://live.karwan.tv:1935/waar-sport-tv/<playpath>waar-sport-tv.stream'		,{ 'title': 'WAAR Sport TV'}, icons + 'waar-sport-tv.png')
    add_video_item('rtmp://live.karwan.tv:1935/rengin-tv/<playpath>rengin-tv.stream'				,{ 'title': 'Batman TV'}, icons + 'batman-tv.png')
    add_video_item('rtmp://live.karwan.tv:1935/ronahi-tv/<playpath>ronahi-tv.stream'				,{ 'title': 'Ronahi TV'}, icons + 'ronahi-tv.png')
    add_video_item('rtmp://live.karwan.tv:1935/speda-tv/<playpath>speda-tv.stream'					,{ 'title': 'Speda TV'}, icons + 'speda-tv.png')
    add_video_item('rtmp://live.karwan.tv:1935/jamawar-tv/<playpath>jamawar-tv.stream'				,{ 'title': 'Jamawar TV'}, icons + 'jamawar-tv.png')
    add_video_item('rtmp://live.karwan.tv:1935/cira-tv/<playpath>cira-tv.stream'					,{ 'title': 'Cira TV'}, icons + 'cira-tv.png')
    add_video_item('rtmp://live.karwan.tv:1935/payam-tv/<playpath>payam-tv.stream'					,{ 'title': 'Payam TV'}, icons + 'payam-tv.png')
    # add_video_item('rtmp://live.karwan.tv:1935/gk-sport-tv/<playpath>gk-sport-tv.stream'			,{ 'title': 'GK SPORT TV'}, icons + 'gk-sport-tv.png')
    add_video_item('rtmp://live.karwan.tv:1935/km-tv/<playpath>km-tv.stream'						,{ 'title': 'KM TV'}, icons + 'kmtv.png')
    add_video_item('rtmp://live.karwan.tv:1935/kirkuk-tv/<playpath>kirkuk-tv.stream'				,{ 'title': 'KIRKUK TV'}, icons + 'kirkuk-tv.png')
    add_video_item('rtmp://live.karwan.tv:1935/pelistank-tv/<playpath>pelistank-tv.stream'			,{ 'title': 'PELISTANK TV'}, icons + 'pelistank-tv.png')
    add_video_item('rtmp://live.karwan.tv:1935/zarok-tv/<playpath>zarok-tv.stream'					,{ 'title': 'Zarok TV'}, icons + 'zarok-tv.png')#
    add_video_item('http://kurdmax-pepule.karwan.tv:1935/live/sorani/playlist.m3u8'					,{ 'title': 'KurdMax Pepule TV'}, icons + 'kurdmax-tv.png')
    add_video_item('rtmp://super-tv.karwan.tv/Super_Tv/<playpath>Super_Tv'							,{ 'title': 'Super TV'}, icons + 'super-tv.png')
    add_video_item('rtmp://halk-tv.karwan.tv:1935/liveedge/<playpath>live'							,{ 'title': 'Halk TV'}, icons + 'halk-tv.png')
    add_video_item('rtmp://live.karwan.tv:1935/evin-tv/<playpath>evin-tv.stream'					,{ 'title': 'Evin Tv'}, icons + 'evin-tv.png')
    # add_video_item('rtmp://live.karwan.tv:1935/abn-sat-tv/<playpath>abn-sat-tv.stream'				,{ 'title': 'ABN Sat TV'}, icons + 'abn-sat-tv.PNG')
    # add_video_item('rtmp://live.karwan.tv:1935/karwan.tv/<playpath>komala-tv.stream'					,{ 'title': 'ARK TV'}, icons + 'ark-tv.png')
    add_video_item('rtmp://live.karwan.tv:1935/berivan-tv/<playpath>berivan-tv.stream'				,{ 'title': 'Berivan TV'}, icons + 'berivan-tv.PNG')
    add_video_item('rtmp://live.karwan.tv:1935/rudaw-tv/<playpath>rudaw-tv.stream'					,{ 'title': 'Rudaw TV English'}, icons + 'rudaw.png')
    add_video_item('rtmp://live.karwan.tv:1935/tishk-tv/<playpath>tishk-tv.stream'					,{ 'title': 'Tishk TV'}, icons + 'tishk-tv.png')
    add_video_item('rtmp://live.karwan.tv:1935/rojhelat-tv/<playpath>rojhelat-tv.stream'			,{ 'title': 'Rojhelat TV'}, icons + 'rojhelat.png')
    add_video_item('rtmp://live.karwan.tv:1935/komala-tv/<playpath>komala-tv.stream'				,{ 'title': 'Komala TV'}, icons + 'komala-tv.png')
    add_video_item('rtmp://al-hurria-tv.karwan.tv:1935/hurria/<playpath>live'						,{ 'title': 'Al Hurria TV'}, icons + 'al-hurria-tv.png')
    # add_video_item('rtmp://50.7.129.202:1935/batmantv<playpath>batmantv'								,{ 'title': 'Batman TV Express'}, icons + 'batman-tv-express.png')
    add_video_item('rtmp://live.karwan.tv:1935/imc-tv/<playpath>imc-tv.stream'						,{ 'title': 'IMC TV'}, icons + 'imc-tv.png')
    add_video_item('rtmp://live.karwan.tv:1935/med-nuce-tv/<playpath>med-nuce-tv.stream'			,{ 'title': 'MED Nuce TV'}, icons + 'med-nuce-tv.png')
    add_video_item('rtmp://live.karwan.tv:1935/sterk-tv/<playpath>sterk-tv.stream'					,{ 'title': 'Sterk TV'}, icons + 'sterk-tv.png')
    add_video_item('rtmp://live.karwan.tv:1935/med-muzik-tv/<playpath>med-muzik-tv.stream'			,{ 'title': 'MED Muzik TV'}, icons + 'med-muzik-tv.png')
    add_video_item('rtmp://live.karwan.tv:1935/damla-tv/<playpath>damla-tv.stream'					,{ 'title': 'Damla TV'}, icons + 'damla-tv.png')
    add_video_item('rtmp://live.karwan.tv:1935/tv-10 /<playpath>tv-10.stream'						,{ 'title': 'TV 10'}, icons + 'tv-10.png')
    add_video_item('rtmp://live.karwan.tv:1935/yol-tv/<playpath>yol-tv.stream'						,{ 'title': 'Yol TV'}, icons + 'yol-tv.png')
    # add_video_item('rtmp://live.karwan.tv:1935/munzur-tv/<playpath>munzur-tv.stream'					,{ 'title': 'Munzur TV'}, icons + 'munzur-tv.jpg')
    add_video_item('rtmp://live.karwan.tv:1935/denge-tv/<playpath>denge-tv.stream'					,{ 'title': 'Denge TV'}, icons + 'denge-tv.png')
    add_video_item('rtmp://live2.karwan.tv/civan-tv//civan-tv.stream'								,{ 'title': 'Civan TV ZINDÎ'}, icons + 'civan-tv.png')
    add_video_item('rtmp://live1.karwan.tv/falcon-eye-tv/<playpath>falcon-eye-tv.stream'				,{ 'title': 'Falcon Eye TV'}, icons + 'falcon-eye-tv.png')
  
    # add_video_item(''				,{ 'title': ''}, icons + '')
    # add_video_item(''				,{ 'title': ''}, icons + '')
    # add_video_item(''				,{ 'title': ''}, icons + '')
    # add_video_item(''				,{ 'title': ''}, icons + '')

    xbmcplugin.endOfDirectory(plugin_handle)

if 'playkurd' in mode:
    iptvxtra_play()
else:
    main()
