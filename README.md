# interface_test
## 基于requests的接口自动化框架实践
### 用到的技术栈有：Python、Requests、Pytest、Allure、Redis
### 本次以企业微信为例
#### 框架组成：
![image](https://user-images.githubusercontent.com/44678811/158416636-62824329-d678-405b-a61c-86f15f193c5d.png)

#### 接口基类：interface_test\source\main\common\baseApi.py
对URL进行初始化并实例化session，封装获取登录凭证的方法，封装接口请求

#### 前置后置：interface_test\source\main\common\testBaseCase.py
定义基础的测试前后的处理工作

#### 接口录入：interface_test\source\main\api
api文件夹用于存放所有需要测试的接口，按照功能模块划分，这里是成员管理接口：addressBook\memberManagement.py

#### 通用工具：interface_test\source\main\utils
utils用于存放通用工具：  
FileUtils：常用文件的读取与写入封装  
Logger：日志输出格式封装  
RedisUtils：接口运行中的临时数据存入Redis与从Redis中获取数据方法封装  
AssertUtils：接口断言类封装，这里使用jsonpath断言  

#### 资源配置：interface_test\source\resources
resources资源类文件夹：  
application：企业微信的基础配置信息  
setting：文件读取路径以及数据库连接配置  

#### 测试用例：interface_test\testcase
testcase测试用例，与source\main\api中录入的接口一一对应  

#### 测试数据：interface_test\testdata
testdata测试数据，接口用例执行时需要输入的数据
