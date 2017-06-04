#-*- coding:utf-8 -*-
import re,os,requests,json,time,urllib
from lxml import etree
import download
def get_id():
    account_content=raw_input('please entry id:')
    save_add= raw_input('please entry address:')
    if account_content=='exit':
        pass
    else:
        account_id=choose_dic[account_content]
        anothor_name=anothor_dic[account_id]
        info=download.func(anothor_name,account_id,save_add)
        info.wait()
        return get_id()
class Miguvideo():
	def run(self):
		print u"""70032516头条70032517娱乐70032518搞笑70032519热播70032520美女70006372电影70006432综艺"""
		nodeId=raw_input('Please entry channel ID:')
		s= requests.Session()
		login_url='http://migu.cmvideo.cn/clt50/uic-service/userInfo/queryByUserId?userId=&sdkVersion=24.00.00.00&playerType=4&res=MDPI&filterType=3&clientId=3cc50909062143db7a660ca9807f2577&imei=db58400daec76935cdd80b2b94088f01b3f4e9c6be4d03ae1a75ba2884f9a26b'
		mycookie={'JSESSIONID':'959290A79FDA207F595272082220684A','Path':'/clt50'}
		login_header={'Host':'migu.cmvideo.cn','User-Agent':'vivo_y27_android','Content-Type':'application/x-www-form-urlencoded','X_UP_CLIENT_CHANNEL_ID':'24000000-99000-200300140100004','X_UP_CLIENT_ID':'000250','SDKCEId':'27fb3129-5a54-45bc-8af1-7dc8f1155501'}
		s.get(url=login_url,headers=login_header,cookies=mycookie)
		every_index='http://migu.cmvideo.cn/clt50/publish/clt/resource/miguvideo4/home/informationData.jsp?nodeId='+nodeId+'&sdkVersion=24.00.00.00&playerType=4&res=MDPI&filterType=3&clientId=3cc50909062143db7a660ca9807f2577&imei=db58400daec76935cdd80b2b94088f01b3f4e9c6be4d03ae1a75ba2884f9a26b'
		info = s.get(url=every_index,headers=login_header)
		new_info = json.dumps(eval(info.text))
		last_info =json.loads(new_info)
		first_info= json.dumps(last_info['recommendList'])
		second_info = json.loads(first_info)
		global choose_dic
		choose_dic={}
		global anothor_dic
		anothor_dic={}
		for all_dic in second_info:
			if 'contList' in all_dic:
				third_info = json.dumps(all_dic['contList'])
				fourth_info = json.loads(third_info)
				k=1
				for last_dic in fourth_info:
					url_name=last_dic['name']
					video_name= re.sub('[?*%\\\/:><|]','',url_name)
					content_id=re.findall('contentId\=(\d*)',last_dic['param'])#得到contentid
					if_id=re.findall('contentId\=\d+',last_dic['param'])
					if if_id:
						print k,content_id[0],video_name
						choose_dic[str(k)]=content_id[0]
						anothor_dic[content_id[0]]=video_name
						k+=1
					else:
						print 'not video'
		get_id()