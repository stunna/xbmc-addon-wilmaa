'''
    Wilmaa XBMC Plugin
    Copyright (C) 2014 stunna

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
import xbmcgui, xbmcplugin

plugin_handle = int(sys.argv[1])

def add_video_item(url, infolabels, img=''):
    listitem = xbmcgui.ListItem(infolabels['title'], iconImage=img, thumbnailImage=img)
    listitem.setInfo('video', infolabels)
    listitem.setProperty('IsPlayable', 'true')
    xbmcplugin.addDirectoryItem(plugin_handle, url, listitem, isFolder=False)

base_url = 'http://iphone.wilmaa.com/iphone_channel/m3u8'
_id = 'plugin.video.wilmaa'
_resdir = "special://home/addons/" + _id + "/resources"

add_video_item('%s/%s.m3u8' % (base_url, 'ard'),{ 'title': 'ARD' }, '%s/media/ard.gif' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'zdf'),{ 'title': 'ZDF' }, '%s/media/zdf.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'wdr'),{ 'title': 'WDR' }, '%s/media/wdr.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'sat1'),{ 'title': 'SAT1' }, '%s/media/sat1.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'rtl'),{ 'title': 'RTL' }, '%s/media/rtl.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'rtl2'),{ 'title': 'RTL2' }, '%s/media/rtl2.jpg' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'pro7'),{ 'title': 'PRO7' }, '%s/media/pro7.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'vox'),{ 'title': 'VOX' }, '%s/media/vox.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'kabel_1'),{ 'title': 'Kabel1' }, '%s/media/kabel1.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'dmax'),{ 'title': 'DMAX' }, '%s/media/dmax.jpg' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'sixx'),{ 'title': 'Sixx' }, '%s/media/sixx.jpg' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'dasvierte'),{ 'title': 'DasVierte' }, '%s/media/dasvierte.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'nickcc'),{ 'title': 'nickCC' }, '%s/media/nickcc.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'superrtl'),{ 'title': 'SuperRTL' }, '%s/media/superrtl.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'viva'),{ 'title': 'Viva' }, '%s/media/viva.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'n24'),{ 'title': 'N24' }, '%s/media/n24.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'ntv'),{ 'title': 'NTV' }, '%s/media/ntv.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'kika'),{ 'title': 'KIKA' }, '%s/media/kika.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'sf1'),{ 'title': 'SRF1' }, '%s/media/srf1.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'sf2'),{ 'title': 'SRF2' }, '%s/media/srf2.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'orf1'),{ 'title': 'ORF1' }, '%s/media/orf1.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'orf2'),{ 'title': 'ORF2' }, '%s/media/orf2.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, '3plus'),{ 'title': '3Plus' }, '%s/media/3plus.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'arte_de'),{ 'title': 'ARTE(DE)' }, '%s/media/arte.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'sfinfo'),{ 'title': 'SRFinfo' }, '%s/media/srfinfo.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, '3sat'),{ 'title': '3SAT' }, '%s/media/3sat.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'zdfneo'),{ 'title': 'ZDFneo' }, '%s/media/zdfneo.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'swr'),{ 'title': 'SWR' }, '%s/media/swr.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'br'),{ 'title': 'BR' }, '%s/media/br.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'phoenix'),{ 'title': 'Phoenix' }, '%s/media/phoenix.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'euronews'),{ 'title': 'Euronews' }, '%s/media/euronews.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'eurosport'),{ 'title': 'Eurosport' }, '%s/media/eurosport.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'joiz'),{ 'title': 'JOIZ' }, '%s/media/joiz.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'rtlnitro'),{ 'title': 'RTLNitro' }, '%s/media/rtlnitro.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'servustv'),{ 'title': 'ServusTV' }, '%s/media/servustv.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'atv'),{ 'title': 'ATV' }, '%s/media/atv.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'cnn'),{ 'title': 'CNN' }, '%s/media/cnn.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'bbcworld'),{ 'title': 'BBCWorld' }, '%s/media/bbcworld.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'tsr1'),{ 'title': 'RTS1' }, '%s/media/rts1.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'tsr2'),{ 'title': 'RTS2' }, '%s/media/rts2.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'tv5monde'),{ 'title': 'TV5Monde' }, '%s/media/tv5monde.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'france2'),{ 'title': 'France2' }, '%s/media/france2.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'france3'),{ 'title': 'France3' }, '%s/media/france3.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'france5'),{ 'title': 'France5' }, '%s/media/france5.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'rtl9'),{ 'title': 'RTL9' }, '%s/media/rtl9.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'tf1'),{ 'title': 'TF1' }, '%s/media/tf1.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'm6'),{ 'title': 'M6' }, '%s/media/m6.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'arte_fr'),{ 'title': 'ARTE(FR)' }, '%s/media/arte.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'rsila1'),{ 'title': 'RSILa1' }, '%s/media/rsila1.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'rsila2'),{ 'title': 'RSILa2' }, '%s/media/rsila2.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'rai1'),{ 'title': 'Rai1' }, '%s/media/rai1.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'rougetv'),{ 'title': 'RougeTV' }, '%s/media/rougetv.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'cartoonnetwork'),{ 'title': 'CartoonNetwork' }, '%s/media/cartoonnetwork.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'latele'),{ 'title': 'LaTele' }, '%s/media/latele.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'canal9'),{ 'title': 'Canal9' }, '%s/media/canal9.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'canalalphaju'),{ 'title': 'CanalAlphaJU' }, '%s/media/canalalpha.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'tele1'),{ 'title': 'Tele1' }, '%s/media/tele1.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'telem1west'),{ 'title': 'TeleM1West' }, '%s/media/telem1.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'telem1ost'),{ 'title': 'TeleM1Ost' }, '%s/media/telem1.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'teletoptg'),{ 'title': 'TeleTopTG' }, '%s/media/teletop.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'teletopzh'),{ 'title': 'TeleTopZH' }, '%s/media/teletop.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'teletopsh'),{ 'title': 'TeleTopSH' }, '%s/media/teletop.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'canalalphane'),{ 'title': 'CanalAlphaNE' }, '%s/media/canalalpha.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'teleticino'),{ 'title': 'TeleTicino' }, '%s/media/teleticino.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'telebasel'),{ 'title': 'TeleBasel' }, '%s/media/telebasel.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'e4'),{ 'title': 'E4' }, '%s/media/e4.png' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'lemanbleu'),{ 'title': 'lemanbleu' }, '%s/media/lemanbleu.jpg' % _resdir)
add_video_item('%s/%s.m3u8' % (base_url, 'film4'),{ 'title': 'Film4' }, '%s/media/film4.jpg' % _resdir)

xbmcplugin.endOfDirectory(plugin_handle)