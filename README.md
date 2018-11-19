
# Python QR-Code


            二维码又称二维条码，常见的二维码为QR Code，QR全称Quick Response，是一个近几年来移动设备上超流行的一种编码方式，
        它比传统的Bar Code条形码能存更多的信息，也能表示更多的数据类型。
            二维条码/二维码（2-dimensional bar code）是用某种特定的几何图形按一定规律在平面（二维方向上）分布的黑白相间的
        图形记录数据符号信息的；在代码编制上巧妙地利用构成计算机内部逻辑基础的“0”、“1”比特流的概念，使用若干个与二进制
        相对应的几何形体来表示文字数值信息，通过图象输入设备或光电扫描设备自动识读以实现信息自动处理：它具有条码技术的
        一些共性：每种码制有其特定的字符集；每个字符占有一定的宽度；具有一定的校验功能等。同时还具有对不同行的信息自动
        识别功能、及处理图形旋转变化点。

  - 堆叠式/行排式
  
        （1）编码原理：建立在一维条码基础之上，按需要堆积成二行或多行。
        （2）有代表性的行排式二维条码有：Code 16K、Code 49、PDF417、MicroPDF417 等。

  - 矩阵式二维码

        （1）编译原理：它是在一个矩形空间通过黑、白像素在矩阵中的不同分布进行编码。在矩阵相应元素位置上，
            用点（方点、圆点或其他形状）的出现表示二进制“1”，点的不出现表示二进制的“0”，点的排列组合确
            定了矩阵式二维条码所代表的意义。
        （2）具有代表性的矩阵式二维条码有：Code One、MaxiCode、QR Code、 Data Matrix、Han Xin Code、
            Grid Matrix 等。

# 概述
  #####   Python二维码生成器

  - 普通二维码
  - 带图片的艺术二维码（黑色与彩色）
  - 动态二维码（黑色与彩色）
  
  # 安装
  
    pip install qrcode
    pip install pillow
    pip install numpy
    pip install imageio
    pip install myqr
    
# 使用方法

 - 普通二维码
 
       （1）myqr https://github.com
                
           在命令后输入链接或者句子作为参数，然后在程序的当前目录中产生相应的二维码图片文件，默认命名为” qrcode.png“。  
              
       （2）myqr https://github.com -v 10 -l Q
       
             · 默认边长是取决于你输入的信息的长度和使用的纠错等级；而默认纠错等级是最高级的H。
             
             · 自定义：如果想要控制边长和纠错水平就使用 -v 和 -l 参数。
                    -v 控制边长，范围是1至40，数字越大边长越大；
                    -l 控制纠错水平，范围是L、M、Q、H，从左到右依次升高。
                    
       （3）myqr https://github.com -n github_qr.jpg  -d .../paths/
         
              · 默认输出文件名是“ qrcode.png "，而默认存储位置是当前目录。
              
              · 自定义：可以自己定义输出名称和位置。注意同名文件会覆盖旧的；
                        -n 控制文件名，格式可以是 .jpg， .png ，.bmp ，.gif ；
                        -d 控制位置。
                        
- 艺术二维码

       （1）myqr https://github.com -p github.jpg
       
            参数-p 用来将QR二维码图像与一张同目录下的图片相结合，产生一张黑白图片。
            
       （2）myqr https://github.com -p github.jpg -c
       
            加上参数 -c 可以使产生的图片由黑白变为彩色的。
       
       （3）myqr https://github.com -p github.jpg [-c] -con 1.5 -bri 1.6
       
            · 参数-con 用以调节图片的对比度，1.0 表示原始图片，更小的值表示更低对比度，更大反之。默认为1.0。
            · 参数 -bri 用来调节图片的亮度，其余用法和取值与 -con 相同。
            
- 动态GIF二维码
        
    - 动态二维码与上述的带图片的二维码的生成方法没什么区别，你只要采用 .gif 格式的图片即可生成黑白或者彩色的动态二维码。但注意如果使用了 -n 参数自定义输出的文件名，切记其格式也必须是 .gif 格式。
    
 # 作为导入文件
 
     #安装模块后
     from MyQR import myqr
     version, level, qr_name = myqr.run(
	        words,
          version=1,
          level='H',
          picture=None,
          colorized=False,
          contrast=1.0,
          brightness=1.0,
          save_name=None,
          save_dir=os.getcwd()
	         )
           
           以下各个参数已经在上文有所介绍
           # help(myqr)
           Positional parameter
            words: str

            Optional parameters
                  version: int, from 1 to 40
                  level: str, just one of ('L','M','Q','H')
                  picutre: str, a filename of a image
                  colorized: bool
                  constrast: float
                  brightness: float
                  save_name: str, the output filename like 'example.png'
                  save_dir: str, the output directory
                  
             
             
# 使用字符

- 数字 0 到 9

- 大小写的英文字母

- 常用英文标点符号和空格

            · , . : ; + - * / \ ~ ! @ # $ % ^ & ` ' = < > [ ] ( ) ? _ { } | and  (space)
            
            
# 使用提示

- 请采用正方形或近似正方形的图片

- 建议在图片尺寸大的时候使用 -v 的值也应该适当变大。


# 依赖库

- pillow
- numpy
- imageio

# 运行环境

- Linux, Windows,Mac + Python 3
