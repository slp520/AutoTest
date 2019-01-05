from pyhessian.client import HessianProxy
# 从pyhessian导入HessianProxy，用它来发请求
from pyhessian import protocol

'''测dubbo（dubbo是一个java的分布式开源框架）接口，不会写java代码，怎么测，能不能用python来调dubbo接口。当然是可以的了，
    想了解dubbo原理的可以看下这篇文章 http://www.cnblogs.com/Javame/p/3632473.html
    Dubbo本身支持多种远程调用方式，例如Dubbo RPC（二进制序列化 + tcp协议）、http invoker（二进制序列化 + http协议）、hessian（二进制序列化 + http协议）、WebServices （文本序列化 + http协议）等。
    Dubbo是支持hessian+http协议调用的，hessian是一种二进制序列化的方式。
    咱们用python调用的dubbo的时候，就是用hessian+http的方式调用，所以dubbo项目要配置使用hessian方式序列化，
    如果小伙伴要用python调用的时候，注意要找开发小哥哥在项目里面改成hessian方式的序列化，也就是改个配置文件的事，不影响原来的项目
    python调用的时候，hessian+http这种方式调用，需要安装一个第三方模块，python-hessian这个模块

当然我们要调用dubbo接口的话，要知道dubbo接口的调用地址、方法、入参对象和入参，这个就需要开发小哥哥提供给你文档了。

如果没有文档的话，就需要你能看懂java和dubbo的代码了。我这里没有文档，就直接说怎么找这些咱们需要用到的。
 

1、先找到调用地址、接口、方法。

   dubbo是带有服务监控的功能的，这个都有，管开发要地址就行，这个里面可以看到你要测的服务，他里面的地址、方法，
   我们可以看到在dubbo服务监控里面有个HelloApi的服务：
    然后我们带点这个服务进去，就可以看到这个服务是部署在哪个服务器上的，然后点这个服务器的ip进去，就可以看到调用地址、接口、和方法，分别是：
    调用地址：http://192.168.1.100:8181/api/yz.dubbo.api.HelloApi ，#那个页面里写的是hessian，咱们用的是http协议发送的，这里咱们用的时候就改成http方法：hello
2、找到入参对象和入参
   通过dubbo的服务监控，我们可以获得调用地址、接口，入参对象和入参就得看代码了，我们打开项目代码，看到入参类型是在yz.dubbo.api下面的param包里面的Param对象，那么入参对象就是yz.dubbo.api.param.Param，然后我们可以看到这个对象里面有几个属性，也就是它的入参，一个字符串类型的sth，一个整形数组ints，一个字符串键值对maps，对应到咱们python的数据类型就是一个字符串，一个list，一个字典。

   入参对象：yz.dubbo.api.param.Param
    入参：sth、ints、maps

3、调用
   通过上面的东西，咱们调用的dubbo需要用到的东西全部都准备好了，咱们封装一个函数去调用，下面是代码，写好了注释'''
# 这个是用来进行把咱们python的数据类型序列化成二进制的

def dubbo_api(url, interface, method, param_obj, **kwargs):
    '''
    :param url: url地址
    :param interface: 接口名称，因为这里可能还有别的服务要测，接口名不一样，这里定义成变量
    :param method: 调用哪个方法
    :param param_obj: 入参的对象
    :param kwargs: 这个用关键字参数，因为每个接口的参数都不一样，不固定，所以这里用关键字参数
    :return:
        '''
    req_param = protocol.object_factory (param_obj, **kwargs)
    # 这个是用来构造二进制的入参的，也就是把入参序列化
    try:  # 用try捕捉一下异常
        req_obj = HessianProxy (url + interface)
        # 这个req是生成一个请求对象
        res = getattr (req_obj, method) (req_param)
        # getattr是python的内置方法，获取对象的方法，咱们从构造的请求对象里面获取到方法，然后调用，把前面生成的
        # 序列化好的参数传进去，然后获取到返回的数据
    except Exception as e:
        print ('有异常了，异常信息是：%s' % e)
        res = {"msg": "异常：%s" % e, "code": 300}
        # 这个是自己定义的异常，如果调用出错了，就返回这个
    return res


if __name__ == '__main__':
    url = 'http://192.168.1.100:8181/api/'
    interface = 'yz.dubbo.api.HelloApi'
    method = 'hello'
    param_obj = 'yz.dubbo.api.param.Param'
    params = {"sth": "dubbo", "ints": [1, 2, 3], "maps": {"name": "dubbo"}}
    # 这个入参，为了不定义多个变量，咱们把它写成字典形式的,就和stu=dubbo这种方式调用是一样的
    over = dubbo_api (url, interface, method, param_obj, **params)
    # 测试调用一下
    print (over)  # 打印结果