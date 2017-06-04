#-*- coding:utf-8 -*-
import requests,re,os,json
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
class migu_go:
    def run(self):
        entry_video=raw_input('Please entry video name:')
        s=requests.Session()
        select_url='http://migu.cmvideo.cn/clt50/publish/clt/resource/miguvideo4/search/characterData.jsp?sdkVersion=24.00.00.00&playerType=4&res=MDPI&filterType=3&clientId=3cc50909062143db7a660ca9807f2577&imei=db58400daec76935cdd80b2b94088f01b3f4e9c6be4d03ae1a75ba2884f9a26b'
        mycookie={'JSESSIONID':'B988D1083618F85805DC1E1619EF9C57','Path':'/clt50'}
        login_header={'Host':'migu.cmvideo.cn','User-Agent':'vivo_y27_android','Content-Type':'application/x-www-form-urlencoded','X_UP_CLIENT_CHANNEL_ID':'24000000-99000-200300140100004','X_UP_CLIENT_ID':'000250','SDKCEId':'27fb3129-5a54-45bc-8af1-7dc8f1155501'}
        post_data={'k':entry_video.decode('gbk').encode('utf8'),'timeparam':'5-25','pageIdx':'1'}
        new_info=s.post(url=select_url,headers=login_header,data=post_data,cookies=mycookie)
        select_content=json.dumps(eval(new_info.text))
        new_dic=json.loads(select_content)
        all_dic=json.dumps(new_dic['searchresult2'])
        every_dic=json.loads(all_dic)
        global choose_dic
        choose_dic={}
        global anothor_dic
        anothor_dic={}
        k=1
        for new in every_dic:
            if 'subList' in new:
                disperse=json.dumps(new['subList'])
                will_disperse=json.loads(disperse)
                for every_lastdic in will_disperse:
                    id_content=every_lastdic['param']
                    video_name=every_lastdic['name']
                    content_id=re.findall('contentId\=(\d*)',id_content)
                    print k,content_id[0],video_name
                    choose_dic[str(k)]=content_id[0]
                    anothor_dic[content_id[0]]=video_name
                    k+=1

            else:
                id_content=new['contParam']
                video_name=new['contName']
                new_id=re.findall('contentId\=(\d*);nodeId',id_content)
                print k,new_id[0],video_name
                choose_dic[str(k)]=new_id[0]
                anothor_dic[new_id[0]]=video_name
                k+=1
        get_id()