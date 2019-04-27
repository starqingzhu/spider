#coding=utf-8

import requests

def read_config(file,config_dict):
    try:
        with open(file,'r') as f:
            while True:
                line = f.readline().strip()
                if not line:
                    break

                # 去掉url后面的换行符
                line_list = line.split('\t')

                key = line_list[0]
                config_dict[key] = []
                config_dict[key].append(line_list[1])
                config_dict[key].append(line_list[2])
    finally:
        if f:
            f.close()

def download_image(config_dict,out_file):
    for key,value in config_dict.items():
        url_index = len(value) -1
        print key,':',value[url_index]

        # 测试用的url
        # url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1504068152047&di=8b53bf6b8e5deb64c8ac726e260091aa&imgtype=0&src=http%3A%2F%2Fpic.baike.soso.com%2Fp%2F20140415%2Fbki-20140415104220-671149140.jpg'
        # url1='https://platform-lookaside.fbsbx.com/platform/instantgames/profile_pic.jpg?igpid=1549666258467029&height=256&width=256&ext=1543020792&hash=AeRAGGQzqrmiBQSJ'
        # print "url1:", url1, " len:", len(url1)

        url = value[url_index]
        print ("url:%s  len:%d" % (url,len(url)))
        savefile_name="pig/"
        savefile_name += key
        savefile_name += ".jpg"
        print "savefile_name:",savefile_name

        #proxies = {"https":"flkf.d2dt3.com:50202","http":"flkf.d2dt3.com:50202",}
        #response = requests.get(url,proxies=proxies)

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2810.1 Safari/537.36'}
        response = requests.get(url,headers=headers)
        print(response.status_code)
        if response.status_code != 200:
            print(response)
            with open(out_file, 'a+') as f1:
                f1.write("id:")
                f1.write(key)
                f1.write("   error_code:")
                f1.write(str(response.status_code))
                f1.write("\n")
                f1.close()
            continue

        with open(savefile_name, 'wb+') as f:
            f.write(response.content)
            f.close()

if __name__ == '__main__':
    # 1.加载配置文件到内存
    config_dict= {}
    read_config('wxpurls.txt',config_dict)

    #2.下载图片
    out_file = "out_error_filename.txt"
    download_image(config_dict,out_file)

