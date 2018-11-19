'''
Title:QR-code
@author:Haijun Ma
Time:2018/11/19
'''

from MyQR import myqri
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