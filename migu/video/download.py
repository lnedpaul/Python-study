#-*- coding:utf-8 -*-
import re,os,requests,json,time,urllib
from lxml import etree
class func():
    def __init__(self,video_name,new_id,save_add):
        self.video_name=video_name
        self.content_id=new_id
        self.change_add=save_add
    def wait(self):
        first_address=self.change_add.split('\\')
        save_address='\\'.join(first_address)
        s=requests.Session()
        if not os.path.exists(save_address+'\\'+self.video_name):
            os.mkdir(save_address+'\\'+self.video_name)
        full_url='http://migu.cmvideo.cn/clt50/publish/clt/resource/miguvideo4/player/playerData.jsp?contentId='+self.content_id+'&nodeId=&objType=video&nt=4&sdkVersion=24.00.00.00&playerType=4&res=MDPI&filterType=3&clientId=3cc50909062143db7a660ca9807f2577&imei=db58400daec76935cdd80b2b94088f01b3f4e9c6be4d03ae1a75ba2884f9a26b'
        new_data={'jsonStr':'','isDisableAdRequest':''}
        mycookie={'JSESSIONID':'B988D1083618F85805DC1E1619EF9C57','Path':'/clt50'}
        login_header={'Host':'migu.cmvideo.cn','User-Agent':'vivo_y27_android','Content-Type':'application/x-www-form-urlencoded','X_UP_CLIENT_CHANNEL_ID':'24000000-99000-200300140100004','X_UP_CLIENT_ID':'000250','SDKCEId':'27fb3129-5a54-45bc-8af1-7dc8f1155501'}
        palyer_info = s.post(url=full_url,headers=login_header,data=urllib.urlencode(new_data),cookies=mycookie)
        time.sleep(1)
        new_dic=json.dumps(eval(palyer_info.text))
        player_dic=json.loads(new_dic)
        new_header={'Accept':'*/*','Connection':'close','Host':'vod.hcs.cmvideo.cn:8088','Icy-MetaData':'1','Range':'bytes=0-','User-Agent':'MGPlayer4Android/v7.2.0.0'}
        all_videourl= re.sub('vod\.gslb\.cmvideo\.cn','vod.hcs.cmvideo.cn:8088',player_dic['playUrl'])
        all_video=s.get(url=all_videourl,headers=new_header)
        new_str= re.compile('\#EXTINF\:\d*\,')
        new_match= new_str.split(all_video.text)
        k=1
        for every_halfurl in new_match:
            get_newhalfurl=re.sub('\r\n','',every_halfurl)
            all_number=re.findall('/depository/asset/zhengshi/\d{4}/\d{3}/\d{3}/\d{10}/media/',player_dic['playUrl'])
            dis_number=re.findall('.*\.mp4',get_newhalfurl)
            if all_number:
                pass
            elif dis_number:
                new_number=re.findall('cmvideo\.cn(/.*\.mp4)',player_dic['playUrl'])
                all_number=[re.sub(dis_number[0],'',new_number[0])]
            if dis_number:
                video_url='http://vod.hcs.cmvideo.cn:8088'+all_number[0]+get_newhalfurl
                last_url=re.sub('hls_type=2&HlsSubType=2&HlsProfileId=0','jid=936193e7c68a32df561eb6d459f1678f&sjid=subsession_1495523675944&hls_type=2&mtv_session=933374c1b1cd407a1875f347cb7a31d7&HlsSubType=2&HlsProfileId=0',video_url)
                print last_url
                full_video=s.get(url=last_url,headers=new_header)
                print full_video
                filename= open(save_address+'\\'+self.video_name+'\\'+str(k)+'.mpeg','wb')
                filename.write(full_video.content)
                filename.close()
                k+=1

# new_info=[]
# info=func(new_info)
# info.wait()