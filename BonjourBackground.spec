# -*- mode: python -*-

block_cipher = None


a = Analysis(['background.py'],
             pathex=['/home/kermito/depot/BonjourBackground'],
             binaries=[],
             datas=[("icon.png", "."), ("icon.ico", ".")],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='BonjourBackground',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='icon.ico', uac_admin=True)
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='BonjourBackground')
