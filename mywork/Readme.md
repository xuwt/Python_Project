title: 域名Domain注册
---

**说明：**

* 想注册一个域名，但是试了好些都是已经注册过了，估计现在比较短的3到6位的域名已经很难找到了，要想一个一个手动输入判断太麻烦了因此就写了一个python脚本来完成这个事情，把未注册的写到文本文件中，最后再挑选。

## 抓取URL请求

* 首先要分析万网查询的接口，打开[万网查询](http://wanwang.aliyun.com/domain/searchresult/ '万网查询')，打开chrome的开发者工具（ctrl + shift + i），随便输入一个域名，点击查询，选择Network选项，如图：

>   ![network](http://7rflmb.com1.z0.glb.clouddn.com/domain_network.png 'network')
   
* 可以看到Name列有好多get请求，看前缀大概可以明白是什么意思，checkremmend是查询推荐的域名，checkdomain就是我们需要检查域名是否存在的请求了，不过这个列表有好多，点开第一个，可以看到如下图：

>   ![com](http://7rflmb.com1.z0.glb.clouddn.com/domain_com.png 'com')

* 这个是.com请求，那可以设想下面就是.cn了，点开下面的一看还真是，这样分析就基本明朗了。

## 模拟请求

* 利用python模拟请求上图中的RequestURL就可以了，但是请求失败，看了下RequestHeader，有个Referer，试了下，就可以请求成功了。

>   ```
       jQuery111106684873232152313_1445225493501({"module":[{"avail":0,"name":"aklc.com","reason":"Domain exists","tld":"com"}],"success":"true"});
        aklc : 0 
    ```

* 接下来只要用正则匹配拿到avail的值做一下判断就行了，是1的话，就把这个domain保存到txt文件中，具体代码在python文件中写的有，代码比较简单，不多说了。


**注意**
* 进行了多次测试发现，阿里那边会限制请求次数，如果请求不能用的话，就自己按我的方法重新抓一下URL，更改一下代码里面的请求URL的前缀和后缀就可以了。
