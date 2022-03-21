# -*- mode: python -*-

block_cipher = None


a = Analysis(['SerLect.py'],
             pathex=['d:\\temp\\eclipse\\LibA5\\A5', 'D:\\temp\\eclipse\\SerLect'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=['pystray','PyQt5', 'PyQt5-sip', 'pyqt5-tools', 'setuptools', 'WMI','altgraph', 'matplotlib', 'numpy', 'kiwisolver','et-xmlfile', 'future', 'iso8601','Click','macholib','cycler', 'setuptools', 'PyYAML'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='SerLect',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , icon='serial.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='SerLect')
