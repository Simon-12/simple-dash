# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['run_app.py'],
             pathex=[],
             binaries=[],
             datas=[
				 ('E:/Anaconda3/envs/finance/Lib/site-packages/dash','dash'),
			 	 ('E:/Anaconda3/envs/finance/Lib/site-packages/dash_html_components','dash_html_components'),
                 ('E:/Anaconda3/envs/finance/Lib/site-packages/dash_core_components','dash_core_components'),
                 ('E:/Anaconda3/envs/finance/Lib/site-packages/dash_bootstrap_components','dash_bootstrap_components'),
                 ('E:/Anaconda3/envs/finance/Lib/site-packages/dash_table','dash_table'),
				 ('long_callback.py','.'),
				 ('assets','assets')
				 ],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='app',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None)
